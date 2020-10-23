import pytest
from tests.python.test_common import data as data
from tests.python.test_common import info as info
from tableauscraper import utils
from tableauscraper import dashboard
from tableauscraper.TableauWorksheet import TableauWorksheet
from tableauscraper.TableauDashboard import TableauDashboard
from tableauscraper import TableauScraper as TS


def test_getDashboard(monkeypatch):
    ts = TS()
    # all worksheet
    monkeypatch.setattr("builtins.input", lambda _: "")
    dataFrameGroup = dashboard.get(ts, data, info, ts.logger)
    assert type(dataFrameGroup) is TableauDashboard
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


def test_getWorksheets():
    ts = TS()
    dataFrameGroup = dashboard.getWorksheets(ts, data, info)
    assert type(dataFrameGroup) is TableauDashboard
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
