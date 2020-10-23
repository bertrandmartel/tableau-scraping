import pytest
from pytest_mock import MockerFixture
from tests.python.test_common import tableauVizHtmlResponse as tableauVizHtmlResponse
from tests.python.test_common import tableauDataResponse as tableauDataResponse
from tests.python.test_common import fakeUri as fakeUri
from tests.python.test_common import data as data
from tests.python.test_common import info as info
from tests.python.test_common import vqlCmdResponse as vqlCmdResponse
from tableauscraper import TableauScraper as TS
from tableauscraper.TableauDashboard import TableauDashboard
from tableauscraper.TableauWorksheet import TableauWorksheet


def test_TableauScraper_loads(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData", return_value=tableauDataResponse)
    ts = TS()
    ts.loads(fakeUri)
    assert "vizql_root" in ts.__dict__["tableauData"]
    assert "sessionid" in ts.__dict__["tableauData"]
    assert "sheetId" in ts.__dict__["tableauData"]
    assert ts.__dict__["data"] == data
    assert ts.__dict__["info"] == info


def test_TableauScraper_listWorksheetNames(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData", return_value=tableauDataResponse)
    ts = TS()
    ts.loads(fakeUri)
    assert ts.listWorksheetNames() == ["[WORKSHEET1]", "[WORKSHEET2]"]


def test_TableauScraper_getWorksheets(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData", return_value=tableauDataResponse)
    ts = TS()
    ts.loads(fakeUri)
    dashboard = ts.getDashboard()
    assert len(dashboard.worksheets) == 2
    assert dashboard.worksheets[0].name == "[WORKSHEET1]"
    assert dashboard.worksheets[1].name == "[WORKSHEET2]"


def test_TableauScraper_getWorksheet(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData", return_value=tableauDataResponse)
    ts = TS()
    ts.loads(fakeUri)
    tableauDataFrame = ts.getWorksheet("[WORKSHEET1]")
    assert type(tableauDataFrame) is TableauWorksheet
    assert tableauDataFrame.name == "[WORKSHEET1]"
    assert tableauDataFrame.data.shape[0] == 4
    assert tableauDataFrame.data.shape[1] == 2


def test_TableauScraper_promptDashboard(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData", return_value=tableauDataResponse)
    ts = TS()
    ts.loads(fakeUri)
    mocker.patch("builtins.input", side_effect=[""])
    tableauDataFrameGroup = ts.promptDashboard()
    assert type(tableauDataFrameGroup) is TableauDashboard
    assert len(tableauDataFrameGroup.worksheets) == 2
    assert tableauDataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert tableauDataFrameGroup.worksheets[0].data.shape[0] == 4
    assert tableauDataFrameGroup.worksheets[0].data.shape[1] == 2
    assert list(tableauDataFrameGroup.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]
    assert tableauDataFrameGroup.worksheets[1].name == "[WORKSHEET2]"
    assert tableauDataFrameGroup.worksheets[1].data.shape[0] == 0
    assert tableauDataFrameGroup.worksheets[1].data.shape[1] == 0


def test_TableauScraper_promptDropdown(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData", return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.setParameterValue", return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)
    mocker.patch("builtins.input", side_effect=["0", "0", "0", ""])
    tableauDataFrameGroup = ts.promptDropdown()
    assert type(tableauDataFrameGroup) is TableauDashboard
    assert len(tableauDataFrameGroup.worksheets) == 1
    assert tableauDataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert tableauDataFrameGroup.worksheets[0].data.shape[0] == 4
    assert tableauDataFrameGroup.worksheets[0].data.shape[1] == 2
    assert list(tableauDataFrameGroup.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]


def test_TableauScraper_promptSelect(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData", return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.select", return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)
    mocker.patch("builtins.input", side_effect=["0", "0", "0", ""])
    tableauDataFrameGroup = ts.promptSelect()
    assert type(tableauDataFrameGroup) is TableauDashboard
    assert len(tableauDataFrameGroup.worksheets) == 1
    assert tableauDataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert tableauDataFrameGroup.worksheets[0].data.shape[0] == 4
    assert tableauDataFrameGroup.worksheets[0].data.shape[1] == 2
    assert list(tableauDataFrameGroup.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]
