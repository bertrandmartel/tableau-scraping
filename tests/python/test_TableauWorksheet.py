import pytest
from tests.python.test_common import data as data
from tests.python.test_common import info as info
from tableauscraper import utils
from tableauscraper import dashboard
from tableauscraper.TableauWorksheet import TableauWorksheet
from tableauscraper.TableauDashboard import TableauDashboard
from tableauscraper import TableauScraper as TS
from pytest_mock import MockerFixture
from tests.python.test_common import vqlCmdResponse as vqlCmdResponse
from tests.python.test_common import tableauVizHtmlResponse as tableauVizHtmlResponse
from tests.python.test_common import tableauDataResponse as tableauDataResponse
from tests.python.test_common import fakeUri as fakeUri
from tests.python.test_common import emptyValues as emptyValues
from tests.python.test_common import vqlCmdResponseDictionaryEmpty as vqlCmdResponseDictionaryEmpty

def test_TableauWorksheet(mocker: MockerFixture) -> None:
    ts = TS()
    tableauDataFrame = dashboard.getWorksheet(ts, data, info, "[WORKSHEET1]")
    assert tableauDataFrame.name == "[WORKSHEET1]"
    assert tableauDataFrame.data.shape[0] == 4
    assert tableauDataFrame.data.shape[1] == 2
    assert type(tableauDataFrame) is TableauWorksheet

    columns = tableauDataFrame.getColumns()
    assert type(columns) is list
    assert columns == ["[FIELD1]", "[FIELD2]"]

    selectableColumns = tableauDataFrame.getSelectableColumns()
    assert type(selectableColumns) is list
    assert selectableColumns == ["[FIELD1]"]

    values = tableauDataFrame.getValues("[FIELD1]")
    assert type(values) is list
    assert values == ["2", "3", "4", "5"]

    # column name doesn't exist
    values = tableauDataFrame.getValues("XXX")
    assert type(values) is list
    assert values == []

    # no values
    tableauDataFrame = dashboard.getWorksheet(ts, emptyValues, info, "[WORKSHEET1]")
    values = tableauDataFrame.getValues("[FIELD1]")
    assert type(values) is list
    assert values == []

    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData", return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.select", return_value=vqlCmdResponse)
    ts.loads(fakeUri)
    tableauDataFrame = dashboard.getWorksheet(ts, data, info, "[WORKSHEET1]")
    tableauDataFrameGroup = tableauDataFrame.select("[FIELD1]", "2")
    assert type(tableauDataFrameGroup) is TableauDashboard
    assert len(tableauDataFrameGroup.worksheets) == 1
    assert tableauDataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert tableauDataFrameGroup.worksheets[0].data.shape[0] == 4
    assert tableauDataFrameGroup.worksheets[0].data.shape[1] == 2
    assert list(tableauDataFrameGroup.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]

    # column name doesn't exist
    tableauDataFrameGroup = tableauDataFrame.select("XXXX", "2")
    assert type(tableauDataFrameGroup) is TableauDashboard
    assert len(tableauDataFrameGroup.worksheets) == 0


    #### VQL CMD RESPONSE ####
    tableauDataFrame = dashboard.getWorksheet(ts, data, info, "[WORKSHEET1]")
    tableauDataFrame = tableauDataFrame.select("[FIELD1]", "2").getWorksheet("[WORKSHEET1]")
    assert type(tableauDataFrame) is TableauWorksheet
    assert tableauDataFrame.cmdResponse

    columns = tableauDataFrame.getColumns()
    assert type(columns) is list
    assert columns == ["[FIELD1]", "[FIELD2]"]

    selectableColumns = tableauDataFrame.getSelectableColumns()
    assert type(selectableColumns) is list
    assert selectableColumns == ["[FIELD1]"]

    values = tableauDataFrame.getValues("[FIELD1]")
    assert type(values) is list
    assert values == ["2", "3", "4", "5"]

    # column name doesn't exist
    values = tableauDataFrame.getValues("XXX")
    assert type(values) is list
    assert values == []

    # no values

    mocker.patch("tableauscraper.api.select", return_value=vqlCmdResponseDictionaryEmpty)
    tableauDataFrame = dashboard.getWorksheet(ts, data, info, "[WORKSHEET1]")
    tableauDataFrame = tableauDataFrame.select("[FIELD1]", "2").getWorksheet("[WORKSHEET1]")
    values = tableauDataFrame.getValues("[FIELD1]")
    assert type(values) is list
    assert values == []
    ####



