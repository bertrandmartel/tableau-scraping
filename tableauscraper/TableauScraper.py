from urllib.parse import urlparse, unquote
from bs4 import BeautifulSoup
import json
import re
from tableauscraper import dashboard
from tableauscraper import parameterControl
from tableauscraper import selectItem
from tableauscraper import utils
from tableauscraper import api
from tableauscraper.TableauWorksheet import TableauWorksheet
from tableauscraper.TableauWorkbook import TableauWorkbook
from typing import List
import logging


class TableauException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class TableauScraper:

    host: str = ""
    info = {}
    data = {}
    dashboard: str = ""
    tableauData = {}
    dataSegments = {}
    logger = logging.getLogger("tableauScraper")
    delayMs = 500  # delay between actions (select/dropdown)
    lastActionTime = 0
    session = None
    verify = True

    def __init__(self, logLevel=logging.INFO, delayMs=500, verify=True):
        ch = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.setLevel(logLevel)
        self.delayMs = delayMs
        self.tableauData = {}
        self.data = {}
        self.info = {}
        self.verify = verify

    def loads(self, url, params={}):
        api.setSession(self)
        r = api.getTableauViz(self, self.session, url, params)
        soup = BeautifulSoup(r, "html.parser")

        tableauPlaceHolder = soup.find("div", {"class": "tableauPlaceholder"})

        if tableauPlaceHolder is not None:
            params = dict([
                (t.get("name", ""), unquote(t.get("value", "")))
                for t in tableauPlaceHolder.findAll("param")
            ])
            if ("host_url" not in params) or ("site_root" not in params) or ("name" not in params):
                self.logger.info("no params found in placeholder")
                return

            if "ticket" in params:
                # get xsrf cookie
                sessionUrl = f'{params["host_url"]}trusted/{params["ticket"]}{params["site_root"]}/views/{params["name"]}'
                api.getSessionUrl(self, self.session, sessionUrl)

            url = f'{params["host_url"][:-1]}{params["site_root"]}/views/{params["name"]}'
            r = api.getTableauVizForSession(self, self.session, url)
            soup = BeautifulSoup(r, "html.parser")

        self.tableauData = json.loads(
            soup.find("textarea", {"id": "tsConfigContainer"}).text
        )

        uri = urlparse(url)
        self.host = "{uri.scheme}://{uri.netloc}".format(uri=uri)

        r = api.getTableauData(self)

        try:
            dataReg = re.search(r"\d+;({.*})\d+;({.*})", r, re.MULTILINE)
            self.info = json.loads(dataReg.group(1))
            self.data = json.loads(dataReg.group(2))

            if "presModelMap" in self.data["secondaryInfo"]:
                presModelMap = self.data["secondaryInfo"]["presModelMap"]
                self.dataSegments = presModelMap["dataDictionary"][
                    "presModelHolder"]["genDataDictionaryPresModel"]["dataSegments"]
            self.dashboard = self.info["sheetName"]
        except (AttributeError):
            raise TableauException(message=r)

    def getWorkbook(self) -> TableauWorkbook:
        return dashboard.getWorksheets(self, self.data, self.info)

    def getWorksheet(self, worksheetName) -> TableauWorksheet:
        return dashboard.getWorksheet(self, self.data, self.info, worksheetName)

    def promptDashboard(self):
        return dashboard.get(self, self.data, self.info, self.logger)

    def promptParameters(self):
        return parameterControl.get(self, self.info, self.logger)

    def promptSelect(self):
        return selectItem.get(self, self.data, self.info, self.logger)
