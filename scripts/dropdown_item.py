from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/PlayerStats-Top5Leagues20192020/OnePlayerSummary"

ts = TS()
ts.loads(url)
workbook = ts.getWorkbook()

# show parameters columns/values
parameters = workbook.getParameters()
print(parameters)

# set parameter
workbook = workbook.setParameter("P.League 2", "Ligue 1")

# display worksheets
for t in workbook.worksheets:
    print(t.data)
