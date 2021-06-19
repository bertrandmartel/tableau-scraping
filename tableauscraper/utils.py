import pandas as pd
import copy
import json


def selectWorksheet(data, logger, single=False):
    presModelmap = getPresModelVizData(data)
    worksheets = listWorksheet(presModelmap)
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


def getPresModelVizData(data):
    if ("secondaryInfo" in data) and ("presModelMap" in data["secondaryInfo"]) and ("vizData" in data["secondaryInfo"]["presModelMap"]):
        return data["secondaryInfo"]["presModelMap"]
    else:
        return None


def getPresModelVizDataWithoutViz(data):
    if ("secondaryInfo" in data) and ("presModelMap" in data["secondaryInfo"]):
        return data["secondaryInfo"]["presModelMap"]
    else:
        return None


def getPresModelVizInfo(info):
    if ("worldUpdate" in info) and ("applicationPresModel" in info["worldUpdate"]) and ("workbookPresModel" in info["worldUpdate"]["applicationPresModel"]):
        return info["worldUpdate"]["applicationPresModel"]
    return None


def listWorksheetInfo(presModel):
    zones = presModel["workbookPresModel"]["dashboardPresModel"]["zones"]
    return [
        zones[z]["worksheet"]
        for z in list(zones)
        if zones[z] is not None
        and ("worksheet" in zones[z])
        and ("presModelHolder" in zones[z])
        and ("visual" in zones[z]["presModelHolder"])
        # and ("vizData" in zones[z]["presModelHolder"]["visual"])
    ]


def listStoryPointsInfo(presModel):
    zones = presModel["workbookPresModel"]["dashboardPresModel"]["zones"]
    storypoints = [
        zones[z]["presModelHolder"]["flipboard"]["storyPoints"]
        for z in list(zones)
        if zones[z] is not None
        and ("presModelHolder" in zones[z])
        and ("flipboard" in zones[z]["presModelHolder"])
        and ("storyPoints" in zones[z]["presModelHolder"]["flipboard"])
    ]
    stories = []
    if len(storypoints) > 0:
        storypoint = storypoints[0]
        keys = list(storypoint.keys())
        if len(keys) > 0:
            zones = storypoint[keys[0]]["dashboardPresModel"]["zones"]
            stories = [
                zones[z]["worksheet"]
                for z in list(zones)
                if zones[z] is not None
                and ("worksheet" in zones[z])
                and ("presModelHolder" in zones[z])
                and ("visual" in zones[z]["presModelHolder"])
                and ("vizData" in zones[z]["presModelHolder"]["visual"])
            ]
    return stories


def getWorksheetNames(wb):
    return [
        t.name
        for t in wb.worksheets
    ]
    # if scraper.cmdResponse:
    #     presModel = scraper._originalData["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
    #     return [
    #         t["worksheet"]
    #         for t in listWorksheetCmdResponse(presModel)
    #     ]
    # else:
    #     presModel = getPresModelVizData(scraper._originalData)
    #     if presModel is None:
    #         presModel = getPresModelVizInfo(scraper._originalInfo)
    #         worksheets = listWorksheetInfo(presModel)
    #         return listStoryPointsInfo(presModel) if len(worksheets) == 0 else worksheets
    #     return listWorksheet(presModel)


def listWorksheet(presModelMap):
    if "presModelHolder" not in presModelMap["vizData"]:
        raise (
            KeyError(
                'presModelMap["vizData"]["presModelHolder"] field is missing'
            )
        )

    if (
        "genPresModelMapPresModel"
        not in presModelMap["vizData"]["presModelHolder"]
    ):
        raise (
            KeyError(
                'presModelMap["vizData"]["presModelHolder"]["genPresModelMapPresModel"] field is missing'
            )
        )

    if (
        "presModelMap"
        not in presModelMap["vizData"]["presModelHolder"][
            "genPresModelMapPresModel"
        ]
    ):
        raise (
            KeyError(
                'presModelMap["vizData"]["presModelHolder"]["genPresModelMapPresModel"]["presModelMap"] field is missing'
            )
        )

    return list(
        presModelMap["vizData"]["presModelHolder"][
            "genPresModelMapPresModel"
        ]["presModelMap"].keys()
    )


