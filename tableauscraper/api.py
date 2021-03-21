import json
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


def getTableauViz(scraper, session, url):
    r = session.get(url, params={
        ":embed": "y",
        ":showVizHome": "no"
    },
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


def select(scraper, worksheetName, selection):
    delayExecution(scraper)
    payload = {
        "worksheet": worksheetName,
        "dashboard": scraper.dashboard,
        "selection": json.dumps({"objectIds": selection, "selectionType": "tuples"}),
        "selectOptions": "select-options-simple",
    }
    r = scraper.session.post(
        f'{scraper.host}{scraper.tableauData["vizql_root"]}/sessions/{scraper.tableauData["sessionid"]}/commands/tabdoc/select',
        data=payload,
        verify=scraper.verify
    )
    return r.json()


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
