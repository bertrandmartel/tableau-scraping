from tableauscraper import TableauScraper as TS

url = "https://public.tableau.com/views/PlayerStats-Top5Leagues20192020/OnePlayerSummary"

ts = TS()
ts.loads(url)
dashboard = ts.getDashboard()


# show dropdown input name
inputNames = dashboard.getDropdownInputs()
print(inputNames)

# show dropdown values for a given input name
values = dashboard.getDropdownValues("P.League 2")
print(values)

# select that value
dashboard = dashboard.setDropdown("P.League 2", "Ligue 1")

# display worksheets
for t in dashboard.worksheets:
    print(t.data)