def getIndicesInfo(presModelMap, worksheet, noSelectFilter=True, noFieldCaption=False):
    genVizDataPresModel = presModelMap["vizData"][
        "presModelHolder"
    ]["genPresModelMapPresModel"]["presModelMap"][worksheet]["presModelHolder"][
        "genVizDataPresModel"
    ]

    if "paneColumnsData" not in genVizDataPresModel:
        return []

    columnsData = genVizDataPresModel["paneColumnsData"]
    result = []
    for t in columnsData["vizDataColumns"]:
        if (t.get("fieldCaption") or noFieldCaption) and (noSelectFilter or (t.get("isAutoSelect") == True)):
            indexLength = len(t["paneIndices"])
            for index in range(indexLength):
                pandeIndex = t["paneIndices"][index]
                columnIndex = t["columnIndices"][index]
                result.append({
                    "fieldCaption": t.get("fieldCaption", ""),
                    "tupleIds": columnsData["paneColumnsList"][pandeIndex]["vizPaneColumns"][columnIndex]["tupleIds"],
                    "valueIndices": columnsData["paneColumnsList"][pandeIndex]["vizPaneColumns"][columnIndex]["valueIndices"],
                    "aliasIndices": columnsData["paneColumnsList"][pandeIndex]["vizPaneColumns"][columnIndex]["aliasIndices"],
                    "dataType": t.get("dataType", ""),
                    "paneIndices": pandeIndex,
                    "columnIndices": columnIndex,
                    "fn": t.get("fn", "")
                })
    return result


def getIndicesInfoVqlResponse(presModel, worksheet, noSelectFilter=True, noFieldCaption=False):
    zonesWithWorksheet = listWorksheetCmdResponse(presModel)

    selectedZones = [
        t for t in zonesWithWorksheet if t["worksheet"] == worksheet]
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
            "tupleIds": columnsData["paneColumnsList"][t["paneIndices"][0]]["vizPaneColumns"][t["columnIndices"][0]]["tupleIds"],
            "valueIndices": columnsData["paneColumnsList"][t["paneIndices"][0]]["vizPaneColumns"][t["columnIndices"][0]]["valueIndices"],
            "aliasIndices": columnsData["paneColumnsList"][t["paneIndices"][0]]["vizPaneColumns"][t["columnIndices"][0]]["aliasIndices"],
            "dataType": t.get("dataType", ""),
            "paneIndices": t["paneIndices"][0],
            "columnIndices": t["columnIndices"][0],
            "fn": t.get("fn", "")
        }
        for t in columnsData["vizDataColumns"]
        if (t.get("fieldCaption") or noFieldCaption) and (noSelectFilter or (t.get("isAutoSelect") == True))
    ]


def getIndicesInfoStoryPoint(presModel, worksheet, noSelectFilter=True, noFieldCaption=False):
    zonesWithWorksheet = listWorksheetStoryPoint(presModel)

    selectedZones = [
        t for t in zonesWithWorksheet if t["worksheet"] == worksheet]
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
            "tupleIds": columnsData["paneColumnsList"][t["paneIndices"][0]]["vizPaneColumns"][t["columnIndices"][0]]["tupleIds"],
            "valueIndices": columnsData["paneColumnsList"][t["paneIndices"][0]]["vizPaneColumns"][t["columnIndices"][0]]["valueIndices"],
            "aliasIndices": columnsData["paneColumnsList"][t["paneIndices"][0]]["vizPaneColumns"][t["columnIndices"][0]]["aliasIndices"],
            "dataType": t.get("dataType", ""),
            "paneIndices": t["paneIndices"][0],
            "columnIndices": t["columnIndices"][0],
            "fn": t.get("fn", "")
        }
        for t in columnsData["vizDataColumns"]
        if (t.get("fieldCaption") or noFieldCaption) and (noSelectFilter or (t.get("isAutoSelect") == True))
    ]


def getDataFull(presModelMap, originSegments):
    dataSegments = {}
    if ("dataDictionary" in presModelMap) and ("presModelHolder" in presModelMap["dataDictionary"]):
        dataSegments = presModelMap["dataDictionary"]["presModelHolder"]["genDataDictionaryPresModel"]["dataSegments"]

    dataSegmentscp = copy.deepcopy(dataSegments)
    originSegmentscp = copy.deepcopy(originSegments)
    dataColumns = []
    for d in list(originSegmentscp):
        dataColumns.extend(originSegmentscp[d]["dataColumns"])

    for d in list(dataSegmentscp):
        if d not in originSegments:
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


def getData(dataFull, indicesInfo):
    if "cstring" in dataFull:
        cstring = dataFull["cstring"]
    else:
        cstring = {}
    frameData = {}
    for index in indicesInfo:
        if index["dataType"] in dataFull:
            t = dataFull[index["dataType"]]
            if len(index["valueIndices"]) > 0:
                values = []
                for value in index["valueIndices"]:
                    if value < len(t):
                        values.append(onDataValue(value, t, cstring))
                frameData[f'{index["fieldCaption"]}-value'] = values
            if len(index["aliasIndices"]) > 0:
                values = []
                for value in index["aliasIndices"]:
                    if value < len(t):
                        values.append(onDataValue(value, t, cstring))
                frameData[f'{index["fieldCaption"]}-alias'] = values
        else:
            # if datatype is not found, try cstring
            t = cstring
            if len(index["valueIndices"]) > 0:
                values = []
                for value in index["valueIndices"]:
                    if value < len(t):
                        values.append(onDataValue(value, t, cstring))
                frameData[f'{index["fieldCaption"]}-value'] = values
            if len(index["aliasIndices"]) > 0:
                values = []
                for value in index["aliasIndices"]:
                    if value < len(t):
                        values.append(onDataValue(value, t, cstring))
                frameData[f'{index["fieldCaption"]}-alias'] = values
    return frameData


