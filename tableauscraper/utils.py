import pandas as pd
import copy


def selectWorksheet(data, logger, single=False):
    worksheets = listWorksheet(data)
    if len(worksheets) == 0:
        return []
    for idx, ws in enumerate(worksheets):
        logger.info(f"[{idx}] {ws}")

    addText = "" if single == True else "(enter for all)"
    selected = input(f"select worksheet by index {addText}: ")
    if selected:
        return [worksheets[int(selected)]]
    elif single == True:
        raise Exception("you must select one worksheet")
    return worksheets


def listWorksheet(data):
    if "secondaryInfo" not in data:
        raise (KeyError("secondaryInfo field is missing"))

    if "presModelMap" not in data["secondaryInfo"]:
        raise (KeyError('secondaryInfo["presModelMap"] field is missing'))

    if "vizData" not in data["secondaryInfo"]["presModelMap"]:
        raise (KeyError('secondaryInfo["presModelMap"]["vizData"] field is missing'))

    if "presModelHolder" not in data["secondaryInfo"]["presModelMap"]["vizData"]:
        raise (
            KeyError(
                'secondaryInfo["presModelMap"]["vizData"]["presModelHolder"] field is missing'
            )
        )

    if (
        "genPresModelMapPresModel"
        not in data["secondaryInfo"]["presModelMap"]["vizData"]["presModelHolder"]
    ):
        raise (
            KeyError(
                'data["secondaryInfo"]["presModelMap"]["vizData"]["presModelHolder"]["genPresModelMapPresModel"] field is missing'
            )
        )

    if (
        "presModelMap"
        not in data["secondaryInfo"]["presModelMap"]["vizData"]["presModelHolder"][
            "genPresModelMapPresModel"
        ]
    ):
        raise (
            KeyError(
                'data["secondaryInfo"]["presModelMap"]["vizData"]["presModelHolder"]["genPresModelMapPresModel"]["presModelMap"] field is missing'
            )
        )

    return list(
        data["secondaryInfo"]["presModelMap"]["vizData"]["presModelHolder"][
            "genPresModelMapPresModel"
        ]["presModelMap"].keys()
    )


def getIndicesInfo(data, worksheet, noSelectFilter=True):
    genVizDataPresModel = data["secondaryInfo"]["presModelMap"]["vizData"][
        "presModelHolder"
    ]["genPresModelMapPresModel"]["presModelMap"][worksheet]["presModelHolder"][
        "genVizDataPresModel"
    ]

    if "paneColumnsData" not in genVizDataPresModel:
        return []

    columnsData = genVizDataPresModel["paneColumnsData"]
    return [
        {
            "fieldCaption": t.get("fieldCaption", ""),
            "valueIndices": columnsData["paneColumnsList"][t["paneIndices"][0]]["vizPaneColumns"][t["columnIndices"][0]]["valueIndices"],
            "aliasIndices": columnsData["paneColumnsList"][t["paneIndices"][0]]["vizPaneColumns"][t["columnIndices"][0]]["aliasIndices"],
            "dataType": t.get("dataType"),
            "paneIndices": t["paneIndices"][0],
            "columnIndices": t["columnIndices"][0],
        }
        for t in columnsData["vizDataColumns"]
        if t.get("fieldCaption") and (noSelectFilter or (t.get("isAutoSelect") == True))
    ]

def getIndicesInfoVqlResponse(presModel, worksheet, noSelectFilter=True):
    zonesWithWorksheet = listWorksheetCmdResponse(presModel)

    selectedZones = [t for t in zonesWithWorksheet if t["worksheet"] == worksheet]
    if len(selectedZones) == 0:
        return []
    selectedZone = selectedZones[0]

    details = selectedZone["presModelHolder"]["visual"]["vizData"]

    if "paneColumnsData" not in details:
        return []
    columnsData = details["paneColumnsData"]

    return [
        {
            "fieldCaption": t.get("fieldCaption", ""),
            "valueIndices": columnsData["paneColumnsList"][t["paneIndices"][0]]["vizPaneColumns"][t["columnIndices"][0]]["valueIndices"],
            "aliasIndices": columnsData["paneColumnsList"][t["paneIndices"][0]]["vizPaneColumns"][t["columnIndices"][0]]["aliasIndices"],
            "dataType": t.get("dataType"),
            "paneIndices": t["paneIndices"][0],
            "columnIndices": t["columnIndices"][0],
        }
        for t in columnsData["vizDataColumns"]
        if t.get("fieldCaption") and (noSelectFilter or (t.get("isAutoSelect") == True))
    ]

def getDataFull(data):
    dataSegments = data["secondaryInfo"]["presModelMap"]["dataDictionary"][
        "presModelHolder"
    ]["genDataDictionaryPresModel"]["dataSegments"]
    dataSegmentscp = copy.deepcopy(dataSegments)
    dataColumns = []
    for d in list(dataSegmentscp):
        dataColumns.extend(dataSegmentscp[d]["dataColumns"])

    dataFull = {}
    for t in dataColumns:
        if t["dataType"] in dataFull:
            dataFull[t["dataType"]].extend(t["dataValues"])
        else:
            dataFull[t["dataType"]] = t["dataValues"]
    return dataFull


