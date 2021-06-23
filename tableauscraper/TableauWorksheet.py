import pandas as pd
import tableauscraper
from typing import List
from tableauscraper import utils
import copy


class TableauWorksheet:

    name: str = ""
    data: pd.DataFrame = pd.DataFrame()
    cmdResponse: bool = False

    _originalData = {}
    _originalInfo = {}
    _data_dictionnary = {}
    _scraper = None

    def __init__(
        self,
        scraper,
        originalData,
        originalInfo,
        worksheetName,
        dataFrame,
        dataFull,
        cmdResponse=False,
    ):
        self._scraper = scraper
        self.name = worksheetName
        self.data = dataFrame
        self._originalData = originalData
        self._originalInfo = originalInfo
        self.cmdResponse = cmdResponse
        self._data_dictionnary = dataFull

    def updateFullData(self, cmdResponse):
        if (("applicationPresModel" in cmdResponse["vqlCmdResponse"]["layoutStatus"]) and
                ("dataDictionary" in cmdResponse["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"])):
            presModel = cmdResponse["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
            dataSegments = presModel["dataDictionary"]["dataSegments"]
            dataSegmentscp = copy.deepcopy(dataSegments)
            keys = list(dataSegmentscp.keys())
            for key in keys:
                if dataSegmentscp[key] is not None:
                    self._scraper.dataSegments[key] = dataSegmentscp[key]
        elif (("cmdResultList" in cmdResponse["vqlCmdResponse"]) and
              (len(cmdResponse["vqlCmdResponse"]["cmdResultList"]) > 0) and
              ("commandReturn" in cmdResponse["vqlCmdResponse"]["cmdResultList"][0]) and
              ("underlyingDataTable" in cmdResponse["vqlCmdResponse"]["cmdResultList"][0]["commandReturn"]) and
                ("dataDictionary" in cmdResponse["vqlCmdResponse"]["cmdResultList"][0]["commandReturn"]["underlyingDataTable"])):
            dataSegments = cmdResponse["vqlCmdResponse"]["cmdResultList"][
                0]["commandReturn"]["underlyingDataTable"]["dataDictionary"]["dataSegments"]
            dataSegmentscp = copy.deepcopy(dataSegments)
            keys = list(dataSegmentscp.keys())
            for key in keys:
                if dataSegmentscp[key] is not None:
                    self._scraper.dataSegments[key] = dataSegmentscp[key]
        else:
            self._scraper.logger.warning(
                f"no data dictionary present in response")

    def getColumns(self) -> List[str]:
        if self.cmdResponse:
            presModel = self._originalData["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
            return [
                t["fieldCaption"]
                for t in tableauscraper.utils.getIndicesInfoVqlResponse(
                    presModel, self.name, noSelectFilter=True
                )
            ]
        else:
            presModel = tableauscraper.utils.getPresModelVizData(
                self._originalData)
            return [
                t["fieldCaption"]
                for t in tableauscraper.utils.getIndicesInfo(
                    presModel, self.name, noSelectFilter=True
                )
            ]

    def getFilters(self) -> List[str]:
        if self.cmdResponse:
            presModel = self._originalData["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
        else:
            presModel = tableauscraper.utils.getPresModelVizInfo(
                self._originalInfo)
        return tableauscraper.utils.listFilters(presModel, self.name)

    def setFilter(self, columnName, value):
        try:
            filter = [
                {
                    "globalFieldName": t["globalFieldName"],
                    "index": t["values"].index(value) + t["ordinal"]
                }
                for t in self.getFilters()
                if t["column"] == columnName
            ]
            if len(filter) == 0:
                self._scraper.logger.error(f"column {columnName} not found")
                return tableauscraper.TableauWorkbook(
                    scraper=self._scraper, originalData={}, originalInfo={}, data=[]
                )
            r = tableauscraper.api.filter(
                self._scraper, self.name, filter[0]["globalFieldName"], [filter[0]["index"]])
            self.updateFullData(r)
            return tableauscraper.dashboard.getWorksheetsCmdResponse(self._scraper, r)
        except ValueError as e:
            self._scraper.logger.error(str(e))
            return tableauscraper.TableauWorkbook(
                scraper=self._scraper, originalData={}, originalInfo={}, data=[]
            )
        except tableauscraper.api.APIResponseException as e:
            self._scraper.logger.error(str(e))
            return tableauscraper.TableauWorkbook(
                scraper=self._scraper, originalData={}, originalInfo={}, data=[]
            )

    def getSelectableItems(self) -> List[str]:
        if self.cmdResponse:
            presModel = self._originalData["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
            return [
                {
                    "column": t["fieldCaption"],
                    "values": next(iter([y for y in tableauscraper.utils.getData(self._data_dictionnary, [t]).values()]), [])
                }
                for t in tableauscraper.utils.getIndicesInfoVqlResponse(presModel, self.name, noSelectFilter=True)
            ]
        else:
            presModel = tableauscraper.utils.getPresModelVizData(
                self._originalData)
            if presModel is None:
                presModel = tableauscraper.utils.getPresModelVizInfo(
                    self._originalInfo)
                indicesInfo = tableauscraper.utils.getIndicesInfoStoryPoint(
                    presModel, self.name, noSelectFilter=True)
            else:
                indicesInfo = tableauscraper.utils.getIndicesInfo(
                    presModel, self.name, noSelectFilter=True)
            return [
                {
                    "column": t["fieldCaption"],
                    "values": next(iter([
                        y
                        for y in tableauscraper.utils.getData(self._data_dictionnary, [t]).values()
                    ]), [])
                }
                for t in indicesInfo
            ]

    def getSelectableValues(self, column) -> List[str]:
        if self.cmdResponse:
            presModel = self._originalData["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
            columnObj = [
                t
                for t in tableauscraper.utils.getIndicesInfoVqlResponse(
                    presModel, self.name, noSelectFilter=True
                )
                if t["fieldCaption"] == column
            ]
            if len(columnObj) == 0:
                return []
            frameData = tableauscraper.utils.getData(
                self._data_dictionnary, [columnObj[0]]
            )
            frameDataKeys = list(frameData.keys())

            if len(frameDataKeys) == 0:
                return []
            return frameData[frameDataKeys[0]]
        else:
            presModel = tableauscraper.utils.getPresModelVizData(
                self._originalData)
            if presModel is None:
                presModel = tableauscraper.utils.getPresModelVizInfo(
                    self._originalInfo)
                indicesInfo = tableauscraper.utils.getIndicesInfoStoryPoint(
                    presModel, self.name, noSelectFilter=True)
            else:
                indicesInfo = tableauscraper.utils.getIndicesInfo(
                    presModel, self.name, noSelectFilter=True)

            columnObj = [
                t
                for t in indicesInfo
                if t["fieldCaption"] == column
            ]
            if len(columnObj) == 0:
                return []
            frameData = tableauscraper.utils.getData(
                self._data_dictionnary, [columnObj[0]]
            )
            frameDataKeys = list(frameData.keys())

            if len(frameDataKeys) == 0:
                return []
            return frameData[frameDataKeys[0]]

    def getTupleIds(self) -> List[int]:
        if self.cmdResponse:
            presModel = self._originalData["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
            columnObj = [
                t
                for t in tableauscraper.utils.getIndicesInfoVqlResponse(
                    presModel, self.name, noSelectFilter=True, noFieldCaption=True
                )
                if t["fn"] == "[system:visual].[tuple_id]"
            ]
            if len(columnObj) == 0:
                return []

            return [t["tupleIds"] for t in columnObj]
        else:
            presModel = tableauscraper.utils.getPresModelVizData(
                self._originalData)
            columnObj = [
                t
                for t in tableauscraper.utils.getIndicesInfo(
                    presModel, self.name, noSelectFilter=True, noFieldCaption=True
                )
                if t["fn"] == "[system:visual].[tuple_id]"
            ]
            if len(columnObj) == 0:
                return []
            return [t["tupleIds"] for t in columnObj]

    def select(self, column, value):
        values = self.getSelectableValues(column)
        tupleItems = self.getTupleIds()
        try:

            indexedByTuple = False
            for tupleItem in tupleItems:
                if len(tupleItem) >= len(values):
                    index = values.index(value)
                    index = tupleItem[index]
                    indexedByTuple = True
                    break
            if not indexedByTuple:
                index = values.index(value)
                index = index + 1
            r = tableauscraper.api.select(self._scraper, self.name, [index])
            self.updateFullData(r)
            return tableauscraper.dashboard.getWorksheetsCmdResponse(self._scraper, r)
        except ValueError as e:
            self._scraper.logger.error(str(e))
            return tableauscraper.TableauWorkbook(
                scraper=self._scraper, originalData={}, originalInfo={}, data=[]
            )

    def getDownloadableSummaryData(self, numRows=200):
        r = tableauscraper.api.getDownloadableSummaryData(
            self._scraper, self.name, self._scraper.dashboard, numRows)
        self.updateFullData(r)
        return tableauscraper.dashboard.getWorksheetDownloadCmdResponse(self._scraper, r)

    def getDownloadableUnderlyingData(self, numRows=200):
        r = tableauscraper.api.getDownloadableUnderlyingData(
            self._scraper, self.name, self._scraper.dashboard, numRows)
        self.updateFullData(r)
        return tableauscraper.dashboard.getWorksheetDownloadCmdResponse(self._scraper, r)

    def levelDrill(self, drillDown, position=0):
        r = tableauscraper.api.levelDrill(
            self._scraper, self.name, drillDown, position)
        self.updateFullData(r)
        return tableauscraper.dashboard.getWorksheetsCmdResponse(self._scraper, r)
