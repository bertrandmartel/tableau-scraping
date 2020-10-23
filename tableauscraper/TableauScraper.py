from urllib.parse import urlparse
from bs4 import BeautifulSoup
import json
import re
from tableauscraper import dashboard
from tableauscraper import parameterControl
from tableauscraper import selectItem
from tableauscraper import utils
from tableauscraper import api
from tableauscraper.TableauWorksheet import TableauWorksheet
from tableauscraper.TableauDashboard import TableauDashboard
from typing import List
import logging


class TableauScraper:

    host: str = ""
    info = {}
    data = {}
    dashboard: str = ""
    tableauData = {}
    logger = logging.getLogger("tableauScraper")
    delayMs = 500  # delay between actions (select/dropdown)
    lastActionTime = 0

    def __init__(self, logLevel=logging.INFO, delayMs=500):
        ch = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
        self.logger.setLevel(logLevel)
        self.delayMs = delayMs

    def loads(self, url):
        r = api.getTableauViz(url)
        soup = BeautifulSoup(r, "html.parser")

        self.tableauData = json.loads(
            soup.find("textarea", {"id": "tsConfigContainer"}).text
        )

        uri = urlparse(url)
        self.host = "{uri.scheme}://{uri.netloc}/".format(uri=uri)

        r = api.getTableauData(self)

        dataReg = re.search(r"\d+;({.*})\d+;({.*})", r, re.MULTILINE)
        self.info = json.loads(dataReg.group(1))
        self.data = json.loads(dataReg.group(2))
        self.dashboard = self.info["sheetName"]

    def listWorksheetNames(self):
        return utils.listWorksheet(self.data)

    def getDashboard(self) -> TableauDashboard:
        return dashboard.getWorksheets(self, self.data, self.info)

    def getWorksheet(self, worksheetName) -> TableauWorksheet:
        return dashboard.getWorksheet(self, self.data, self.info, worksheetName)

    def promptDashboard(self):
        return dashboard.get(self, self.data, self.info, self.logger)

    def promptDropdown(self):
        return parameterControl.get(self, self.info, self.logger)

    def promptSelect(self):
        return selectItem.get(self, self.data, self.info, self.logger)
