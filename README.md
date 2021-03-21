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

- Get worksheets data

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

- Get a specific worksheet

```python
from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/PlayerStats-Top5Leagues20192020/OnePlayerSummary"

ts = TS()
ts.loads(url)

worksheet = ts.getWorksheet("ATT MID CREATIVE COMP")
print(worksheet.data)
```

- select a selectable item

```python
from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/PlayerStats-Top5Leagues20192020/OnePlayerSummary"

ts = TS()
ts.loads(url)

#show selectable columns
columns = ts.getWorksheet("ATT MID CREATIVE COMP").getSelectableColumns()
print(columns)

#show values by column name
values = ts.getWorksheet("ATT MID CREATIVE COMP").getValues("ATTR(Player)")
print(values)

#select that value
wb = ts.getWorksheet("ATT MID CREATIVE COMP").select("ATTR(Player)", "Vinicius Júnior")

#display worksheets
for t in wb.worksheets:
	print(t.data)
```

[Try this on repl.it](https://repl.it/@bertrandmartel/TableauSelectItem)

- set parameter

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

- set filter

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
wb = ws.setFilter('[Olympics]', 'Winter')

# show the new data for worksheet
countyWs = wb.getWorksheet("Bar Chart")
print(countyWs.data)
```

[Try this on repl.it](https://repl.it/@bertrandmartel/TableauFilter)

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

### Testing Python script

To discover all worksheets, selectable columns and dropdowns, run `prompt.py` script under `scripts` directory :

```bash
git clone git@github.com:bertrandmartel/tableau-scraping.git
cd tableau-scraping/scripts

#get worksheets data
python3 prompt.py -get dashboard -url "https://public.tableau.com/views/COVID-19inMissouri/COVID-19inMissouri"

#select a selectable item
python3 prompt.py -get select -url "https://public.tableau.com/views/MKTScoredeisolamentosocial/VisoGeral"

#select an item in dropdown
python3 prompt.py -get dropdown -url "https://public.tableau.com/views/COVID-19DailyDashboard_15960160643010/Casesbyneighbourhood"
```

### Settings

`TableauScraper` class has the following optional parameters :

| Parameters | default value | description                                                       |
| ---------- | ------------- | ----------------------------------------------------------------- |
| logLevel   | logging.INFO  | log level                                                         |
| delayMs    | 500           | minimum delay in millis between actions (select/dropdown request) |

## R

under `R` directory :

```R
Rscript tableau.R
```

R library is under development

## Stackoverflow Questions

See [those stackoverflow posts about this topic](https://stackoverflow.com/search?q=user%3A2614364+%5Btableau-api%5D)