def test_TableauDashboard_getDropdownInputs(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData", return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.select", return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)
    tableauDataFrameGroup = dashboard.getWorksheets(ts, data, info)
    assert type(tableauDataFrameGroup) is TableauDashboard
    assert not tableauDataFrameGroup.cmdResponse

    dropDownInputs = tableauDataFrameGroup.getDropdownInputs()
    assert type(dropDownInputs) is list
    assert dropDownInputs == ["[INPUT_NAME1]", "[INPUT_NAME2]"]

    # in vql cmd response
    tableauDataFrameGroup = tableauDataFrameGroup.getWorksheet("[WORKSHEET1]").select(
        "[FIELD1]", "2"
    )
    assert type(tableauDataFrameGroup) is TableauDashboard
    assert tableauDataFrameGroup.cmdResponse

    dropDownInputs = tableauDataFrameGroup.getDropdownInputs()
    assert type(dropDownInputs) is list
    assert dropDownInputs == ["[INPUT_NAME1]", "[INPUT_NAME2]"]


def test_TableauDashboard_getDropdownValues(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData", return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.select", return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)
    tableauDataFrameGroup = dashboard.getWorksheets(ts, data, info)
    assert type(tableauDataFrameGroup) is TableauDashboard
    assert not tableauDataFrameGroup.cmdResponse

    dropDownValues = tableauDataFrameGroup.getDropdownValues("[INPUT_NAME1]")
    assert type(dropDownValues) is list
    assert dropDownValues == ["select1", "select2", "select3"]

    # missing parameter name
    dropDownValues = tableauDataFrameGroup.getDropdownValues("XXXXX")
    assert type(dropDownValues) is list
    assert dropDownValues == []

    # in vql cmd response
    tableauDataFrameGroup = tableauDataFrameGroup.getWorksheet("[WORKSHEET1]").select(
        "[FIELD1]", "2"
    )
    assert type(tableauDataFrameGroup) is TableauDashboard
    assert tableauDataFrameGroup.cmdResponse

    dropDownValues = tableauDataFrameGroup.getDropdownValues("[INPUT_NAME1]")
    assert type(dropDownValues) is list
    assert dropDownValues == ["select1", "select2", "select3"]

    # vql cmd response missing parameter name
    dropDownValues = tableauDataFrameGroup.getDropdownValues("XXXXX")
    assert type(dropDownValues) is list
    assert dropDownValues == []


def test_TableauDashboard_setDropdown(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData", return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.setParameterValue", return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)
    tableauDataFrameGroup = dashboard.getWorksheets(ts, data, info)
    assert type(tableauDataFrameGroup) is TableauDashboard
    tableauDataFrameGroup = tableauDataFrameGroup.setDropdown(
        "[INPUT_NAME1]", "select1"
    )
    assert type(tableauDataFrameGroup) is TableauDashboard
    assert len(tableauDataFrameGroup.worksheets) == 1
    assert tableauDataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert tableauDataFrameGroup.worksheets[0].data.shape[0] == 4
    assert tableauDataFrameGroup.worksheets[0].data.shape[1] == 2
    assert list(tableauDataFrameGroup.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]

    # chain
    tableauDataFrameGroup = tableauDataFrameGroup.setDropdown(
        "[INPUT_NAME1]", "select1"
    )
    assert type(tableauDataFrameGroup) is TableauDashboard
    assert len(tableauDataFrameGroup.worksheets) == 1
    assert tableauDataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert tableauDataFrameGroup.worksheets[0].data.shape[0] == 4
    assert tableauDataFrameGroup.worksheets[0].data.shape[1] == 2
    assert list(tableauDataFrameGroup.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]

    # wrong input name
    tableauDataFrameGroup = tableauDataFrameGroup.setDropdown("XXXXXXXX", "select1")
    assert type(tableauDataFrameGroup) is TableauDashboard
    assert len(tableauDataFrameGroup.worksheets) == 0
