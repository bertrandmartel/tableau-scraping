import pytest

from tests.python.test_common import tableauVizHtmlResponse as tableauVizHtmlResponse
from tests.python.test_common import tableauSessionResponse as tableauSessionResponse
from tests.python.test_common import tableauDataResponse as tableauDataResponse
from tests.python.test_common import vqlCmdResponse as vqlCmdResponse
from tableauscraper import TableauScraper as TS
from pytest_mock import MockerFixture
from tableauscraper import api
import json
from tests.python.test_common import fakeUri as fakeUri
import time
import requests
from tests.python.test_common import tableauDownloadableSummaryData
from tests.python.test_common import tableauDownloadableUnderlyingData
from tests.python.test_common import tableauDownloadableCsvData


def test_getTableauViz(httpserver):
    ts = TS()
    s = requests.Session()
    httpserver.serve_content(tableauVizHtmlResponse)
    result = api.getTableauViz(ts, s, httpserver.url)
    assert result == tableauVizHtmlResponse


def test_getTableauVizForSession(httpserver):
    ts = TS()
    s = requests.Session()
    httpserver.serve_content(tableauVizHtmlResponse)
    result = api.getTableauVizForSession(ts, s, httpserver.url)
    assert result == tableauVizHtmlResponse


def test_getSessionUrl(httpserver):
    ts = TS()
    s = requests.Session()
    httpserver.serve_content(tableauSessionResponse)
    result = api.getSessionUrl(ts, s, httpserver.url)
    assert result == tableauSessionResponse


def test_getTableauData(httpserver, mocker: MockerFixture):
    ts = TS()
    ts.session = requests.Session()
    httpserver.serve_content(tableauDataResponse)
    ts.host = httpserver.url + "/"
    ts.tableauData = {"vizql_root": "", "sessionid": "", "sheetId": ""}
    result = api.getTableauData(ts)
    assert result == tableauDataResponse


def test_select(httpserver, mocker: MockerFixture):
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    ts = TS()
    ts.loads(fakeUri)
    httpserver.serve_content(json.dumps(vqlCmdResponse))
    ts.host = httpserver.url + "/"
    result = api.select(scraper=ts, worksheetName="", selection=[1])
    assert result == vqlCmdResponse


def test_filter(httpserver, mocker: MockerFixture):
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    ts = TS()
    ts.loads(fakeUri)
    httpserver.serve_content(json.dumps(vqlCmdResponse))
    ts.host = httpserver.url + "/"
    result = api.filter(scraper=ts, worksheetName="",
                        globalFieldName="", selection=[1])
    assert result == vqlCmdResponse


def test_gotosheet(httpserver, mocker: MockerFixture):
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    ts = TS()
    ts.loads(fakeUri)
    httpserver.serve_content(json.dumps(vqlCmdResponse))
    ts.host = httpserver.url + "/"
    result = api.goToSheet(scraper=ts, windowId="")
    assert result == vqlCmdResponse


def test_setParameterValue(httpserver, mocker: MockerFixture):
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    ts = TS()
    ts.loads(fakeUri)
    httpserver.serve_content(json.dumps(vqlCmdResponse))
    ts.host = httpserver.url + "/"
    result = api.setParameterValue(scraper=ts, parameterName="", value="test")
    assert result == vqlCmdResponse


def test_getDownloadableData(httpserver, mocker: MockerFixture):
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    ts = TS()
    ts.loads(fakeUri)
    httpserver.serve_content(tableauVizHtmlResponse)
    ts.host = httpserver.url + "/"
    ts.tableauData = {"vizql_root": "", "sessionid": "", "sheetId": ""}
    result = api.getDownloadableData(
        scraper=ts, worksheetName="", dashboardName="", viewId="")
    assert result == tableauVizHtmlResponse


def test_getDownloadableSummaryData(httpserver, mocker: MockerFixture):
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    ts = TS()
    ts.loads(fakeUri)
    httpserver.serve_content(json.dumps(tableauDownloadableSummaryData))
    ts.host = httpserver.url + "/"
    ts.tableauData = {"vizql_root": "", "sessionid": "", "sheetId": ""}
    result = api.getDownloadableSummaryData(
        scraper=ts, worksheetName="", dashboardName="", numRows=200)
    assert result == tableauDownloadableSummaryData


def test_getDownloadableUnderlyingData(httpserver, mocker: MockerFixture):
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    ts = TS()
    ts.loads(fakeUri)
    httpserver.serve_content(json.dumps(tableauDownloadableUnderlyingData))
    ts.host = httpserver.url + "/"
    ts.tableauData = {"vizql_root": "", "sessionid": "", "sheetId": ""}
    result = api.getDownloadableUnderlyingData(
        scraper=ts, worksheetName="", dashboardName="", numRows=200)
    assert result == tableauDownloadableUnderlyingData


def test_getCsvData(httpserver, mocker: MockerFixture):
    mocker.patch(
        "tableauscraper.api.getTableauViz", return_value=tableauVizHtmlResponse
    )
    mocker.patch("tableauscraper.api.getTableauData",
                 return_value=tableauDataResponse)
    ts = TS()
    ts.loads(fakeUri)
    httpserver.serve_content(tableauDownloadableCsvData)
    ts.host = httpserver.url + "/"
    result = api.getCsvData(
        scraper=ts, viewId="")
    assert result == tableauDownloadableCsvData


def test_delayExcution():
    ts = TS()
    ts.lastActionTime = time.time()
    formerValue = time.time()
    api.delayExecution(ts)
    currentTime = time.time()
    assert((currentTime-formerValue) <= 0.6 and (currentTime-formerValue) > 0.5)

    ts.lastActionTime = time.time() - 0.6
    formerValue = time.time()
    api.delayExecution(ts)
    currentTime = time.time()
    assert((currentTime-formerValue) <= 0.3)