def getDataFullCmdResponse(presModel, originSegments, dataSegments={}):
    if (not dataSegments) and ("dataDictionary" in presModel):
        dataSegments = presModel["dataDictionary"]["dataSegments"]
    dataSegmentscp = copy.deepcopy(dataSegments)
    originSegmentscp = copy.deepcopy(originSegments)
    dataColumns = []
    for d in list(originSegmentscp):
        dataColumns.extend(originSegmentscp[d]["dataColumns"])

    for d in list(dataSegmentscp):
        if d not in originSegments:
            dataColumns.extend(dataSegmentscp[d]["dataColumns"])

    dataFull = {}
    for t in dataColumns:
        if t["dataType"] in dataFull:
            dataFull[t["dataType"]].extend(t["dataValues"])
        else:
            dataFull[t["dataType"]] = t["dataValues"]
    return dataFull


def getStoryPointsFromInfo(info):
    result = {
        "storyBoard": "",
        "storyPoints": []
    }
    if "sheetName" in info:
        result["storyBoard"] = info["sheetName"]
    else:
        print("sheet name not found")
        return result
    presModel = getPresModelVizInfo(info)
    if (("workbookPresModel" in presModel) and
        ("dashboardPresModel" in presModel["workbookPresModel"]) and
            ("zones" in presModel["workbookPresModel"]["dashboardPresModel"])):
        zones = presModel["workbookPresModel"]["dashboardPresModel"]["zones"]
        storyPointsNav = [
            zones[z]["presModelHolder"]["flipboardNav"]["storypointNavItems"]
            for z in list(zones)
            if zones[z] is not None
            and ("presModelHolder" in zones[z])
            and "flipboardNav" in zones[z]["presModelHolder"]
            and "storypointNavItems" in zones[z]["presModelHolder"]["flipboardNav"]
        ]
        storyPointsList = []
        for t in storyPointsNav:
            storyPoints = []
            for story in t:
                storyPoints.append({
                    "storyPointId": story["storyPointId"],
                    "storyPointCaption": story["storyPointCaption"]
                })
            storyPointsList.append(storyPoints)
        result["storyPoints"] = storyPointsList
        return result
    return result


def listWorksheetCmdResponse(presModel):
    zones = presModel["workbookPresModel"]["dashboardPresModel"]["zones"]
    return [
        zones[z]
        for z in list(zones)
        if zones[z] is not None
        and ("worksheet" in zones[z])
        and ("presModelHolder" in zones[z])
        and ("visual" in zones[z]["presModelHolder"])
        and ("vizData" in zones[z]["presModelHolder"]["visual"])
    ]


def listStoryPointsCmdResponse(presModel):
    zones = presModel["workbookPresModel"]["dashboardPresModel"]["zones"]
    storypoints = [
        zones[z]["presModelHolder"]["flipboard"]["storyPoints"]
        for z in list(zones)
        if zones[z] is not None
        and ("presModelHolder" in zones[z])
        and ("flipboard" in zones[z]["presModelHolder"])
        and ("storyPoints" in zones[z]["presModelHolder"]["flipboard"])
    ]
    stories = []
    if len(storypoints) > 0:
        storypoint = storypoints[0]
        keys = list(storypoint.keys())
        if len(keys) > 0:
            zones = storypoint[keys[0]]["dashboardPresModel"]["zones"]
            stories = [
                zones[z]
                for z in list(zones)
                if zones[z] is not None
                and ("worksheet" in zones[z])
                and ("presModelHolder" in zones[z])
                and ("visual" in zones[z]["presModelHolder"])
                and ("vizData" in zones[z]["presModelHolder"]["visual"])
            ]
    return stories


