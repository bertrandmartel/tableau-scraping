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
    dataFull = utils.getDataFull(presModelMap)
    frameData = utils.getData(dataFull, indicesInfo)

    df = pd.DataFrame.from_dict(frameData, orient="index").fillna(0).T

    return TableauWorksheet(
        scraper=TS,
        originalData=data,
        originalInfo=info,
        worksheetName=worksheet,
        dataFrame=df,
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
    dataFull = utils.getDataFullCmdResponse(presModel)
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
                cmdResponse=True,
            )
        )
    return TableauDashboard(scraper=TS, originalData=data, originalInfo={}, data=output, cmdResponse=True)


def getWorksheetsCmdResponse(TS, data):
    presModel = data["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
    zonesWithWorksheet = utils.listWorksheetCmdResponse(presModel)
    dataFull = utils.getDataFullCmdResponse(presModel)
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
            cmdResponse=True,
        )

    selectedZone = zonesWithWorksheet[0]

    dataFull = utils.getDataFullCmdResponse(presModel)
    frameData = utils.getWorksheetCmdResponse(selectedZone, dataFull)

    if frameData is None:
        return TableauWorksheet(
            scraper=TS,
            originalData=data,
            originalInfo={},
            worksheetName=worksheetName,
            dataFrame=pd.DataFrame(),
            cmdResponse=True,
        )

    df = pd.DataFrame.from_dict(frameData, orient="index").fillna(0).T

    return TableauWorksheet(
        scraper=TS,
        originalData=data,
        originalInfo={},
        worksheetName=selectedZone["worksheet"],
        dataFrame=df,
        cmdResponse=True,
    )
