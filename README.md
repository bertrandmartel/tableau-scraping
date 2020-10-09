# Tableau scraping scripts

R and Python scripts to scrape [Tableau viz](https://www.tableau.com/solutions/gallery) into dataframe

You just need to update tableau host and path in the files, the script will :

* get the session token
* get the data
* extract the list of worksheet available and prompt user to choose one
* parse the complex json datamodel to get the data
* put the data into a dataframe

See [my stackoverflow posts about this topic](https://stackoverflow.com/search?q=user%3A2614364+%5Btableau-api%5D)

## Usage

### Python

```python
python tableau.py
```

### R

```R
Rscript tableau.R
```

## Output

```
~/tableau-scraping$ python3 tableau.py 
[0] + PCR by age
[1] County map
[2] Death by age
[3] Death eth
[4] Death race
[5] PCR+ eth
[6] PCR+ race
[7] Testing Report Update Date
[8] test date by age
select worksheet by index: 1
you selected : County map
    Latitude (generated)-value Latitude (generated)-alias Longitude (generated)-value Longitude (generated)-alias    County-value    County-alias Only KC and Joplin-value Only KC and Joplin-alias
0                      37.2725                     37.273                    -92.4725                     -92.473          WRIGHT          WRIGHT              KANSAS CITY              KANSAS CITY
1                      40.4778                     40.478                    -94.4318                     -94.432           WORTH           WORTH                   JOPLIN                   JOPLIN
2                      37.2756                     37.276                    -92.8844                     -92.884         WEBSTER         WEBSTER                        0                        0
3                      37.1184                     37.118                    -90.5006                     -90.501           WAYNE           WAYNE                        0                        0
4                      37.9701                     37.970                     -90.868                     -90.868      WASHINGTON      WASHINGTON                        0                        0
5                      38.7692                     38.769                    -91.1898                     -91.190          WARREN          WARREN                        0                        0
6                      37.8515                     37.852                    -94.3425                     -94.343          VERNON          VERNON                        0                        0
7                      37.3295                     37.330                    -91.9496                     -91.950           TEXAS           TEXAS                        0                        0
8                      36.6632                     36.663                    -93.0397                     -93.040           TANEY           TANEY                        0                        0
9                      40.2195                     40.220                    -93.1111                     -93.111        SULLIVAN        SULLIVAN                        0                        0
10                     36.7415                     36.742                    -93.4417                     -93.442           STONE           STONE                        0                        0
11                     36.8776                     36.878                    -89.9732                     -89.973        STODDARD        STODDARD                        0                        0
12                     37.8995                     37.900                    -90.1973                     -90.197   STE GENEVIEVE   STE GENEVIEVE                        0                        0
13                     38.6529                     38
```

## Tableau viz working

* https://public.tableau.com/views/COVID-19inMissouri/COVID-19inMissouri
* https://public.tableau.com/views/UVACOVIDTracker/Summary
* https://public.tableau.com/views/S07StuP58/Dashboard1
* https://public.tableau.com/views/COVID-19CasesandDeathsinthePhilippines_15866705872710/Home
* https://public.tableau.com/views/MKTScoredeisolamentosocial/VisoGeral
* https://results.mo.go/t/COVID19/views/Demographics/Public-Demographics

## Tableau viz not working

* https://public.tableau.com/views/CMI-2_0/CMI
* https://tableau.ons.org.br/t/ONS_Publico/views/DemandaMxima/HistricoDemandaMxima
