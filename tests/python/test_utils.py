import pytest
from tableauscraper import utils
import os.path
import json
from tests.python.test_common import data as data
from tests.python.test_common import info as info
from tests.python.test_common import emptyData as emptyData
from tests.python.test_common import dataWithoutViz as WithoutViz
from tests.python.test_common import dataWithoutPres1 as WithoutPres1
from tests.python.test_common import dataWithoutMapPresModel as WithoutMapPresModel
from tests.python.test_common import dataWithoutMapPres2 as WithoutMapPres2
from tests.python.test_common import vqlCmdResponse as vqlCmdResponse
from tests.python.test_common import noWorksheet as noWorksheet
from tests.python.test_common import (
    vqlCmdResponseEmptyValues as vqlCmdResponseEmptyValues,
)
import logging


def test_listWorksheet():
    presModel = utils.getPresModelVizData(data)
    worksheets = utils.listWorksheet(presModel)
    assert len(worksheets) == 2
    assert worksheets[0] == "[WORKSHEET1]"
    assert worksheets[1] == "[WORKSHEET2]"
    pytest.raises(KeyError, utils.listWorksheet, {})
    pytest.raises(KeyError, utils.listWorksheet, emptyData)
    pytest.raises(KeyError, utils.listWorksheet, WithoutViz)
    pytest.raises(KeyError, utils.listWorksheet, WithoutPres1)
    pytest.raises(KeyError, utils.listWorksheet, WithoutMapPresModel)
    pytest.raises(KeyError, utils.listWorksheet, WithoutMapPres2)


def test_selectWorksheet(monkeypatch):
    logger = logging.getLogger("tableauScraper")
    # all worksheet
    monkeypatch.setattr("builtins.input", lambda _: "")
    worksheets = utils.selectWorksheet(data, logger)
    assert len(worksheets) == 2
    assert worksheets == ["[WORKSHEET1]", "[WORKSHEET2]"]

    # select 1 worksheet
    monkeypatch.setattr("builtins.input", lambda _: "0")
    worksheets = utils.selectWorksheet(data, logger)
    assert len(worksheets) == 1
    assert worksheets == ["[WORKSHEET1]"]

    # return 1 element
    monkeypatch.setattr("builtins.input", lambda _: "")
    pytest.raises(Exception, utils.selectWorksheet, data, logger, single=True)
    monkeypatch.setattr("builtins.input", lambda _: "0")
    assert len(worksheets) == 1
    assert worksheets == ["[WORKSHEET1]"]

    # no worksheet
    worksheets = utils.selectWorksheet(noWorksheet, logger)
    assert len(worksheets) == 0


def test_getIndicesInfo():
    presModel = utils.getPresModelVizData(data)
    indicesInfo = utils.getIndicesInfo(presModel, "[WORKSHEET1]")
    assert len(indicesInfo) == 2
    assert "fieldCaption" in indicesInfo[0]
    assert "valueIndices" in indicesInfo[0]
    assert "aliasIndices" in indicesInfo[0]
    assert "dataType" in indicesInfo[0]
    assert "paneIndices" in indicesInfo[0]
    assert "columnIndices" in indicesInfo[0]
    assert len(indicesInfo[0]["valueIndices"]) == 4
    assert len(indicesInfo[0]["aliasIndices"]) == 0
    assert len(indicesInfo[1]["valueIndices"]) == 0
    assert len(indicesInfo[1]["aliasIndices"]) == 4
    assert indicesInfo[0]["fieldCaption"] == "[FIELD1]"
    assert indicesInfo[1]["fieldCaption"] == "[FIELD2]"

    # check noSelectFilter parameter
    indicesInfo = utils.getIndicesInfo(presModel, "[WORKSHEET1]", noSelectFilter=False)
    assert len(indicesInfo) == 1


def test_getDataFull():
    presModel = utils.getPresModelVizData(data)
    dataFull = utils.getDataFull(presModel)
    # check the extended list is not modified
    assert (
        len(
            data["secondaryInfo"]["presModelMap"]["dataDictionary"]["presModelHolder"][
                "genDataDictionaryPresModel"
            ]["dataSegments"]["0"]["dataColumns"][0]["dataValues"]
        )
        == 6
    )
    assert (
        len(
            data["secondaryInfo"]["presModelMap"]["dataDictionary"]["presModelHolder"][
                "genDataDictionaryPresModel"
            ]["dataSegments"]["1"]["dataColumns"][0]["dataValues"]
        )
        == 3
    )
    assert len(dataFull.keys()) == 2
    assert "cstring" in dataFull
    assert "real" in dataFull
    assert len(dataFull["cstring"]) == 9
    assert len(dataFull["real"]) == 5
    assert dataFull["cstring"] == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    assert dataFull["real"] == [1, 2, 3, 4, 5]


def test_onDataValue():
    newVal = utils.onDataValue(1, [1, 2, 3, 4, 5], ["string1", "string2", "string3"])
    assert newVal == 2
    newVal = utils.onDataValue(-1, [1, 2, 3, 4, 5], ["string1", "string2", "string3"])
    assert newVal == "string1"


def test_getData():
    presModel = utils.getPresModelVizData(data)
    dataFull = utils.getDataFull(presModel)
    indicesInfo = utils.getIndicesInfo(presModel, "[WORKSHEET1]")
    frameData = utils.getData(dataFull, indicesInfo)
    assert len(frameData.keys()) == 2
    assert "[FIELD1]-value" in frameData
    assert "[FIELD2]-alias" in frameData
    assert len(frameData["[FIELD1]-value"]) == 4
    assert len(frameData["[FIELD2]-alias"]) == 4
    assert frameData["[FIELD1]-value"] == ["2", "3", "4", "5"]
    assert frameData["[FIELD2]-alias"] == ["6", "7", "8", "9"]


