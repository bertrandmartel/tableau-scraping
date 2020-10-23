import pytest
from tests.python.test_common import data as data
from tableauscraper.TableauWorksheet import TableauWorksheet
from tableauscraper.TableauDashboard import TableauDashboard
from pytest_mock import MockerFixture
from tests.python.test_common import tableauVizHtmlResponse as tableauVizHtmlResponse
from tests.python.test_common import tableauDataResponse as tableauDataResponse
from tableauscraper import TableauScraper as TS
from tests.python.test_common import fakeUri as fakeUri
from tests.python.test_common import vqlCmdResponse as vqlCmdResponse
from tests.python.test_common import (
    vqlCmdResponseEmptyValues as vqlCmdResponseEmptyValues,
)


def test_TableauDashboard(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData", return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.select", return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)
    dataFrameGroup = ts.getDashboard()
    assert type(dataFrameGroup) is TableauDashboard
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
    dataFrameGroup = ts.getDashboard()
    dataFrameGroup = dataFrameGroup.getWorksheets()
    assert type(dataFrameGroup) is TableauDashboard
    assert not dataFrameGroup.cmdResponse
    assert len(dataFrameGroup.worksheets) == 2

    # get worksheets (vql response)
    dataFrameGroup = dataFrameGroup.worksheets[0].select("[FIELD1]", "2")
    dataFrameGroup = dataFrameGroup.getWorksheets()
    assert type(dataFrameGroup) is TableauDashboard
    assert dataFrameGroup.cmdResponse
    assert len(dataFrameGroup.worksheets) == 1

    # get single worksheet (initial response)
    dataFrameGroup = ts.getDashboard()
    dataFrame = dataFrameGroup.getWorksheet("[WORKSHEET1]")
    assert type(dataFrame) is TableauWorksheet
    assert not dataFrameGroup.cmdResponse
    assert len(dataFrameGroup.worksheets) == 2

    # get single worksheet (vql response)
    dataFrameGroup = ts.getDashboard()
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
    dataFrameGroup = ts.getDashboard()
    dataFrame = (
        dataFrameGroup.worksheets[0].select("[FIELD1]", "2").getWorksheet("XXXX")
    )
    assert type(dataFrame) is TableauWorksheet
    assert dataFrame.cmdResponse
    assert dataFrame.name == "XXXX"
    assert dataFrame.data.shape[0] == 0
    assert dataFrame.data.shape[1] == 0

    # get single worksheet (vql response) no data
    mocker.patch("tableauscraper.api.select", return_value=vqlCmdResponseEmptyValues)
    dataFrameGroup = ts.getDashboard()
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
