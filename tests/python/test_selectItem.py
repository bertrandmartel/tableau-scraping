import pytest
from tableauscraper import selectItem
from pytest_mock import MockerFixture
from tests.python.test_common import vqlCmdResponse as vqlCmdResponse
from tests.python.test_common import data as data
from tests.python.test_common import info as info
from tests.python.test_common import noWorksheet as noWorksheet
from tests.python.test_common import emptyValues as emptyValues
from tableauscraper import TableauScraper as TS
from tableauscraper.TableauWorkbook import TableauWorkbook


def test_selectItem(mocker: MockerFixture) -> None:
    ts = TS()
    # we want : 1st worksheet / 1st column / 1st value and then all worksheets for this value
    mocker.patch("builtins.input", side_effect=["0", "0", "0", ""])
    mocker.patch("tableauscraper.api.select", return_value=vqlCmdResponse)
    tableauDataFrameGroup = selectItem.get(ts, data, info, ts.logger)
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert len(tableauDataFrameGroup.worksheets) == 1
    assert tableauDataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert tableauDataFrameGroup.worksheets[0].data.shape[0] == 4
    assert tableauDataFrameGroup.worksheets[0].data.shape[1] == 2
    assert list(tableauDataFrameGroup.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]

    # no worksheet
    mocker.patch("builtins.input", side_effect=["0", "0", "0", ""])
    tableauDataFrameGroup = selectItem.get(ts, noWorksheet, info, ts.logger)
    assert type(tableauDataFrameGroup) is TableauWorkbook
    assert len(tableauDataFrameGroup.worksheets) == 0

    # no column name selected
    mocker.patch("builtins.input", side_effect=["0", "", "0", ""])
    pytest.raises(Exception, selectItem.get, ts, data, info, ts.logger)

    # no value selected
    mocker.patch("builtins.input", side_effect=["0", "0", "", ""])
    pytest.raises(Exception, selectItem.get, ts, data, info, ts.logger)

    # no value existing in data
    mocker.patch("builtins.input", side_effect=["0", "0", "0", ""])
    pytest.raises(Exception, selectItem.get, ts, emptyValues, info, ts.logger)
