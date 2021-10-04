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
        elif (("cmdResultList" in cmdResponse["vqlCmdResponse"]) and
              (len(cmdResponse["vqlCmdResponse"]["cmdResultList"]) > 0) and
              ("commandReturn" in cmdResponse["vqlCmdResponse"]["cmdResultList"][0]) and
              ("underlyingDataTable" in cmdResponse["vqlCmdResponse"]["cmdResultList"][0]["commandReturn"]) and
                ("dataDictionary" in cmdResponse["vqlCmdResponse"]["cmdResultList"][0]["commandReturn"]["underlyingDataTable"]) and
                ("dataSegments" in cmdResponse["vqlCmdResponse"]["cmdResultList"][0]["commandReturn"]["underlyingDataTable"]["dataDictionary"])):
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
            selectedFilters = tableauscraper.utils.getSelectedFilters(
                presModel,
                self.name
            )
        else:
            presModel = tableauscraper.utils.getPresModelVizInfo(
                self._originalInfo)
            selectedFilters = tableauscraper.utils.getSelectedFilters(
                tableauscraper.utils.getPresModelVizInfo(self._originalInfo),
                self.name
            )
        return tableauscraper.utils.listFilters(presModel, self.name, selectedFilters)

    def setFilter(self, columnName, value, dashboardFilter=False, membershipTarget=True, filterDelta=False):
        try:
            filter = [
                {
                    "globalFieldName": t["globalFieldName"],
                    "indices": (
                        ([t["values"].index(value) + t["ordinal"]])
                        if not isinstance(value, list)
                        else [
                            t["values"].index(it) + t["ordinal"]
                            for it in value
                        ]
                    ),
                    "selection": t["selection"],
                    "selectionAlt": t["selectionAlt"],
                    "values": t["values"],
                    "ordinal": t["ordinal"]
                }
                for t in self.getFilters()
                if t["column"] == columnName
            ]
            if len(filter) == 0:
                self._scraper.logger.error(f"column {columnName} not found")
                return tableauscraper.TableauWorkbook(
                    scraper=self._scraper, originalData={}, originalInfo={}, data=[]
                )
            selectedIndex = []

            # get selection from filterJson
            if (len(filter[0]["selection"]) > 0):
                for idx, val in enumerate(filter[0]["values"]):
                    if val in filter[0]["selection"]:
                        selectedIndex.append(idx + filter[0]["ordinal"])

            # get selection from quickFilter
            if (len(filter[0]["selectionAlt"]) > 0) and ("domainTables" in filter[0]["selectionAlt"][0]):
                for idx, val in enumerate(filter[0]["selectionAlt"][0]["domainTables"]):
                    if ("isSelected" in val) and val["isSelected"] and (idx not in selectedIndex):
                        selectedIndex.append(idx)

            if dashboardFilter:
                r = tableauscraper.api.dashboardFilter(
                    self._scraper, columnName, [value] if not isinstance(value, list) else value)
            else:
                r = tableauscraper.api.filter(
                    self._scraper,
                    worksheetName=self.name,
                    globalFieldName=filter[0]["globalFieldName"],
                    selection=filter[0]["indices"],
                    selectionToRemove=[] if not filterDelta else selectedIndex,
                    membershipTarget=membershipTarget,
                    filterDelta=filterDelta
                )
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
            selectableItems = [
                {
                    "column": t["fieldCaption"],
                    "values": next(iter([y for y in tableauscraper.utils.getData(self._data_dictionnary, [t]).values()]), [])
                }
                for t in tableauscraper.utils.getIndicesInfoVqlResponse(presModel, self.name, noSelectFilter=True)
            ]
            if len(selectableItems) == 0:
                indicesInfo = tableauscraper.utils.getIndicesInfoStoryPoint(
                    presModel, self.name, noSelectFilter=True)
                return [
                    {
                        "column": t["fieldCaption"],
                        "values": next(iter([y for y in tableauscraper.utils.getData(self._data_dictionnary, [t]).values()]), [])
                    }
                    for t in indicesInfo
                ]
            return selectableItems
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
                indicesInfo = tableauscraper.utils.getIndicesInfoStoryPoint(
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

    def renderTooltip(self, x, y):
        r = tableauscraper.api.renderTooltipServer(
            self._scraper, self.name, x, y)
        return tableauscraper.utils.getTooltipText(r)
