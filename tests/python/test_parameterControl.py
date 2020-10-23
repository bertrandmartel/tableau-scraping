import pytest
from pytest_mock import MockerFixture
from tableauscraper import parameterControl
from tests.python.test_common import info as info
from tests.python.test_common import vqlCmdResponse as vqlCmdResponse
from tableauscraper import TableauScraper as TS
from tableauscraper.TableauDashboard import TableauDashboard


def test_getParameterControl(mocker: MockerFixture) -> None:
    ts = TS()
    mocker.patch("builtins.input", side_effect=["0", "0", ""])
    mocker.patch("tableauscraper.api.setParameterValue", return_value=vqlCmdResponse)
    tableauDataFrameGroup = parameterControl.get(ts, info, ts.logger)
    assert type(tableauDataFrameGroup) is TableauDashboard
    assert len(tableauDataFrameGroup.worksheets) == 1
    assert tableauDataFrameGroup.worksheets[0].name == "[WORKSHEET1]"
    assert tableauDataFrameGroup.worksheets[0].data.shape[0] == 4
    assert tableauDataFrameGroup.worksheets[0].data.shape[1] == 2
    assert list(tableauDataFrameGroup.worksheets[0].data.columns.values) == [
        "[FIELD1]-value",
        "[FIELD2]-alias",
    ]

    # no input parameter control
    mocker.patch("builtins.input", side_effect=["", "0", ""])
    pytest.raises(Exception, parameterControl.get, ts, info, ts.logger)

    # no input value
    mocker.patch("builtins.input", side_effect=["0", "", ""])
    pytest.raises(Exception, parameterControl.get, ts, info, ts.logger)