def onDataValue(it, value, cstring):
    return value[it] if (it >= 0) else cstring[abs(it) - 1]


def getData(data, dataFull, indicesInfo):
    cstring = dataFull["cstring"]

    frameData = {}
    for index in indicesInfo:
        if index["dataType"] in dataFull:
            t = dataFull[index["dataType"]]
            if len(index["valueIndices"]) > 0:
                frameData[f'{index["fieldCaption"]}-value'] = [
                    onDataValue(it, t, cstring) for it in index["valueIndices"]
                ]
            if len(index["aliasIndices"]) > 0:
                frameData[f'{index["fieldCaption"]}-alias'] = [
                    onDataValue(it, t, cstring) for it in index["aliasIndices"]
                ]
    return frameData

def getDataCmdResponse(dataFull, indicesInfo):
    cstring = dataFull["cstring"]
    frameData = {}
    for index in indicesInfo:
        if index["dataType"] in dataFull:
            t = dataFull[index["dataType"]]
            if len(index["valueIndices"]) > 0:
                frameData[f'{index["fieldCaption"]}-value'] = [
                    onDataValue(it, t, cstring) for it in index["valueIndices"]
                ]
            if len(index["aliasIndices"]) > 0:
                frameData[f'{index["fieldCaption"]}-alias'] = [
                    onDataValue(it, t, cstring) for it in index["aliasIndices"]
                ]

    return frameData

def getDataFullCmdResponse(presModel):
    dataSegments = presModel["dataDictionary"]["dataSegments"]
    dataSegmentscp = copy.deepcopy(dataSegments)
    dataColumns = []
    for d in list(dataSegmentscp):
        dataColumns.extend(dataSegmentscp[d]["dataColumns"])

    dataFull = {}
    for t in dataColumns:
        if t["dataType"] in dataFull:
            dataFull[t["dataType"]].extend(t["dataValues"])
        else:
            dataFull[t["dataType"]] = t["dataValues"]
    return dataFull


def listWorksheetCmdResponse(presModel):
    zones = presModel["workbookPresModel"]["dashboardPresModel"]["zones"]
    return [
        zones[z]
        for z in list(zones)
        if ("worksheet" in zones[z])
        and ("presModelHolder" in zones[z])
        and ("visual" in zones[z]["presModelHolder"])
        and ("vizData" in zones[z]["presModelHolder"]["visual"])
    ]


def getWorksheetCmdResponse(selectedZone, dataFull):
    cstring = dataFull["cstring"]
    details = selectedZone["presModelHolder"]["visual"]["vizData"]

    if "paneColumnsData" not in details:
        return None
    columnsData = details["paneColumnsData"]

    result = [
        {
            "fieldCaption": t.get("fieldCaption", ""),
            "valueIndices": columnsData["paneColumnsList"][t["paneIndices"][0]]["vizPaneColumns"][t["columnIndices"][0]]["valueIndices"],
            "aliasIndices": columnsData["paneColumnsList"][t["paneIndices"][0]]["vizPaneColumns"][t["columnIndices"][0]]["aliasIndices"],
            "dataType": t.get("dataType"),
            "paneIndices": t["paneIndices"][0],
            "columnIndices": t["columnIndices"][0],
        }
        for t in columnsData["vizDataColumns"]
        if t.get("fieldCaption")
    ]

    frameData = {}
    for index in result:
        if index["dataType"] in dataFull:
            t = dataFull[index["dataType"]]
            if len(index["valueIndices"]) > 0:
                frameData[f'{index["fieldCaption"]}-value'] = [
                    onDataValue(it, t, cstring) for it in index["valueIndices"]
                ]
            if len(index["aliasIndices"]) > 0:
                frameData[f'{index["fieldCaption"]}-alias'] = [
                    onDataValue(it, t, cstring) for it in index["aliasIndices"]
                ]

    return frameData


def selectWorksheetCmdResponse(presModel, logger):
    zonesWithWorksheet = listWorksheetCmdResponse(presModel)

    for idx, z in enumerate(zonesWithWorksheet):
        logger.info(f'[{idx}] {z["worksheet"]}')
    selectedWorksheet = input("select a worksheet (enter for all): ")

    if selectedWorksheet:
        selectedZone = zonesWithWorksheet[int(selectedWorksheet)]
        logger.info(f'you selected : {selectedZone["worksheet"]}')
        zonesWithWorksheet = [selectedZone]
    else:
        logger.info("you selected all worksheet")
    return zonesWithWorksheet


def getParameterControlInput(info):
    zones = info["worldUpdate"]["applicationPresModel"]["workbookPresModel"][
        "dashboardPresModel"
    ]["zones"]
    return [
        zones[key]["presModelHolder"]["parameterControl"]
        for key in list(zones)
        if "parameterControl" in zones[key]["presModelHolder"]
    ]


def getParameterControlVqlResponse(presModel):
    zones = presModel["workbookPresModel"]["dashboardPresModel"]["zones"]
    return [
        zones[z]["presModelHolder"]["parameterControl"]
        for z in list(zones)
        if ("worksheet" in zones[z])
        and ("presModelHolder" in zones[z])
        and ("parameterControl" in zones[z]["presModelHolder"])
    ]
