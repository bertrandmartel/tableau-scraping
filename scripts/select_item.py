from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/PlayerStats-Top5Leagues20192020/OnePlayerSummary"

ts = TS()
ts.loads(url)

# show selectable columns
columns = ts.getWorksheet("ATT MID CREATIVE COMP").getSelectableColumns()
print(columns)

# show values by column name
values = ts.getWorksheet("ATT MID CREATIVE COMP").getValues("ATTR(Player)")
print(values)

# select that value
dashboard = ts.getWorksheet("ATT MID CREATIVE COMP").select(
    "ATTR(Player)", "Vinicius Júnior"
)

# display worksheets
for t in dashboard.worksheets:
    print(t.data)
