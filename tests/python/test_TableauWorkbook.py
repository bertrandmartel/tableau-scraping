import pytest
from tests.python.test_common import data as data
from tableauscraper.TableauWorksheet import TableauWorksheet
from tableauscraper.TableauWorkbook import TableauWorkbook
from pytest_mock import MockerFixture
from tests.python.test_common import tableauVizHtmlResponse as tableauVizHtmlResponse
from tests.python.test_common import tableauDataResponse as tableauDataResponse
from tests.python.test_common import tableauDataResponseWithStoryPoints as tableauDataResponseWithStoryPoints
from tableauscraper import TableauScraper as TS
from tests.python.test_common import fakeUri as fakeUri
from tests.python.test_common import vqlCmdResponse as vqlCmdResponse
from tests.python.test_common import (
    vqlCmdResponseEmptyValues as vqlCmdResponseEmptyValues,
)
from tests.python.test_common import storyPointsCmdResponse as storyPointsCmdResponse
from tests.python.test_common import tableauDownloadableCsvData as tableauDownloadableCsvData


def test_TableauWorkbook(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.select", return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)
    dataFrameGroup = ts.getWorkbook()
    assert type(dataFrameGroup) is TableauWorkbook
    assert "_originalData" in dataFrameGroup.__dict__
    assert dataFrameGroup.__dict__["_scraper"] is ts
    assert not dataFrameGroup.cmdResponse
    assert len(dataFrameGroup.worksheets) == 2

    # get worksheet names (initial response)
    worksheetNames = dataFrameGroup.getWorksheetNames()
    assert type(worksheetNames) is list
    assert not dataFrameGroup.cmdResponse
    assert worksheetNames == ["[WORKSHEET1]", "[WORKSHEET2]"]

    # get worksheet names (vql response)
    dataFrameGroup = dataFrameGroup.worksheets[0].select("[FIELD1]", "2")
    assert dataFrameGroup.cmdResponse
    assert len(dataFrameGroup.worksheets) == 1
    worksheetNames = dataFrameGroup.getWorksheetNames()
    assert type(worksheetNames) is list
    assert worksheetNames == ["[WORKSHEET1]", "[WORKSHEET2]"]

    # get worksheets (initial response)
    dataFrameGroup = ts.getWorkbook()
    dataFrameGroup = dataFrameGroup.getWorksheets()
    assert type(dataFrameGroup) is TableauWorkbook
    assert not dataFrameGroup.cmdResponse
    assert len(dataFrameGroup.worksheets) == 2

    # get worksheets (vql response)
    dataFrameGroup = dataFrameGroup.worksheets[0].select("[FIELD1]", "2")
    dataFrameGroup = dataFrameGroup.getWorksheets()
    assert type(dataFrameGroup) is TableauWorkbook
    assert dataFrameGroup.cmdResponse
    assert len(dataFrameGroup.worksheets) == 1

    # get single worksheet (initial response)
    dataFrameGroup = ts.getWorkbook()
    dataFrame = dataFrameGroup.getWorksheet("[WORKSHEET1]")
    assert type(dataFrame) is TableauWorksheet
    assert not dataFrameGroup.cmdResponse
    assert len(dataFrameGroup.worksheets) == 2

    # get single worksheet (vql response)
    dataFrameGroup = ts.getWorkbook()
    dataFrame = (
        dataFrameGroup.worksheets[0]
        .select("[FIELD1]", "2")
        .getWorksheet("[WORKSHEET1]")
    )
    assert type(dataFrame) is TableauWorksheet
    assert dataFrame.cmdResponse
    assert dataFrame.name == "[WORKSHEET1]"
    assert dataFrame.data.shape[0] == 4
    assert dataFrame.data.shape[1] == 2

    # get single worksheet (vql response) wrong sheet name
    dataFrameGroup = ts.getWorkbook()
    dataFrame = (
        dataFrameGroup.worksheets[0].select(
            "[FIELD1]", "2").getWorksheet("XXXX")
    )
    assert type(dataFrame) is TableauWorksheet
    assert dataFrame.cmdResponse
    assert dataFrame.name == "XXXX"
    assert dataFrame.data.shape[0] == 0
    assert dataFrame.data.shape[1] == 0

    # get single worksheet (vql response) no data
    mocker.patch("tableauscraper.api.select",
                 return_value=vqlCmdResponseEmptyValues)
    dataFrameGroup = ts.getWorkbook()
    dataFrame = (
        dataFrameGroup.worksheets[0]
        .select("[FIELD1]", "2")
        .getWorksheet("[WORKSHEET1]")
    )
    assert type(dataFrame) is TableauWorksheet
    assert dataFrame.cmdResponse
    assert dataFrame.name == "[WORKSHEET1]"
    assert dataFrame.data.shape[0] == 0
    assert dataFrame.data.shape[1] == 0

    # get worksheet names (storypoints)
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponseWithStoryPoints)
    ts = TS()
    ts.loads(fakeUri)
    dataFrameGroup = ts.getWorkbook()
    worksheetNames = dataFrameGroup.getWorksheetNames()
    assert type(worksheetNames) is list
    assert not dataFrameGroup.cmdResponse
    assert worksheetNames == ["[WORKSHEET1]"]

    # get parameters with storypoints
    parameters = dataFrameGroup.getParameters()
    assert type(parameters) is list
    assert parameters == [{
        "column": "[INPUT_NAME1]",
        "values": [
            "select1",
            "select2",
            "select3",
        ],
        "parameterName": "[Parameters].[Parameter 1]"
    }, {
        "column": "[INPUT_NAME2]",
        "values": [
            "select4",
            "select5",
            "select6",
        ],
        "parameterName": "[Parameters].[Parameter 1]",
    }]

    # set parameter with story points on vql cmd response
    mocker.patch("tableauscraper.api.setParameterValue",
                 return_value=storyPointsCmdResponse)
    wb = dataFrameGroup.setParameter("[INPUT_NAME1]", "select1")
    parameters = wb.getParameters()
    assert type(parameters) is list
    assert parameters == [{
        "column": "[INPUT_NAME1]",
        "values": [
            "select1",
            "select2",
            "select3",
        ],
        "parameterName": "[Parameters].[Parameter 1]"
    }, {
        "column": "[INPUT_NAME2]",
        "values": [
            "select4",
            "select5",
            "select6",
        ],
        "parameterName": "[Parameters].[Parameter 1]",
    }]


