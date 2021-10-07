import pandas as pd
from typing import List
import tableauscraper
from tableauscraper import utils
from tableauscraper import dashboard
from tableauscraper import api
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
        # persist data dictionary
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

        # update filters if present
        if ("applicationPresModel" in cmdResponse["vqlCmdResponse"]["layoutStatus"]):
            newFilters = utils.getFiltersForAllWorksheet(
                self.logger, data=cmdResponse, info=None, rootDashboard=self._scraper.dashboard, cmdResponse=True)
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

    def getColumns(self) -> List[str]:
        if self.cmdResponse:
            presModel = self._originalData["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
            return [
                t["fieldCaption"]
                for t in utils.getIndicesInfoVqlResponse(
                    presModel, self.name, noSelectFilter=True
                )
            ]
        else:
            presModel = utils.getPresModelVizData(
                self._originalData)
            return [
                t["fieldCaption"]
                for t in utils.getIndicesInfo(
                    presModel, self.name, noSelectFilter=True
                )
            ]

    def getFilters(self) -> List[str]:
        return self._scraper.filters[self.name] if self.name in self._scraper.filters else []

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
                    "ordinal": t["ordinal"],
                    "storyboard": t["storyboard"] if "storyboard" in t else None,
                    "storyboardId": t["storyboardId"] if "storyboardId" in t else None,
                    "dashboard": t["dashboard"] if "dashboard" in t else self._scraper.dashboard
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
                r = api.dashboardFilter(
                    self._scraper, columnName, [value] if not isinstance(value, list) else value)
            else:
                r = api.filter(
                    self._scraper,
                    worksheetName=self.name,
                    globalFieldName=filter[0]["globalFieldName"],
                    selection=filter[0]["indices"],
                    selectionToRemove=[] if not filterDelta else selectedIndex,
                    membershipTarget=membershipTarget,
                    filterDelta=filterDelta,
                    storyboard=filter[0]["storyboard"],
                    storyboardId=filter[0]["storyboardId"],
                    dashboard=filter[0]["dashboard"]
                )
            self.updateFullData(r)
            return dashboard.getWorksheetsCmdResponse(self._scraper, r)
        except ValueError as e:
            self._scraper.logger.error(str(e))
            return tableauscraper.TableauWorkbook(
                scraper=self._scraper, originalData={}, originalInfo={}, data=[]
            )
        except api.APIResponseException as e:
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
                    "values": next(iter([y for y in utils.getData(self._data_dictionnary, [t]).values()]), [])
                }
                for t in utils.getIndicesInfoVqlResponse(presModel, self.name, noSelectFilter=True)
            ]
            if len(selectableItems) == 0:
                indicesInfo = utils.getIndicesInfoStoryPoint(
                    presModel, self.name, noSelectFilter=True)
                return [
                    {
                        "column": t["fieldCaption"],
                        "values": next(iter([y for y in utils.getData(self._data_dictionnary, [t]).values()]), [])
                    }
                    for t in indicesInfo
                ]
            return selectableItems
        else:
            presModel = utils.getPresModelVizData(
                self._originalData)
            if presModel is None:
                presModel = utils.getPresModelVizInfo(
                    self._originalInfo)
                indicesInfo = utils.getIndicesInfoStoryPoint(
                    presModel, self.name, noSelectFilter=True)
            else:
                indicesInfo = utils.getIndicesInfo(
                    presModel, self.name, noSelectFilter=True)
            return [
                {
                    "column": t["fieldCaption"],
                    "values": next(iter([
                        y
                        for y in utils.getData(self._data_dictionnary, [t]).values()
                    ]), [])
                }
                for t in indicesInfo
            ]

    def getSelectableValues(self, column) -> List[str]:
        if self.cmdResponse:
            presModel = self._originalData["vqlCmdResponse"]["layoutStatus"]["applicationPresModel"]
            columnObj = [
                t
                for t in utils.getIndicesInfoVqlResponse(
                    presModel, self.name, noSelectFilter=True
                )
                if t["fieldCaption"] == column
            ]
            if len(columnObj) == 0:
                indicesInfo = utils.getIndicesInfoStoryPoint(
                    presModel, self.name, noSelectFilter=True)
                columnObj = [
                    t
                    for t in indicesInfo
                    if t["fieldCaption"] == column
                ]
                if len(columnObj) == 0:
                    return []
            frameData = utils.getData(
                self._data_dictionnary, [columnObj[0]]
            )
            frameDataKeys = list(frameData.keys())

            if len(frameDataKeys) == 0:
                return []
            return frameData[frameDataKeys[0]]
        else:
            presModel = utils.getPresModelVizData(
                self._originalData)
            if presModel is None:
                presModel = utils.getPresModelVizInfo(
                    self._originalInfo)
                indicesInfo = utils.getIndicesInfoStoryPoint(
                    presModel, self.name, noSelectFilter=True)
            else:
                indicesInfo = utils.getIndicesInfo(
                    presModel, self.name, noSelectFilter=True)

            columnObj = [
                t
                for t in indicesInfo
                if t["fieldCaption"] == column
            ]
            if len(columnObj) == 0:
                return []
            frameData = utils.getData(
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
                for t in utils.getIndicesInfoVqlResponse(
                    presModel, self.name, noSelectFilter=True, noFieldCaption=True
                )
                if t["fn"] == "[system:visual].[tuple_id]"
            ]
            if len(columnObj) == 0:
                return []

            return [t["tupleIds"] for t in columnObj]
        else:
            presModel = utils.getPresModelVizData(
                self._originalData)
            columnObj = [
                t
                for t in utils.getIndicesInfo(
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
            r = api.select(self._scraper, self.name, [index])
            self.updateFullData(r)
            return dashboard.getWorksheetsCmdResponse(self._scraper, r)
        except ValueError as e:
            self._scraper.logger.error(str(e))
            return tableauscraper.TableauWorkbook(
                scraper=self._scraper, originalData={}, originalInfo={}, data=[]
            )

    def getDownloadableSummaryData(self, numRows=200):
        r = api.getDownloadableSummaryData(
            self._scraper, self.name, self._scraper.dashboard, numRows)
        self.updateFullData(r)
        return dashboard.getWorksheetDownloadCmdResponse(self._scraper, r)

    def getDownloadableUnderlyingData(self, numRows=200):
        r = api.getDownloadableUnderlyingData(
            self._scraper, self.name, self._scraper.dashboard, numRows)
        self.updateFullData(r)
        return dashboard.getWorksheetDownloadCmdResponse(self._scraper, r)

    def levelDrill(self, drillDown, position=0):
        r = api.levelDrill(
            self._scraper, self.name, drillDown, position)
        self.updateFullData(r)
        return dashboard.getWorksheetsCmdResponse(self._scraper, r)

    def renderTooltip(self, x, y):
        r = api.renderTooltipServer(
            self._scraper, self.name, x, y)
        return utils.getTooltipText(r)