def listWorksheetStoryPoint(presModel, hasWorksheet=True):
    zones = presModel["workbookPresModel"]["dashboardPresModel"]["zones"]
    storypoints = [
        zones[z]["presModelHolder"]["flipboard"]["storyPoints"]
        for z in list(zones)
        if zones[z] is not None
        and ("presModelHolder" in zones[z])
        and ("flipboard" in zones[z]["presModelHolder"])
        and ("storyPoints" in zones[z]["presModelHolder"]["flipboard"])
    ]
    stories = []
    if len(storypoints) > 0:
        storypoint = storypoints[0]
        keys = list(storypoint.keys())
        if len(keys) > 0:
            zones = storypoint[keys[0]]["dashboardPresModel"]["zones"]
            if hasWorksheet:
                stories = [
                    zones[z]
                    for z in list(zones)
                    if zones[z] is not None
                    and ("worksheet" in zones[z])
                    and ("presModelHolder" in zones[z])
                    and ("visual" in zones[z]["presModelHolder"])
                    and ("vizData" in zones[z]["presModelHolder"]["visual"])
                ]
            else:
                stories = [
                    zones[z]
                    for z in list(zones)
                    if ("presModelHolder" in zones[z])
                ]
    return stories


def getWorksheetCmdResponse(selectedZone, dataFull):
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
    return getData(dataFull, result)


def getWorksheetDownloadCmdResponse(dataFull, underlyingDataTableColumns):
    result = [
        {
            "fieldCaption": t["fieldCaption"],
            "valueIndices": t["valueIndices"],
            "aliasIndices": t["aliasIndices"],
            "dataType": t["dataType"]
        }
        for t in underlyingDataTableColumns
        if t.get("fieldCaption")
    ]
    return getData(dataFull, result)


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
    presModel = getPresModelVizInfo(info)
    storyPointZones = listWorksheetStoryPoint(presModel, hasWorksheet=False)
    if len(storyPointZones) == 0:
        zones = presModel["workbookPresModel"]["dashboardPresModel"]["zones"]
        return [
            {
                "column": zones[key]["presModelHolder"]["parameterControl"]["fieldCaption"],
                "values": zones[key]["presModelHolder"]["parameterControl"]["formattedValues"],
                "parameterName": zones[key]["presModelHolder"]["parameterControl"]["parameterName"]
            }
            for key in list(zones)
            if "parameterControl" in zones[key]["presModelHolder"]
        ]
    return [
        {
            "column": zone["presModelHolder"]["parameterControl"]["fieldCaption"],
            "values": zone["presModelHolder"]["parameterControl"]["formattedValues"],
            "parameterName": zone["presModelHolder"]["parameterControl"]["parameterName"]
        }
        for zone in storyPointZones
        if "parameterControl" in zone["presModelHolder"]
    ]


def getParameterControlVqlResponse(presModel):
    zones = presModel["workbookPresModel"]["dashboardPresModel"]["zones"]
    zoneStoryPoint = listWorksheetStoryPoint(presModel, hasWorksheet=False)
    if len(zoneStoryPoint) != 0:
        return [
            {
                "column": z["presModelHolder"]["parameterControl"]["fieldCaption"],
                "values": z["presModelHolder"]["parameterControl"]["formattedValues"],
                "parameterName": z["presModelHolder"]["parameterControl"]["parameterName"]
            }
            for z in zoneStoryPoint
            if "parameterControl" in z["presModelHolder"]
        ]
    return [
        {
            "column": zones[z]["presModelHolder"]["parameterControl"]["fieldCaption"],
            "values": zones[z]["presModelHolder"]["parameterControl"]["formattedValues"],
            "parameterName": zones[z]["presModelHolder"]["parameterControl"]["parameterName"]
        }
        for z in list(zones)
        if ("presModelHolder" in zones[z])
        and ("parameterControl" in zones[z]["presModelHolder"])
    ]


def listFilters(presModel, worksheetName):
    zones = presModel["workbookPresModel"]["dashboardPresModel"]["zones"]
    filters = [
        json.loads(zones[z]["presModelHolder"]["visual"]["filtersJson"])
        for z in list(zones)
        if zones[z] is not None
        and ("worksheet" in zones[z])
        and ("presModelHolder" in zones[z])
        and ("visual" in zones[z]["presModelHolder"])
        and ("filtersJson" in zones[z]["presModelHolder"]["visual"])
        and zones[z]["worksheet"] == worksheetName
    ]
    if len(filters) != 0:
        entries = []
        for arr in filters:
            result = [
                {
                    "columns": [(z["caption"], z["name"], z["ordinal"]) for z in t["table"]["schema"]],
                    "values": [z["t"][0]["v"] for z in t["table"]["tuples"] if "t" in z and len(z["t"]) != 0]
                }
                for t in arr
                if "table" in t
                and "schema" in t["table"]
                and "tuples" in t["table"]
            ]
            for r in result:
                for c in r["columns"]:
                    entries.append({
                        "column": c[0],
                        "ordinal": c[2],
                        "values": r["values"],
                        "globalFieldName": f"[{c[1][0]}].[{c[1][1]}]"
                    })
        return entries
    return []
