import pytest
from tests.python.test_common import data as data
from tests.python.test_common import info as info
from tests.python.test_common import tableauDataResponseWithTupleIds as tableauDataResponseWithTupleIds
from tests.python.test_common import dataWithTupleIds as dataWithTupleIds
from tests.python.test_common import vqlCmdResponseWithTupleIds as vqlCmdResponseWithTupleIds
from tests.python.test_common import tableauDataResponseWithStoryPoints as tableauDataResponseWithStoryPoints

from tableauscraper import utils
from tableauscraper import dashboard
from tableauscraper.TableauWorksheet import TableauWorksheet
from tableauscraper.TableauWorkbook import TableauWorkbook
from tableauscraper import TableauScraper as TS
from pytest_mock import MockerFixture
from tests.python.test_common import vqlCmdResponse as vqlCmdResponse
from tests.python.test_common import tableauVizHtmlResponse as tableauVizHtmlResponse
from tests.python.test_common import tableauDataResponse as tableauDataResponse
from tests.python.test_common import fakeUri as fakeUri
from tests.python.test_common import emptyValues as emptyValues
from tests.python.test_common import vqlCmdResponseDictionaryEmpty as vqlCmdResponseDictionaryEmpty
from tests.python.test_common import tooltipCmdResponse as tooltipCmdResponse

from tests.python.test_common import dataWithoutPresModelWithDictionary as dataWithoutPresModelWithDictionary
from tests.python.test_common import storyPointsInfo as storyPointsInfo
from tests.python.test_common import tableauDownloadableSummaryData as tableauDownloadableSummaryData
from tests.python.test_common import tableauDownloadableUnderlyingData as tableauDownloadableUnderlyingData
import json


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

    selectableColumns = tableauDataFrame.getSelectableItems()
    assert type(selectableColumns) is list
    assert selectableColumns == [
        {"column": "[FIELD1]", "values": ["2", "3", "4", "5"]},
        {"column": "[FIELD2]", "values": ["6", "7", "8", "9"]}]

    values = tableauDataFrame.getSelectableValues("[FIELD1]")
    assert type(values) is list
    assert values == ["2", "3", "4", "5"]

    # column name doesn't exist
    values = tableauDataFrame.getSelectableValues("XXX")
    assert type(values) is list
    assert values == []

    # no values
    tableauDataFrame = dashboard.getWorksheet(
        ts, emptyValues, info, "[WORKSHEET1]")
    values = tableauDataFrame.getSelectableValues("[FIELD1]")
    assert type(values) is list
    assert values == []

    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.select", return_value=vqlCmdResponse)
    ts.loads(fakeUri)
    tableauDataFrame = dashboard.getWorksheet(ts, data, info, "[WORKSHEET1]")
    tableauDataFrameGroup = tableauDataFrame.select("[FIELD1]", "2")
    assert type(tableauDataFrameGroup) is TableauWorkbook
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
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert len(tableauDataFrameGroup.worksheets) == 0

    #### VQL CMD RESPONSE ####
    tableauDataFrame = dashboard.getWorksheet(ts, data, info, "[WORKSHEET1]")
    tableauDataFrame = tableauDataFrame.select(
        "[FIELD1]", "2").getWorksheet("[WORKSHEET1]")
    assert type(tableauDataFrame) is TableauWorksheet
    assert tableauDataFrame.cmdResponse

    columns = tableauDataFrame.getColumns()
    assert type(columns) is list
    assert columns == ["[FIELD1]", "[FIELD2]"]

    selectableColumns = tableauDataFrame.getSelectableItems()
    assert type(selectableColumns) is list
    assert selectableColumns == [
        {"column": "[FIELD1]", "values": ["2", "3", "4", "5"]},
        {"column": "[FIELD2]", "values": ["6", "7", "8", "9"]}]

    values = tableauDataFrame.getSelectableValues("[FIELD1]")
    assert type(values) is list
    assert values == ["2", "3", "4", "5"]

    # column name doesn't exist
    values = tableauDataFrame.getSelectableValues("XXX")
    assert type(values) is list
    assert values == []

    # no values

    mocker.patch("tableauscraper.api.select",
                 return_value=vqlCmdResponseDictionaryEmpty)
    tableauDataFrame = dashboard.getWorksheet(ts, data, info, "[WORKSHEET1]")
    tableauDataFrame = tableauDataFrame.select(
        "[FIELD1]", "2").getWorksheet("[WORKSHEET1]")
    values = tableauDataFrame.getSelectableValues("[FIELD1]")
    assert type(values) is list
    assert values == []
    ####

    # story point
    ts = TS()
    tableauDataFrameGroup = dashboard.getWorksheets(
        ts, dataWithoutPresModelWithDictionary, storyPointsInfo)
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert not tableauDataFrameGroup.cmdResponse
    ws = tableauDataFrameGroup.getWorksheet("[WORKSHEET1]")
    values = ws.getSelectableValues("[FIELD1]")
    assert type(values) is list
    assert values == ["2", "3", "4", "5"]


