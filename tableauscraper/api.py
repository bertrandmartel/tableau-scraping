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
            "clientDimension": json.dumps({"w": 1920, "h": 1080})
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
    scraper.lastActionTime = time.time()
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
    scraper.lastActionTime = time.time()
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
    scraper.lastActionTime = time.time()
    try:
        return r.json()
    except (ValueError, JSONDecodeError):
        raise APIResponseException(message=r.text)


def filter(scraper, worksheetName, globalFieldName, dashboard, selection=[], selectionToRemove=[], membershipTarget=True, filterDelta=False, storyboard=None, storyboardId=None):
    delayExecution(scraper)
    visualIdPresModel = {
        "worksheet": worksheetName,
        "dashboard": dashboard
    }
    if storyboard is not None:
        visualIdPresModel["storyboard"] = storyboard
    if storyboardId is not None:
        visualIdPresModel["storyPointId"] = storyboardId
    payload = (
        (
            "visualIdPresModel", (None, json.dumps(visualIdPresModel))
        ),
        ("globalFieldName", (None, globalFieldName)),
        ("filterUpdateType", (None, "filter-replace" if not filterDelta else "filter-delta"))
    )
    if membershipTarget:
        payload = (("membershipTarget", (None, "filter")),) + payload
    if filterDelta:
        payload = (("filterAddIndices", (None, json.dumps(selection))),) + \
            (("filterRemoveIndices", (None, json.dumps(selectionToRemove))),) + payload
    else:
        payload = (("filterIndices", (None, json.dumps(selection))),) + payload
    r = scraper.session.post(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/sessions/{scraper.tableauData["sessionid"]}/commands/tabdoc/categorical-filter-by-index',
        files=payload,
        verify=scraper.verify
    )
    scraper.lastActionTime = time.time()
    try:
        return r.json()
    except ValueError:
        raise APIResponseException(message=r.text)


def dashboardFilter(scraper, columnName, selection):
    delayExecution(scraper)
    payload = (
        ("dashboard", (None, scraper.dashboard)),
        ("qualifiedFieldCaption", (None, columnName)),
        ("exclude", (None, "false")),
        ("filterUpdateType", (None, "filter-replace")),
        ("filterValues", (None, json.dumps(selection,
                                           ensure_ascii=False)))
    )

    r = scraper.session.post(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/sessions/{scraper.tableauData["sessionid"]}/commands/tabdoc/dashboard-categorical-filter',
        files=payload,
        verify=scraper.verify
    )
    scraper.lastActionTime = time.time()
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
    scraper.lastActionTime = time.time()
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
    scraper.lastActionTime = time.time()
    return r.json()


def exportCrosstabServerDialog(scraper):
    delayExecution(scraper)
    payload = (
        ("thumbnailUris", (None, json.dumps({}))),
    )
    r = scraper.session.post(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/sessions/{scraper.tableauData["sessionid"]}/commands/tabsrv/export-crosstab-server-dialog',
        files=payload,
        verify=scraper.verify
    )
    scraper.lastActionTime = time.time()
    return r.json()


def exportCrosstabToCsvServer(scraper, sheetId):
    delayExecution(scraper)
    payload = (
        ("sheetdocId", (None, sheetId)),
        ("useTabs", (None, "true")),
        ("sendNotifications", (None, "true")),
    )
    r = scraper.session.post(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/sessions/{scraper.tableauData["sessionid"]}/commands/tabsrv/export-crosstab-to-csvserver',
        files=payload,
        verify=scraper.verify
    )
    scraper.lastActionTime = time.time()
    return r.json()


def downloadCrossTabData(scraper, resultKey):
    r = scraper.session.get(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/tempfile/sessions/{scraper.tableauData["sessionid"]}/',
        params={
            "key": resultKey,
            "keepfile": "yes",
            "attachment": "yes"
        },
        verify=scraper.verify)
    scraper.lastActionTime = time.time()
    return r.content.decode('utf-16')


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
    scraper.lastActionTime = time.time()
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
    scraper.lastActionTime = time.time()
    return r.json()


def renderTooltipServer(scraper, worksheetName, x, y):
    delayExecution(scraper)
    payload = (
        ("worksheet", (None, worksheetName)),
        ("dashboard", (None, scraper.dashboard)),
        ("vizRegionRect", (None, json.dumps({
            "r": "viz",
            "x": x,
            "y": y,
            "w": 0,
            "h": 0,
            "fieldVector": None
        }))),
        ("allowHoverActions", (None, "true")),
        ("allowPromptText", (None, "true")),
        ("allowWork", (None, "false")),
        ("useInlineImages", (None, "true")),
    )
    r = scraper.session.post(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/sessions/{scraper.tableauData["sessionid"]}/commands/tabsrv/render-tooltip-server',
        files=payload,
        verify=scraper.verify
    )
    scraper.lastActionTime = time.time()
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
