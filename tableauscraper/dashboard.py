import pandas as pd
from tableauscraper import utils
from tableauscraper.TableauWorksheet import TableauWorksheet
from tableauscraper.TableauDashboard import TableauDashboard


def get(TS, data, info, logger):
    output = []
    worksheets = utils.selectWorksheet(data, logger)

    for worksheet in worksheets:
        df = getWorksheet(TS, data, info, worksheet)
        output.append(df)

    return TableauDashboard(
        scraper=TS, originalData=data, originalInfo=info, data=output
    )


def getWorksheet(TS, data, info, worksheet) -> TableauWorksheet:

    presModelMap = data["secondaryInfo"]["presModelMap"]

    indicesInfo = utils.getIndicesInfo(presModelMap, worksheet)
    dataFull = utils.getDataFull(presModelMap, TS.dataSegments)
    frameData = utils.getData(dataFull, indicesInfo)

    df = pd.DataFrame.from_dict(frameData, orient="index").fillna(0).T

    presModel = utils.getPresModelVizData(data)
    return TableauWorksheet(
        scraper=TS,
        originalData=data,
        originalInfo=info,
        worksheetName=worksheet,
        dataFull=utils.getDataFull(presModel, TS.dataSegments),
        dataFrame=df
    )


def getWorksheets(TS, data, info) -> TableauDashboard:

    presModelMapVizData = utils.getPresModelVizData(data)
    presModelMapVizInfo = utils.getPresModelVizInfo(info)
    if presModelMapVizData is not None:
        worksheets = utils.listWorksheet(presModelMapVizData)
    elif presModelMapVizInfo is not None:
        worksheets = utils.listWorksheetInfo(presModelMapVizInfo)
    else:
        worksheets = []

    # if presModelMapVizData is not None:
    #     storyPoints = utils.listStoryPoints(presModelMapVizData)
    # elif presModelMapVizInfo is not None:
    #     storyPoints = utils.listStoryPointsInfo(presModelMapVizInfo)
    # else:
    #     storyPoints = []
    # print(storyPoints)

    output = []
    for worksheet in worksheets:
        df = getWorksheet(TS, data, info, worksheet)
        output.append(df)

    return TableauDashboard(
        scraper=TS, originalData=data, originalInfo=info, data=output
    )


def getCmdResponse(TS, data, logger):
    presModel = data["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]

    zonesWithWorksheet = utils.selectWorksheetCmdResponse(presModel, logger)
    dataFull = utils.getDataFullCmdResponse(presModel, TS.dataSegments)
    output = []
    for selectedZone in zonesWithWorksheet:
        frameData = utils.getWorksheetCmdResponse(selectedZone, dataFull)

        if frameData is None:
            continue

        df = pd.DataFrame.from_dict(frameData, orient="index").fillna(0).T

        output.append(
            TableauWorksheet(
                scraper=TS,
                originalData=data,
                originalInfo={},
                worksheetName=selectedZone["worksheet"],
                dataFrame=df,
                dataFull=utils.getDataFullCmdResponse(
                    presModel, TS.dataSegments),
                cmdResponse=True,
            )
        )
    return TableauDashboard(scraper=TS, originalData=data, originalInfo={}, data=output, cmdResponse=True)


def getWorksheetsCmdResponse(TS, data):
    presModel = data["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
    zonesWithWorksheet = utils.listWorksheetCmdResponse(presModel)
    dataFull = utils.getDataFullCmdResponse(presModel, TS.dataSegments)
    output = []
    for selectedZone in zonesWithWorksheet:
        frameData = utils.getWorksheetCmdResponse(selectedZone, dataFull)

        if frameData is None:
            continue

        df = pd.DataFrame.from_dict(frameData, orient="index").fillna(0).T

        output.append(
            TableauWorksheet(
                scraper=TS,
                originalData=data,
                originalInfo={},
                worksheetName=selectedZone["worksheet"],
                dataFrame=df,
                dataFull=utils.getDataFullCmdResponse(
                    presModel, TS.dataSegments),
                cmdResponse=True,
            )
        )
    return TableauDashboard(
        scraper=TS, originalData=data, originalInfo={}, data=output, cmdResponse=True
    )


def getWorksheetCmdResponse(TS, data, worksheetName):
    presModel = data["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
    zonesWithWorksheet = [
        t
        for t in utils.listWorksheetCmdResponse(presModel)
        if t["worksheet"] == worksheetName
    ]
    if len(zonesWithWorksheet) == 0:
        return TableauWorksheet(
            scraper=TS,
            originalData=data,
            originalInfo={},
            worksheetName=worksheetName,
            dataFrame=pd.DataFrame(),
            dataFull=utils.getDataFullCmdResponse(
                presModel, TS.dataSegments),
            cmdResponse=True,
        )

    selectedZone = zonesWithWorksheet[0]

    dataFull = utils.getDataFullCmdResponse(presModel, TS.dataSegments)
    frameData = utils.getWorksheetCmdResponse(selectedZone, dataFull)

    if frameData is None:
        return TableauWorksheet(
            scraper=TS,
            originalData=data,
            originalInfo={},
            worksheetName=worksheetName,
            dataFrame=pd.DataFrame(),
            dataFull=utils.getDataFullCmdResponse(
                presModel, TS.dataSegments),
            cmdResponse=True,
        )

    df = pd.DataFrame.from_dict(frameData, orient="index").fillna(0).T

    return TableauWorksheet(
        scraper=TS,
        originalData=data,
        originalInfo={},
        worksheetName=selectedZone["worksheet"],
        dataFrame=df,
        dataFull=utils.getDataFullCmdResponse(
            presModel, TS.dataSegments),
        cmdResponse=True,
    )