def test_TableauWorkbook_getParameters(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.select", return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)
    tableauDataFrameGroup = dashboard.getWorksheets(ts, data, info)
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert not tableauDataFrameGroup.cmdResponse

    parameters = tableauDataFrameGroup.getParameters()
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
    # in vql cmd response
    tableauDataFrameGroup = tableauDataFrameGroup.getWorksheet("[WORKSHEET1]").select(
        "[FIELD1]", "2"
    )
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert tableauDataFrameGroup.cmdResponse

    parameters = tableauDataFrameGroup.getParameters()
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


def test_TableauWorkbook_setParameter(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.setParameterValue",
                 return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)
    tableauDataFrameGroup = dashboard.getWorksheets(ts, data, info)
    assert type(tableauDataFrameGroup) is TableauWorkbook
    tableauDataFrameGroup = tableauDataFrameGroup.setParameter(
        "[INPUT_NAME1]", "select1"
    )
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert len(tableauDataFrameGroup.worksheets) == 1
    assert tableauDataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert tableauDataFrameGroup.worksheets[0].data.shape[0] == 4
    assert tableauDataFrameGroup.worksheets[0].data.shape[1] == 2
    assert list(tableauDataFrameGroup.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]

    # chain
    tableauDataFrameGroup = tableauDataFrameGroup.setParameter(
        "[INPUT_NAME1]", "select1"
    )
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert len(tableauDataFrameGroup.worksheets) == 1
    assert tableauDataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert tableauDataFrameGroup.worksheets[0].data.shape[0] == 4
    assert tableauDataFrameGroup.worksheets[0].data.shape[1] == 2
    assert list(tableauDataFrameGroup.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]

    # wrong input name
    tableauDataFrameGroup = tableauDataFrameGroup.setParameter(
        "XXXXXXXX", "select1")
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert len(tableauDataFrameGroup.worksheets) == 0


def test_TableauWorkbook_getSelectableItems(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.select", return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)

    tableauDataFrameGroup = dashboard.getWorksheets(ts, data, info)
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert not tableauDataFrameGroup.cmdResponse

    ws = tableauDataFrameGroup.getWorksheet("[WORKSHEET1]")
    selection = ws.getSelectableItems()
    assert type(selection) is list
    assert selection == [
        {"column": "[FIELD1]", "values": ["2", "3", "4", "5"]},
        {"column": "[FIELD2]", "values": ["6", "7", "8", "9"]}]

    # in vql cmd response
    tableauDataFrameGroup = ws.select("[FIELD1]", "2")
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert tableauDataFrameGroup.cmdResponse

    ws = tableauDataFrameGroup.getWorksheet("[WORKSHEET1]")
    selection = ws.getSelectableItems()
    assert type(selection) is list
    assert selection == [
        {"column": "[FIELD1]", "values": ["2", "3", "4", "5"]},
        {"column": "[FIELD2]", "values": ["6", "7", "8", "9"]}]

    # story point
    tableauDataFrameGroup = dashboard.getWorksheets(
        ts, dataWithoutPresModelWithDictionary, storyPointsInfo)
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert not tableauDataFrameGroup.cmdResponse
    ws = tableauDataFrameGroup.getWorksheet("[WORKSHEET1]")
    selection = ws.getSelectableItems()
    assert type(selection) is list
    assert selection == [
        {"column": "[FIELD1]", "values": ["2", "3", "4", "5"]},
        {"column": "[FIELD2]", "values": ["6", "7", "8", "9"]}]


def test_TableauWorkbook_getFilters(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.select", return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)

    tableauDataFrameGroup = dashboard.getWorksheets(ts, data, info)
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert not tableauDataFrameGroup.cmdResponse

    ws = tableauDataFrameGroup.getWorksheet("[WORKSHEET1]")
    filters = ws.getFilters()
    assert type(filters) is list
    assert filters == [
        {
            "column": "FILTER_1",
            "ordinal": 0,
            "values": ["FITLTER_VALUE_1", "FITLTER_VALUE_2", "FITLTER_VALUE_3"],
            "globalFieldName": "[FILTER].[FILTER_1]",
            "selection": [],
            "selectionAlt": []
        },
    ]


def test_TableauWorkbook_setFilter(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.filter",
                 return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)
    tableauDataFrameGroup = dashboard.getWorksheets(ts, data, info)
    assert type(tableauDataFrameGroup) is TableauWorkbook

    ws = tableauDataFrameGroup.getWorksheet("[WORKSHEET1]")
    tableauDataFrameGroup = ws.setFilter(
        "FILTER_1", "FITLTER_VALUE_1"
    )
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert len(tableauDataFrameGroup.worksheets) == 1
    assert tableauDataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert tableauDataFrameGroup.worksheets[0].data.shape[0] == 4
    assert tableauDataFrameGroup.worksheets[0].data.shape[1] == 2
    assert list(tableauDataFrameGroup.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]

    # column not found
    tableauDataFrameGroup = ws.setFilter(
        "UNKNOWN", "FITLTER_VALUE_1"
    )
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert len(tableauDataFrameGroup.worksheets) == 0

    # incorrect value
    tableauDataFrameGroup = ws.setFilter(
        "FILTER_1", "FITLTER_VALUE_X"
    )
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert len(tableauDataFrameGroup.worksheets) == 0


def test_TableauWorkbook_selectWithTupleIds(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponseWithTupleIds)
    mocker.patch("tableauscraper.api.select", return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)
    tableauDataFrameGroup = dashboard.getWorksheets(ts, dataWithTupleIds, info)
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert not tableauDataFrameGroup.cmdResponse

    ws = tableauDataFrameGroup.getWorksheet("[WORKSHEET1]")

    # getTupleIds before select
    tupleIds = ws.getTupleIds()
    assert tupleIds == [[2, 4, 6, 8]]

    tableauDataFrameGroup = ws.select(
        "[FIELD1]", "2"
    )
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert len(tableauDataFrameGroup.worksheets) == 1
    assert tableauDataFrameGroup.worksheets[0].name == "[WORKSHEET1]"

    ws = tableauDataFrameGroup.getWorksheet("[WORKSHEET1]")

    # getTuplesIds empty after select
    tupleIds = ws.getTupleIds()
    assert tupleIds == []

    mocker.patch("tableauscraper.api.select",
                 return_value=vqlCmdResponseWithTupleIds)
    tableauDataFrameGroup = ws.select(
        "[FIELD1]", "2"
    )
    ws = tableauDataFrameGroup.getWorksheet("[WORKSHEET1]")

    # getTuplesIds full after select
    tupleIds = ws.getTupleIds()
    assert tupleIds == [[2, 4, 6, 8]]


def test_getDownloadableSummaryData(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.getDownloadableSummaryData",
                 return_value=json.loads(tableauDownloadableSummaryData))
    ts = TS()
    ts.loads(fakeUri)
    wb = ts.getWorkbook()

    data = wb.getWorksheet("[WORKSHEET1]").getDownloadableSummaryData()
    assert data.shape[0] == 200
    assert data.shape[1] == 8


def test_getDownloadableUnderlyingData(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.getDownloadableUnderlyingData",
                 return_value=json.loads(tableauDownloadableUnderlyingData))
    ts = TS()
    ts.loads(fakeUri)
    wb = ts.getWorkbook()

    data = wb.getWorksheet("[WORKSHEET1]").getDownloadableUnderlyingData()
    assert data.shape[0] == 200
    assert data.shape[1] == 42


def test_levelDrill(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.levelDrill",
                 return_value=vqlCmdResponse)
    ts = TS()
    ts.loads(fakeUri)
    wb = ts.getWorkbook()
    wb = wb.getWorksheet("[WORKSHEET1]").levelDrill(
        drillDown=True)
    assert type(wb) is TableauWorkbook
    assert len(wb.worksheets) == 1
    assert wb.worksheets[0].name == "[WORKSHEET1]"


def test_TableauWorksheet_renderTooltip(mocker: MockerFixture) -> None:
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    mocker.patch("tableauscraper.api.renderTooltipServer",
                 return_value=tooltipCmdResponse)
    ts = TS()
    ts.loads(fakeUri)
    wb = ts.getWorkbook()
    ws = wb.getWorksheet("[WORKSHEET1]")

    tableauDataFrameGroup = ws.renderTooltip(
        x=0, y=0
    )
    assert tableauDataFrameGroup == "<div></div>"
