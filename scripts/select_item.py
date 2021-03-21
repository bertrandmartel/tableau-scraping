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
