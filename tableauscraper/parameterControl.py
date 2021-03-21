import requests
import json
from tableauscraper import utils
from tableauscraper import api
from tableauscraper import dashboard


def get(TS, info, logger):
    parameterControl = utils.getParameterControlInput(info)

    for idx, item in enumerate(parameterControl):
        logger.info(f'[{idx}] {item["column"]}')

    selectedPC = input("select parameter control by index: ")
    if (selectedPC is None) or (selectedPC == ""):
        raise (Exception("you must select at least one parameter control"))
    parameterControl = parameterControl[int(selectedPC)]
    logger.info(f'you selected : {parameterControl["column"]}')

    for idx, item in enumerate(parameterControl["values"]):
        logger.info(f"[{idx}] {item}")
    selectedValue = input("select value by index: ")
    if (selectedValue is None) or (selectedValue == ""):
        raise (Exception("you must select at least one value"))
    value = parameterControl["values"][int(selectedValue)]
    logger.info(f"you selected : {value}")

    r = api.setParameterValue(TS, parameterControl["parameterName"], value)

    return dashboard.getCmdResponse(TS, r, logger)
