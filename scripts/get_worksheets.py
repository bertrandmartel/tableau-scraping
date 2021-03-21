from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/PlayerStats-Top5Leagues20192020/OnePlayerSummary"

ts = TS()
ts.loads(url)
workbook = ts.getWorkbook()

for t in workbook.worksheets:
    # show worksheet name
    print(f"WORKSHEET NAME : {t.name}")
    # show dataframe for this worksheet
    print(t.data)
