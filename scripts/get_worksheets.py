from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/PlayerStats-Top5Leagues20192020/OnePlayerSummary"

ts = TS()
ts.loads(url)
dashboard = ts.getDashboard()

for t in dashboard.worksheets:
    # show worksheet name
    print(f"WORKSHEET NAME : {t.name}")
    # show dataframe for this worksheet
    print(t.data)
