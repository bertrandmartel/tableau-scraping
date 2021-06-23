import json
from json.decoder import JSONDecodeError
import time
import requests


class APIResponseException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def setSession(scraper):
    scraper.session = requests.Session()


def getTableauVizForSession(scraper, session, url):
    r = session.get(url, params={
        ":embed": "y",
        ":showVizHome": "no"},
        verify=scraper.verify
    )
    return r.text


def getTableauViz(scraper, session, url, params={}):
    if not params:
        params = {
            ":embed": "y",
            ":showVizHome": "no"
        }
    r = session.get(url, params=params,
                    verify=scraper.verify
                    )
    return r.text


def getSessionUrl(scraper, session, url):
    r = session.get(url, verify=scraper.verify)
    return r.text


def getTableauData(scraper):
    dataUrl = f'{scraper.host}{scraper.tableauData["vizql_root"]}/bootstrapSession/sessions/{scraper.tableauData["sessionid"]}'
    r = scraper.session.post(
        dataUrl,
        data={
            "sheet_id": scraper.tableauData["sheetId"],
        },
        verify=scraper.verify
    )
    scraper.lastActionTime = time.time()
    return r.text


def getCsvData(scraper, viewId, prefix="vudcsv"):
    dataUrl = f'{scraper.host}{scraper.tableauData["vizql_root"]}/{prefix}/sessions/{scraper.tableauData["sessionid"]}/views/{viewId}'
    r = scraper.session.get(
        dataUrl,
        params={
            "csv": "true",
            "showall": "true"
        },
        verify=scraper.verify)
    scraper.lastActionTime = time.time()
    return r.content.decode('utf-8')


def getDownloadableData(scraper, worksheetName, dashboardName, viewId):
    input = json.dumps({
        "worksheet": worksheetName,
        "dashboard": dashboardName
    })
    dataUrl = f'{scraper.host}{scraper.tableauData["vizql_root"]}/viewData/sessions/{scraper.tableauData["sessionid"]}/views/{viewId}'
    r = scraper.session.get(
        dataUrl,
        params={
            "maxrows": "200",
            "viz": input
        },
        verify=scraper.verify)
    scraper.lastActionTime = time.time()
    return r.text


def getDownloadableSummaryData(scraper, worksheetName, dashboardName, numRows=200):
    delayExecution(scraper)
    payload = (
        ("maxRows", (None, numRows)),
        ("visualIdPresModel", (None, json.dumps(
            {"worksheet": worksheetName, "dashboard": dashboardName, "flipboardZoneId": 0, "storyPointId": 0}))
         ),
    )
    r = scraper.session.post(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/sessions/{scraper.tableauData["sessionid"]}/commands/tabdoc/get-summary-data',
        files=payload,
        verify=scraper.verify
    )
    return r.json()


def getDownloadableUnderlyingData(scraper, worksheetName, dashboardName, numRows=200):
    delayExecution(scraper)
    payload = (
        ("maxRows", (None, numRows)),
        ("includeAllColumns", (None, "true")),
        ("visualIdPresModel", (None, json.dumps(
            {"worksheet": worksheetName, "dashboard": dashboardName, "flipboardZoneId": 0, "storyPointId": 0}))
         ),
    )
    r = scraper.session.post(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/sessions/{scraper.tableauData["sessionid"]}/commands/tabdoc/get-underlying-data',
        files=payload,
        verify=scraper.verify
    )
    try:
        return r.json()
    except ValueError:
        raise APIResponseException(message=r.text)


def select(scraper, worksheetName, selection):
    delayExecution(scraper)
    payload = (
        ("worksheet", (None, worksheetName)),
        ("dashboard", (None, scraper.dashboard)),
        ("selection", (None, json.dumps(
            {"objectIds": selection, "selectionType": "tuples"}))),
        ("selectOptions", (None, "select-options-simple")),
    )
    r = scraper.session.post(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/sessions/{scraper.tableauData["sessionid"]}/commands/tabdoc/select',
        files=payload,
        verify=scraper.verify
    )
    try:
        return r.json()
    except (ValueError, JSONDecodeError):
        raise APIResponseException(message=r.text)


def filter(scraper, worksheetName, globalFieldName, selection):
    delayExecution(scraper)
    payload = (
        (
            "visualIdPresModel", (None, json.dumps({
                "worksheet": worksheetName,
                "dashboard": scraper.dashboard
            }))
        ),
        ("globalFieldName", (None, globalFieldName)),
        ("membershipTarget", (None, "filter")),
        ("filterIndices", (None, json.dumps(selection))),
        ("filterUpdateType", (None, "filter-replace"))
    )
    r = scraper.session.post(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/sessions/{scraper.tableauData["sessionid"]}/commands/tabdoc/categorical-filter-by-index',
        files=payload,
        verify=scraper.verify
    )
    try:
        return r.json()
    except ValueError:
        raise APIResponseException(message=r.text)


def setParameterValue(scraper, parameterName, value):
    delayExecution(scraper)
    payload = (
        ("globalFieldName", (None, parameterName)),
        ("valueString", (None, value)),
        ("useUsLocale", (None, "false")),
    )
    r = scraper.session.post(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/sessions/{scraper.tableauData["sessionid"]}/commands/tabdoc/set-parameter-value',
        files=payload,
        verify=scraper.verify
    )
    return r.json()


def goToSheet(scraper, windowId):
    delayExecution(scraper)
    payload = (
        ("windowId", (None, windowId)),
    )
    r = scraper.session.post(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/sessions/{scraper.tableauData["sessionid"]}/commands/tabdoc/goto-sheet',
        files=payload,
        verify=scraper.verify
    )
    return r.json()


def setActiveStoryPoint(scraper, storyBoard, storyPointId):
    delayExecution(scraper)
    payload = (
        ("storyboard", (None, storyBoard)),
        ("storyPointId", (None, storyPointId)),
        ("shouldAutoCapture", (None, "false")),
        ("shouldAutoRevert", (None, "true")),
    )
    r = scraper.session.post(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/sessions/{scraper.tableauData["sessionid"]}/commands/tabdoc/set-active-story-point',
        files=payload,
        verify=scraper.verify
    )
    return r.json()


def levelDrill(scraper, worksheetName, drillDown, position=0):
    delayExecution(scraper)
    payload = (
        ("worksheet", (None, worksheetName)),
        ("dashboard", (None, scraper.dashboard)),
        ("boolAggregateDrillUp", (None, "true" if drillDown else "false")),
        ("shelfType", (None, "columns-shelf")),
        ("position", (None, position)),
    )
    r = scraper.session.post(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/sessions/{scraper.tableauData["sessionid"]}/commands/tabdoc/level-drill-up-down',
        files=payload,
        verify=scraper.verify
    )
    return r.json()


def delayExecution(scraper):
    if scraper.lastActionTime != 0:
        currentTime = time.time()
        timeDif = currentTime - scraper.lastActionTime
        if timeDif < (scraper.delayMs / 1000):
            waitTime = timeDif + (scraper.delayMs / 1000)
            scraper.logger.debug(f"delaying request by {waitTime} seconds")
            time.sleep(waitTime)
            scraper.lastActionTime = currentTime
        else:
            scraper.lastActionTime = currentTime