def test_Sheets(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.goToSheet", return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)
    wb = ts.getWorkbook()

    sheets = wb.getSheets()
    assert sheets == [{
        "sheet": "[WORKSHEET1]",
        "isDashboard": False,
        "isVisible": True,
        "namesOfSubsheets": [],
        "windowId":"{XXXXX}"
    }]

    wbRes = wb.goToSheet("[WORKSHEET1]")
    assert type(wbRes) is TableauWorkbook
    assert len(wbRes.worksheets) == 1
    assert wbRes.worksheets[0].name == "[WORKSHEET1]"

    # sheet not found
    wbRes = wb.goToSheet("XXXXXX")
    assert type(wbRes) is TableauWorkbook
    assert len(wbRes.worksheets) == 0


def test_getCsvData(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.getCsvData",
                 return_value=tableauDownloadableCsvData)
    ts = TS()
    ts.loads(fakeUri)
    wb = ts.getWorkbook()

    data = wb.getCsvData("[WORKSHEET1]")
    print(data)
    assert data.shape[0] == 3
    assert data.shape[1] == 1


def test_getDownloadableData(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.getDownloadableData",
                 return_value=tableauVizHtmlResponse)

    ts = TS()
    ts.loads(fakeUri)

    dataFrameGroup = ts.getWorkbook()
    dataFrameGroup.getDownloadableData(sheetName="[WORKSHEET1]")

    assert type(dataFrameGroup) is TableauWorkbook
    assert "_originalData" in dataFrameGroup.__dict__
    assert dataFrameGroup.__dict__["_scraper"] is ts
    assert not dataFrameGroup.cmdResponse
    assert len(dataFrameGroup.worksheets) == 2