def test_getDataFullCmdResponse():
    presModel = vqlCmdResponse["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
    dataFull = utils.getDataFullCmdResponse(presModel)
    assert len(dataFull.keys()) == 2
    assert "cstring" in dataFull
    assert "real" in dataFull
    assert len(dataFull["cstring"]) == 9
    assert len(dataFull["real"]) == 5
    assert dataFull["cstring"] == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    assert dataFull["real"] == [1, 2, 3, 4, 5]


def test_listWorksheetCmdResponse():
    presModel = vqlCmdResponse["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
    worksheetList = utils.listWorksheetCmdResponse(presModel)
    assert type(worksheetList) is list
    assert len(worksheetList) == 2
    assert [t["worksheet"] for t in worksheetList] == ["[WORKSHEET1]", "[WORKSHEET2]"]


def test_getWorksheetCmdResponse():
    presModel = vqlCmdResponse["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
    dataFull = utils.getDataFullCmdResponse(presModel)
    worksheet = utils.listWorksheetCmdResponse(presModel)[0]
    frameData = utils.getWorksheetCmdResponse(worksheet, dataFull)
    assert len(frameData.keys()) == 2
    assert "[FIELD1]-value" in frameData
    assert "[FIELD2]-alias" in frameData
    assert len(frameData["[FIELD1]-value"]) == 4
    assert len(frameData["[FIELD2]-alias"]) == 4
    assert frameData["[FIELD1]-value"] == ["2", "3", "4", "5"]
    assert frameData["[FIELD2]-alias"] == ["6", "7", "8", "9"]


def test_selectWorksheetCmdResponse(monkeypatch):
    logger = logging.getLogger("tableauScraper")
    presModel = vqlCmdResponse["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]

    # all worksheet
    monkeypatch.setattr("builtins.input", lambda _: "")
    worksheetList = utils.selectWorksheetCmdResponse(presModel, logger)
    assert type(worksheetList) is list
    assert len(worksheetList) == 2
    assert [t["worksheet"] for t in worksheetList] == ["[WORKSHEET1]", "[WORKSHEET2]"]

    # one worksheet
    monkeypatch.setattr("builtins.input", lambda _: "0")
    worksheetList = utils.selectWorksheetCmdResponse(presModel, logger)
    assert type(worksheetList) is list
    assert len(worksheetList) == 1
    assert [t["worksheet"] for t in worksheetList] == ["[WORKSHEET1]"]


def test_getParameterControlInput():
    parameterControlInput = utils.getParameterControlInput(info)
    assert len(parameterControlInput) == 2
    assert [t["fieldCaption"] for t in parameterControlInput] == [
        "[INPUT_NAME1]",
        "[INPUT_NAME2]",
    ]


def test_getParameterControlVqlResponse():
    presModel = vqlCmdResponse["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
    parameterControl = utils.getParameterControlVqlResponse(presModel)
    assert [t["fieldCaption"] for t in parameterControl] == [
        "[INPUT_NAME1]",
        "[INPUT_NAME2]",
    ]


def test_getDataCmdResponse():
    presModel = vqlCmdResponse["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
    dataFull = utils.getDataFullCmdResponse(presModel)
    indicesInfo = utils.getIndicesInfoVqlResponse(presModel, "[WORKSHEET1]")
    frameData = utils.getDataCmdResponse(dataFull, indicesInfo)
    assert len(frameData.keys()) == 2
    assert "[FIELD1]-value" in frameData
    assert "[FIELD2]-alias" in frameData
    assert len(frameData["[FIELD1]-value"]) == 4
    assert len(frameData["[FIELD2]-alias"]) == 4
    assert frameData["[FIELD1]-value"] == ["2", "3", "4", "5"]
    assert frameData["[FIELD2]-alias"] == ["6", "7", "8", "9"]


def test_getIndicesInfoVqlResponse():
    presModel = vqlCmdResponse["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
    indicesInfo = utils.getIndicesInfoVqlResponse(presModel, "[WORKSHEET1]")
    assert len(indicesInfo) == 2
    assert "fieldCaption" in indicesInfo[0]
    assert "valueIndices" in indicesInfo[0]
    assert "aliasIndices" in indicesInfo[0]
    assert "dataType" in indicesInfo[0]
    assert "paneIndices" in indicesInfo[0]
    assert "columnIndices" in indicesInfo[0]
    assert len(indicesInfo[0]["valueIndices"]) == 4
    assert len(indicesInfo[0]["aliasIndices"]) == 0
    assert len(indicesInfo[1]["valueIndices"]) == 0
    assert len(indicesInfo[1]["aliasIndices"]) == 4
    assert indicesInfo[0]["fieldCaption"] == "[FIELD1]"
    assert indicesInfo[1]["fieldCaption"] == "[FIELD2]"

    # check noSelectFilter parameter
    indicesInfo = utils.getIndicesInfoVqlResponse(
        presModel, "[WORKSHEET1]", noSelectFilter=False
    )
    assert len(indicesInfo) == 1

    # worksheet not found
    indicesInfo = utils.getIndicesInfoVqlResponse(presModel, "XXXXX")
    assert len(indicesInfo) == 0

    ## empty data
    presModel = vqlCmdResponseEmptyValues["vqlCmdResponse"]["layoutStatus"][
        "applicationPresModel"
    ]
    indicesInfo = utils.getIndicesInfoVqlResponse(presModel, "[WORKSHEET1]")
    assert len(indicesInfo) == 0
