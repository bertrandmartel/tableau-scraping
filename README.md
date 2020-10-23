# Tableau Scraper

[![CI](https://github.com/bertrandmartel/tableau-scraping/workflows/CI/badge.svg)](https://github.com/bertrandmartel/tableau-scraping/actions)
[![codecov](https://codecov.io/gh/bertrandmartel/tableau-scraping/branch/master/graph/badge.svg?token=F4R3NZF796)](https://codecov.io/gh/bertrandmartel/tableau-scraping)
[![License](http://img.shields.io/:license-mit-blue.svg)](LICENSE.md)

Python library to scrape data from [Tableau viz](https://public.tableau.com/fr-fr/gallery)

R library is under development but a script is available to get the worksheets, see [this](#R)

## Python

### Install

```
pip install tableau-scraper
```

### Usage

* Get worksheets data

```python
from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/PlayerStats-Top5Leagues20192020/OnePlayerSummary"

ts = TS()
ts.loads(url)
dashboard = ts.getDashboard()

for t in dashboard.worksheets:
	#show worksheet name
	print(f"WORKSHEET NAME : {t.name}")
	#show dataframe for this worksheet
	print(t.data)
```

* select a selectable item 

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
dashboard = ts.getWorksheet("ATT MID CREATIVE COMP").select("ATTR(Player)", "Vinicius Júnior")

#display worksheets 
for t in dashboard.worksheets:
	print(t.data)
```

* select item in a dropdown

```python
from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/PlayerStats-Top5Leagues20192020/OnePlayerSummary"

ts = TS()
ts.loads(url)
dashboard = ts.getDashboard()

#show dropdown input name
inputNames = dashboard.getDropdownInputs()
print(inputNames)

#show dropdown values for a given input name
values = dashboard.getDropdownValues("P.League 2")
print(values)

#select that value
dashboard = dashboard.setDropdown("P.League 2", "Ligue 1")

#display worksheets 
for t in dashboard.worksheets:
	print(t.data)
```

### Important Note

In `ts.loads(url)` you must input the Tableau URL which can be different from the one you're looking at in the browser. Open the network tab under Chrome Development tools and look for URL with those query params : `:embed=y` and `:showVizHome=no`. Before the session query which looks like `315165BFBC204028B80CD3FB73880452-0:0` in the network tabs

In the following screenshot, the first request is the corret URL. The last request is the session query :

![network tabs](https://user-images.githubusercontent.com/5183022/96939027-2e716780-14cc-11eb-8712-5f6292af8bef.png)

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
python3 tableau.py -get dropdown -url "https://public.tableau.com/views/COVID-19DailyDashboard_15960160643010/Casesbyneighbourhood"
```

### Settings

`TableauScraper` class has the following optional parameters : 

| Parameters      |  default value     |  description |
|-----------------|--------------------|--------------|
| logLevel        |logging.INFO |   log level |
| delayMs         |  500        |  minimum delay in millis between actions (select/dropdown request) |

## R

under `R` directory :

```R
Rscript tableau.R
```

R library is under development

## How it works

Tableau dashboard is rendered get its data from an internal API. In order to get the data, you must get the initial tableau URL which is called with the query parameter `:embed=y` and `:showVizHome=no` (checkout networks logs)

In the html body, you have a `textarea` tag with id `tsConfigContainer` with a JSON configuration. The `session_id` field and root path `vizql_root` makes possible to build the session uri : 

    POST https://public.tableau.com/ROOT_PATH/bootstrapSession/sessions/SESSION_ID

The result is 2 json objects. One of them contains the data. The JSON object is complex since it dissociates the value indices from the column indices and from the worksheets.

## Stackoverflow Questions

See [those stackoverflow posts about this topic](https://stackoverflow.com/search?q=user%3A2614364+%5Btableau-api%5D)
