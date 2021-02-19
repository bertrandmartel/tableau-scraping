from tableauscraper import utils
from tableauscraper import api
import json
import requests
from tableauscraper import dashboard
from tableauscraper.TableauDashboard import TableauDashboard


def get(TS, data, info, logger):
    worksheets = utils.selectWorksheet(data, logger, single=True)
    if len(worksheets) == 0:
        return TableauDashboard(
            scraper=TS, originalData=data, originalInfo=info, data=[]
        )
    selectedWorksheet = worksheets[0]

    presModel = utils.getPresModelVizData(data)
    result = utils.getIndicesInfo(presModel, selectedWorksheet, noSelectFilter=False)

    for idx, t in enumerate(result):
        logger.info(f"[{idx}] {t['fieldCaption']}")

    selected = input(f"select field by index : ")

    if (selected is None) or (selected == ""):
        raise (Exception("you must select at least one field"))
    field = result[int(selected)]
    logger.info(f"you have selected {field['fieldCaption']}")

    dataFull = utils.getDataFull(presModel)
    frameData = utils.getData(dataFull, [field])
    frameDataKeys = list(frameData.keys())

    if len(frameDataKeys) == 0:
        raise (Exception("no data extracted"))

    data = frameData[frameDataKeys[0]]
    for idx, t in enumerate(data):
        logger.info(f"[{idx}] {t}")

    selected = input(f"select value by index : ")
    if (selected is None) or (selected == ""):
        raise (Exception("you must select at least one value"))
    value = data[int(selected)]
    logger.info(f"you have selected {value}")

    r = api.select(TS, selectedWorksheet, [int(selected) + 1])
    return dashboard.getCmdResponse(TS, r, logger)
