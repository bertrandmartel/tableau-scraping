import pytest
from tests.python.test_common import data as data
from tests.python.test_common import info as info
from tests.python.test_common import dataWithoutPresModelWithDictionary as dataWithoutPresModelWithDictionary
from tests.python.test_common import storyPointsInfo as storyPointsInfo
from tests.python.test_common import storyPointsCmdResponse as storyPointsCmdResponse

from tableauscraper import utils
from tableauscraper import dashboard
from tableauscraper.TableauWorksheet import TableauWorksheet
from tableauscraper.TableauWorkbook import TableauWorkbook
from tableauscraper import TableauScraper as TS


def test_getWorkbook(monkeypatch):
    ts = TS()
    # all worksheet
    monkeypatch.setattr("builtins.input", lambda _: "")
    dataFrameGroup = dashboard.get(ts, data, info, ts.logger)
    assert type(dataFrameGroup) is TableauWorkbook
    assert len(dataFrameGroup.worksheets) == 2
    assert dataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert dataFrameGroup.worksheets[0].data.shape[0] == 4
    assert dataFrameGroup.worksheets[0].data.shape[1] == 2
    assert list(dataFrameGroup.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]
    assert dataFrameGroup.worksheets[1].name == "[WORKSHEET2]"
    assert dataFrameGroup.worksheets[1].data.shape[0] == 0
    assert dataFrameGroup.worksheets[1].data.shape[1] == 0

    # single worksheet
    monkeypatch.setattr("builtins.input", lambda _: "0")
    dataFrameGroup = dashboard.get(ts, data, info, ts.logger)
    assert len(dataFrameGroup.worksheets) == 1
    assert dataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert dataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert dataFrameGroup.worksheets[0].data.shape[0] == 4
    assert dataFrameGroup.worksheets[0].data.shape[1] == 2


def test_getWorksheet():
    ts = TS()
    tableauDataFrame = dashboard.getWorksheet(ts, data, info, "[WORKSHEET1]")
    assert tableauDataFrame.name == "[WORKSHEET1]"
    assert tableauDataFrame.data.shape[0] == 4
    assert tableauDataFrame.data.shape[1] == 2
    assert type(tableauDataFrame) is TableauWorksheet

    # story point
    tableauDataFrame = dashboard.getWorksheet(
        ts, dataWithoutPresModelWithDictionary, storyPointsInfo, "[WORKSHEET1]")
    assert tableauDataFrame.name == "[WORKSHEET1]"
    assert tableauDataFrame.data.shape[0] == 4
    assert tableauDataFrame.data.shape[1] == 2
    assert type(tableauDataFrame) is TableauWorksheet


def test_getWorksheets():
    ts = TS()
    dataFrameGroup = dashboard.getWorksheets(ts, data, info)
    assert type(dataFrameGroup) is TableauWorkbook
    assert len(dataFrameGroup.worksheets) == 2
    assert dataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert dataFrameGroup.worksheets[0].data.shape[0] == 4
    assert dataFrameGroup.worksheets[0].data.shape[1] == 2
    assert list(dataFrameGroup.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]
    assert dataFrameGroup.worksheets[1].name == "[WORKSHEET2]"
    assert dataFrameGroup.worksheets[1].data.shape[0] == 0
    assert dataFrameGroup.worksheets[1].data.shape[1] == 0

    # story point
    dataFrameGroup = dashboard.getWorksheets(
        ts, dataWithoutPresModelWithDictionary, storyPointsInfo)
    assert type(dataFrameGroup) is TableauWorkbook
    assert len(dataFrameGroup.worksheets) == 1
    assert dataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert dataFrameGroup.worksheets[0].data.shape[0] == 4
    assert dataFrameGroup.worksheets[0].data.shape[1] == 2
    assert list(dataFrameGroup.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]


def test_getWorksheetsCmdResponse():
    ts = TS()
    ts.zones = storyPointsCmdResponse["vqlCmdResponse"]["layoutStatus"][
        "applicationPresModel"]["workbookPresModel"]["dashboardPresModel"]["zones"]
    # story point
    wb = dashboard.getWorksheetsCmdResponse(
        ts, storyPointsCmdResponse)
    assert type(wb) is TableauWorkbook
    assert len(wb.worksheets) == 1
    assert wb.worksheets[0].name == "[WORKSHEET1]"
    assert wb.worksheets[0].data.shape[0] == 4
    assert wb.worksheets[0].data.shape[1] == 2
    assert list(wb.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]
