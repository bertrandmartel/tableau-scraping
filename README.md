# Tableau Scraper

[![PyPI](https://img.shields.io/pypi/v/TableauScraper.svg)](https://pypi.python.org/pypi/TableauScraper)
[![CI](https://github.com/bertrandmartel/tableau-scraping/workflows/CI/badge.svg)](https://github.com/bertrandmartel/tableau-scraping/actions)
[![codecov](https://codecov.io/gh/bertrandmartel/tableau-scraping/branch/master/graph/badge.svg?token=F4R3NZF796)](https://codecov.io/gh/bertrandmartel/tableau-scraping)
[![License](http://img.shields.io/:license-mit-blue.svg)](LICENSE.md)

Python library to scrape data from [Tableau viz](https://public.tableau.com/fr-fr/gallery)

R library is under development but a script is available to get the worksheets, see [this](https://github.com/bertrandmartel/tableau-scraping#r)

## Python

### Install

```bash
pip install TableauScraper
```

### Usage

#### Get worksheets data

```python
from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/PlayerStats-Top5Leagues20192020/OnePlayerSummary"

ts = TS()
ts.loads(url)
workbook = ts.getWorkbook()

for t in workbook.worksheets:
    print(f"worksheet name : {t.name}") #show worksheet name
    print(t.data) #show dataframe for this worksheet
```

[Try this on repl.it](https://repl.it/@bertrandmartel/TableauGetWorksheets)

#### Get a specific worksheet

```python
from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/PlayerStats-Top5Leagues20192020/OnePlayerSummary"

ts = TS()
ts.loads(url)

ws = ts.getWorksheet("ATT MID CREATIVE COMP")
print(ws.data)
```

#### select a selectable item

```python
from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/PlayerStats-Top5Leagues20192020/OnePlayerSummary"

ts = TS()
ts.loads(url)

ws = ts.getWorksheet("ATT MID CREATIVE COMP")

# show selectable values
selections = ws.getSelectableItems()
print(selections)

# select that value
dashboard = ws.select("ATTR(Player)", "Vinicius Júnior")

# display worksheets
for t in dashboard.worksheets:
    print(t.data)
```

[Try this on repl.it](https://repl.it/@bertrandmartel/TableauSelectItem)

#### set parameter

Get list of parameters with `workbook.getParameters()` and set parameter value using `workbook.setParameter("column_name", "value")` :

```python
from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/PlayerStats-Top5Leagues20192020/OnePlayerSummary"

ts = TS()
ts.loads(url)
workbook = ts.getWorkbook()

# show parameters values / column
parameters = workbook.getParameters()
print(parameters)

# set parameters column / value
workbook = workbook.setParameter("P.League 2", "Ligue 1")

# display worksheets
for t in workbook.worksheets:
    print(t.data)
```

[Try this on repl.it](https://repl.it/@bertrandmartel/TableauParameter)

It's possible to override the parameter name used in the API requests using `inputParameter`, which is different from the input name:

```
wb = wb.setParameter(inputName=None, value="Ligue 1",
                     inputParameter="[Parameters].[P.League (copy)_1642969456470679625]")
```

#### set filter

Get list of filters with `worksheet.getFilters` and set filter value using `worksheet.setFilter("column_name", "value")`:

```python
from tableauscraper import TableauScraper as TS

url = 'https://public.tableau.com/views/WomenInOlympics/Dashboard1'
ts = TS()
ts.loads(url)

# show original data for worksheet
ws = ts.getWorksheet("Bar Chart")
print(ws.data)

# get filters columns and values
filters = ws.getFilters()
print(filters)

# set filter value
wb = ws.setFilter('Olympics', 'Winter')

# show the new data for worksheet
countyWs = wb.getWorksheet("Bar Chart")
print(countyWs.data)
```

[Try this on repl.it](https://repl.it/@bertrandmartel/TableauFilter)

#### More advanced filtering options

- You can specify `dashboardFilter=True` in order to use `dashboard-categorical-filter` API instead of `categorical-filter-by-index` API ([related](https://github.com/bertrandmartel/tableau-scraping/issues/26))
- When using `dashboardFilter=True` you can skip the filter value check usin `noCheck=True` ([related](https://github.com/bertrandmartel/tableau-scraping/issues/50))

- You can discard `membershipTarget` property from being sent in `setFilter` using `setFilter('COLUMN','VALUE', membershipTarget=False)` ([related](https://github.com/bertrandmartel/tableau-scraping/issues/29))

- You can specify multiple filters for filters that enable that feature using `setFilter('COLUMN', ['VALUE1','VALUE2'])`

- You can specify a "filter-delta" filter type adding the parameter `filterDelta=True` like the following `setFilter('COLUMN','VALUE', filterDelta=True)`. This will discard all filters and add the one corresponding to `['VALUE']` in this case. This is helpful when all or some filters are selected by default, and you want to unselect them. The default behaviour (`filterDelta=False`) is `filter-replace` which sometimes doesn't work when filter multi-selection is possible in the dashboard. [example](https://replit.com/@bertrandmartel/TableauUSCustoms)

- In last recourse, you can use `indexValues` property to directly specify the indices (if there is a bug in the library or anything comes up): `setFilter('COLUMN', [], indexValues=[0,1,2])`

#### Story points

Some Tableau dashboard have storypoints where you can navigate. To list the storypoints and go to a specific storypoints:

```python
from tableauscraper import TableauScraper as TS

url = 'https://public.tableau.com/views/EarthquakeTrendStory2/Finished-Earthquakestory'
ts = TS()
ts.loads(url)
wb = ts.getWorkbook()

print(wb.getStoryPoints())
print("go to specific storypoint")
sp = wb.goToStoryPoint(storyPointId=10)

print(sp.getWorksheetNames())
print(sp.getWorksheet("Timeline").data)
```

[Try this on repl.it](https://replit.com/@bertrandmartel/TableauEarthquakeStorypoint)

#### Level drill Up/Down

On some graph/table, there is a drill up/down feature used to zoom in or out data like this
![drill up/down](https://user-images.githubusercontent.com/5183022/123021337-332c4980-d3d4-11eb-8e8c-d19c5b989edb.png)

```python
from tableauscraper import TableauScraper as TS

url = 'https://tableau.azdhs.gov/views/ELRv2testlevelandpeopletested/PeopleTested'
ts = TS()
ts.loads(url)
wb = ts.getWorkbook()

sheetName = "P1 - Tests by Day W/ % Positivity (Both) (2)"

drillDown1 = wb.getWorksheet(sheetName).levelDrill(drillDown=True, position=1)
drillDown2 = drillDown1.getWorksheet(sheetName).levelDrill(drillDown=True, position=1)
drillDown3 = drillDown2.getWorksheet(sheetName).levelDrill(drillDown=True, position=1)

print(drillDown1.getWorksheet(sheetName).data)
print(drillDown2.getWorksheet(sheetName).data)
print(drillDown3.getWorksheet(sheetName).data)
```

[Try this on repl.it](https://replit.com/@bertrandmartel/TableauCovid19AzdhsPeopleTested)

The `position` parameter is default to `0`. It doesn't seem to be present in the json configuration. If the default is not working try incrementing it or checkout the network tabs using Chrome devtools.

#### Download CSV data

For Tableau URL that have the download feature enabled, you can download full data using:

```python
from tableauscraper import TableauScraper as TS

url = 'https://public.tableau.com/views/WYCOVID-19Dashboard/WyomingCOVID-19CaseDashboard'
ts = TS()
ts.loads(url)
wb = ts.getWorkbook()
data = wb.getCsvData(sheetName='case map')

print(data)
```

Note that in some Tableau server, the prefix used in the API url is different. As it's set in the javascript, it must be set manually if it's not the same as public.tableau.com like:

```python
wb.getCsvData(sheetName='worksheet1', prefix="vud")
```

The prefix values, I've encountered are: `vud` and `vudcsv`. The default is `vudcsv`.

[Try this on repl.it](https://replit.com/@bertrandmartel/TableauCovidWyomingCsv)

#### Download Cross Tab data

For Tableau URL that have the crosstab feature enabled, you can download the crosstab using:

```python
from tableauscraper import TableauScraper as TS

url = "https://tableau.soa.org/t/soa-public/views/USPostLevelTermMortalityExperienceInteractiveTool/DataTable2"

ts = TS()
ts.loads(url)
wb = ts.getWorkbook()

wb.setParameter(inputName="Count or Amount", value="Amount")

data = wb.getCrossTabData(
    sheetName="Data Table 2 - Premium Jump & PLT Duration")

print(data)
```

#### Go to sheet

Get list of all sheets with subsheets visible or invisible, ability to send a go-to-sheet command (dashboar button) :

```python
from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/COVID-19VaccineTrackerDashboard_16153822244270/Dosesadministered"
ts = TS()
ts.loads(url)
workbook = ts.getWorkbook()

sheets = workbook.getSheets()
print(sheets)

nycAdults = workbook.goToSheet("NYC Adults")
for t in nycAdults.worksheets:
    print(f"worksheet name : {t.name}")  # show worksheet name
    print(t.data)  # show dataframe for this worksheet
```

#### Render tooltip

Get the tooltip html output when `render-tooltip-server` API is called. This is particularly useful when dealing with [server side rendering dashboard](https://github.com/bertrandmartel/tableau-scraping#server-side-rendering):

```python
from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/CMI-2_0/CMI"

ts = TS()
ts.loads(url)
workbook = ts.getWorkbook()
ws = workbook.getWorksheet("US Map - State - CMI")

tooltipHtml = ws.renderTooltip(x=387, y=196)
print(tooltipHtml)
```

### Sample usecases

- https://replit.com/@bertrandmartel/TableauOregonCovid
- https://replit.com/@bertrandmartel/TableauCovidIndia
- https://replit.com/@bertrandmartel/TableauCovidArizona
- https://replit.com/@bertrandmartel/TableauIllinoisOpioId
- https://replit.com/@bertrandmartel/TableauCovidNY
- https://replit.com/@bertrandmartel/TableauCovidNCDHHS
- https://replit.com/@bertrandmartel/TableauCovidWisconsin
- https://replit.com/@bertrandmartel/TableauScrapeNewspaper
- https://replit.com/@bertrandmartel/TableauStoryPoints
- https://replit.com/@bertrandmartel/TableauCovidOhio
- https://replit.com/@bertrandmartel/TableauCovidSouthCarolina
- https://replit.com/@bertrandmartel/TableauCovidNewHampshire
- https://replit.com/@bertrandmartel/TableauCovidNewJersey
- https://replit.com/@bertrandmartel/TableauCovid19Wyoming
- https://replit.com/@bertrandmartel/TableauCovid19Louisiana
- https://replit.com/@bertrandmartel/TableauCIESFootball
- https://replit.com/@bertrandmartel/TableauCovid19TestingCommonsASU
- https://replit.com/@bertrandmartel/TableauCovid19Tracker
- https://replit.com/@bertrandmartel/TableauCovid19CbreResidentMigration
- https://replit.com/@bertrandmartel/TableauEarthquakeStorypoint
- https://replit.com/@bertrandmartel/TableauCovid19AzdhsPeopleTested
- https://replit.com/@bertrandmartel/TableauCovidDDCMOPH
- https://replit.com/@bertrandmartel/TableauUSCustoms
- https://replit.com/@bertrandmartel/TableauONSDemandaMaxima
- https://replit.com/@bertrandmartel/TableauCovidAZDHSTests

### Server side rendering

If the tableau url you're working on is using [server side rendering](https://help.tableau.com/current/server/en-us/browser_rendering.htm), data can't be extracted as is.

You can checkout if your tableau url is using server side rendering by opening chrome development console / network tab. You would notice the API calls have `renderMode` properties set to `render-mode-server`:

![server side render mode](https://user-images.githubusercontent.com/5183022/135779239-8321d6a2-81b6-4ae9-8606-b20ba36a86ae.png)

Server side rendering means that no data is sent to the browser. Instead, the server is rendering the tableau chart using images only and detects selection using mouse coordinates.

To extract the data, one thing that has worked with some tableau url was to trigger a specific filter that is not server-side-rendered. You can checkout the network tab on Chrome development console to check if the filter call is using or not server-side rendering or client-side-rendering with `renderMode`:

![client side rendering](https://user-images.githubusercontent.com/5183022/115800868-b7198380-a3db-11eb-95c0-7104f7f0c77c.png)

If the filter is only using client side rendering, you can list all filters and perform the filter for each value. This technique only works if the tableau data has "cleared" the filter by default otherwise the data is already cached when the tableau data is loaded, and since it's using server side rendering you can't access this data

Checkout the following repl.it for examples with tableau url using server side rendering:

- https://replit.com/@bertrandmartel/TableauCIESFootball
- https://replit.com/@bertrandmartel/TableauCovid19TestingCommonsASU

### Testing Python script

To discover all worksheets, selectable columns and dropdowns, run `prompt.py` script under `scripts` directory :

```bash
git clone git@github.com:bertrandmartel/tableau-scraping.git
cd tableau-scraping/scripts

#get worksheets data
python3 prompt.py -get workbook -url "https://public.tableau.com/views/PlayerStats-Top5Leagues20192020/OnePlayerSummary"

#select a selectable item
python3 prompt.py -get select -url "https://public.tableau.com/views/MKTScoredeisolamentosocial/VisoGeral"

#set a parameter
python3 prompt.py -get parameter -url "https://public.tableau.com/views/COVID-19DailyDashboard_15960160643010/Casesbyneighbourhood"
```

### Settings

`TableauScraper` class has the following optional parameters :

| Parameters | default value | description                               |
| ---------- | ------------- | ----------------------------------------- |
| logLevel   | logging.INFO  | log level                                 |
| delayMs    | 500           | minimum delay in millis between api calls |

## R

under `R` directory :

```R
Rscript tableau.R
```

R library is under development

## Dependencies

[requirements.txt](https://github.com/bertrandmartel/tableau-scraping/blob/master/requirements.txt)

- pandas
- requests
- beautifulsoup4

## Stackoverflow Questions

See [those stackoverflow posts about this topic](https://stackoverflow.com/search?q=user%3A2614364+tableau+%5Bweb-scraping%5D)
