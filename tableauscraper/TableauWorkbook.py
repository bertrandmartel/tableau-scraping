from typing import List
from tableauscraper.TableauWorksheet import TableauWorksheet
import tableauscraper
import copy
import pandas as pd
import io
from pandas.errors import ParserError, EmptyDataError


class TableauWorkbook:

    worksheets: List[TableauWorksheet] = []
    cmdResponse: bool = False
    _originalData = {}
    _originalInfo = {}
    _scraper = None

    def __init__(self, scraper, originalData, originalInfo, data, cmdResponse=False):
        self._scraper = scraper
        self.worksheets = data
        self.cmdResponse = cmdResponse
        self._originalData = originalData
        self._originalInfo = originalInfo

    def updateFullData(self, cmdResponse):
        # update data dictionary if present
        if (("applicationPresModel" in cmdResponse["vqlCmdResponse"]["layoutStatus"]) and
                ("dataDictionary" in cmdResponse["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"])):
            presModel = cmdResponse["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
            if "dataSegments" in presModel["dataDictionary"]:
                dataSegments = presModel["dataDictionary"]["dataSegments"]
                dataSegmentscp = copy.deepcopy(dataSegments)
                keys = list(dataSegmentscp.keys())
                for key in keys:
                    if dataSegmentscp[key] is not None:
                        self._scraper.dataSegments[key] = dataSegmentscp[key]
            else:
                self._scraper.logger.warning(
                    f"no data dictionary present in response")
        else:
            self._scraper.logger.warning(
                f"no data dictionary present in response")
        # update parameters if present
        self._scraper.parameters = self.getParameters()
        if ("applicationPresModel" in cmdResponse["vqlCmdResponse"]["layoutStatus"]):
            presModel = cmdResponse["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
            newParameters = tableauscraper.utils.getParameterControlVqlResponse(
                presModel)
            newParameterscsp = copy.deepcopy(newParameters)
            for newParam in newParameterscsp:
                found = False
                for param in self._scraper.parameters:
                    if newParam["parameterName"] == param["parameterName"]:
                        found = True
                if not found:
                    self._scraper.parameters.append(newParam)
        # update filters if present
        if ("applicationPresModel" in cmdResponse["vqlCmdResponse"]["layoutStatus"]):
            newFilters = tableauscraper.utils.getFiltersForAllWorksheet(
                data=cmdResponse, info=None, rootDashboard=self._scraper.dashboard, cmdResponse=True)
            newFilterscsp = copy.deepcopy(newFilters)
            for worksheet in newFilterscsp:
                if worksheet not in self._scraper.filters:
                    self._scraper.filters[worksheet] = newFilters[worksheet]
                else:
                    for newFilter in newFilters[worksheet]:
                        found = False
                        foundFilterIndex = -1
                        for idx, filter in enumerate(self._scraper.filters[worksheet]):
                            if newFilter["globalFieldName"] == filter["globalFieldName"]:
                                found = True
                                foundFilterIndex = idx
                        if not found:
                            self._scraper.filters[worksheet].append(newFilter)
                        else:
                            del self._scraper.filters[worksheet][foundFilterIndex]
                            self._scraper.filters[worksheet].append(newFilter)

    def getWorksheetNames(self):
        return tableauscraper.utils.getWorksheetNames(self)

    def getWorksheets(self):
        if self.cmdResponse:
            return tableauscraper.dashboard.getWorksheetsCmdResponse(
                self._scraper, self._originalData
            )
        else:
            return tableauscraper.dashboard.getWorksheets(
                self._scraper, self._originalData, self._originalInfo
            )

    def getWorksheet(self, worksheetName) -> TableauWorksheet:
        if self.cmdResponse:
            return tableauscraper.dashboard.getWorksheetCmdResponse(
                self._scraper, self._originalData, worksheetName
            )
        else:
            return tableauscraper.dashboard.getWorksheet(
                self._scraper, self._originalData, self._originalInfo, worksheetName
            )

    def getParameters(self):
        return self._scraper.parameters

    def setParameter(self, inputName, value):
        parameterNames = [
            t["parameterName"]
            for t in self._scraper.parameters
            if t["column"] == inputName
        ]
        if len(parameterNames) == 0:
            self._scraper.logger.error(f"column {inputName} not found")
            return TableauWorkbook(
                scraper=self._scraper,
                originalData=self._originalData,
                originalInfo=self._originalInfo,
                data=list(),
                cmdResponse=self.cmdResponse,
            )

        r = tableauscraper.api.setParameterValue(
            self._scraper, parameterNames[0], value
        )
        self.updateFullData(r)
        return tableauscraper.dashboard.getWorksheetsCmdResponse(self._scraper, r)

    def getSheets(self):
        presModel = tableauscraper.utils.getPresModelVizInfo(
            self._originalInfo)
        return [
            {
                "sheet": t["sheet"],
                "isDashboard": t["isDashboard"],
                "isVisible": t["isVisible"],
                "namesOfSubsheets": t["namesOfSubsheets"],
                "windowId": t["windowId"]
            }
            for t in presModel["workbookPresModel"]["sheetsInfo"]
        ]

    def goToSheet(self, sheetName):
        windowId = [
            t["windowId"]
            for t in self.getSheets()
            if t["sheet"] == sheetName
        ]
        if len(windowId) == 0:
            self._scraper.logger.error(f"sheet {sheetName} not found")
            return TableauWorkbook(
                scraper=self._scraper,
                originalData=self._originalData,
                originalInfo=self._originalInfo,
                data=list(),
                cmdResponse=self.cmdResponse,
            )
        r = tableauscraper.api.goToSheet(self._scraper, windowId[0])
        self.updateFullData(r)
        self._scraper.dashboard = sheetName
        return tableauscraper.dashboard.getWorksheetsCmdResponse(self._scraper, r)

    def getDownloadableData(self, sheetName):
        presModel = tableauscraper.utils.getPresModelVizInfo(
            self._originalInfo)
        if ("workbookPresModel" in presModel) and ("dashboardPresModel" in presModel["workbookPresModel"]) and ("viewIds" in presModel["workbookPresModel"]["dashboardPresModel"]):
            if sheetName in presModel["workbookPresModel"]["dashboardPresModel"]["viewIds"]:
                tableauscraper.api.getDownloadableData(
                    self._scraper, sheetName, self._scraper.dashboard, presModel["workbookPresModel"]["dashboardPresModel"]["viewIds"][sheetName])
            else:
                print(f"{sheetName} not present in viewIds list")
        else:
            print("no viewIds found in json info")

    def getCsvData(self, sheetName, prefix="vudcsv"):
        presModel = tableauscraper.utils.getPresModelVizInfo(
            self._originalInfo)
        if ("workbookPresModel" in presModel) and ("dashboardPresModel" in presModel["workbookPresModel"]) and ("viewIds" in presModel["workbookPresModel"]["dashboardPresModel"]):
            if sheetName in presModel["workbookPresModel"]["dashboardPresModel"]["viewIds"]:
                r = tableauscraper.api.getCsvData(
                    self._scraper, presModel["workbookPresModel"]["dashboardPresModel"]["viewIds"][sheetName], prefix=prefix)
                try:
                    return pd.read_csv(io.StringIO(r))
                except (ParserError, EmptyDataError):
                    return None

            else:
                print(f"{sheetName} not present in viewIds list")
        else:
            print("no viewIds found in json info")
        return None

    def getCrossTabData(self, sheetName):
        r = tableauscraper.api.exportCrosstabServerDialog(self._scraper)

        sheets = [
            t for t in r["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]["presentationLayerNotification"][
                0]["presModelHolder"]["genExportCrosstabOptionsDialogPresModel"]["thumbnailSheetPickerItems"]
            if t["sheetName"] == sheetName
        ]
        if len(sheets) == 0:
            self._scraper.logger.warning(
                f"sheet {sheetName} not found in API result")
            return None

        sheetId = sheets[0]["sheetdocId"]
        r = tableauscraper.api.exportCrosstabToCsvServer(
            self._scraper, sheetId)
        resultKey = r[
            "vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]["presentationLayerNotification"][0]["presModelHolder"]["genExportFilePresModel"]["resultKey"]
        r = tableauscraper.api.downloadCrossTabData(self._scraper, resultKey)
        try:
            return pd.read_csv(io.StringIO(r), sep='\t')
        except (ParserError, EmptyDataError):
            return None

    def getStoryPoints(self):
        return tableauscraper.utils.getStoryPointsFromInfo(self._originalInfo)

    def goToStoryPoint(self, storyPointId) -> "TableauWorkbook":
        storypointResult = self.getStoryPoints()
        r = tableauscraper.api.setActiveStoryPoint(
            self._scraper, storyBoard=storypointResult["storyBoard"], storyPointId=storyPointId)
        self.updateFullData(r)
        return tableauscraper.dashboard.getWorksheetsCmdResponse(self._scraper, r)
