# The following script will get the session token, get the data,
# prompt the user to select a worksheet, parse the data into a dataframe
import json
import pandas as pd
import argparse
from tableauscraper import TableauScraper as TS
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    "-get",
    "--get",
    choices=["dashboard", "dropdown", "select"],
    help="type of action",
    required=True,
)
parser.add_argument("-url", "--url", help="full tableau url", required=True)
args = parser.parse_args()

ts = TS()
ts.loads(args.url)

# checkout the json data
# with open('data.json', 'w', encoding='utf-8') as f:
#    json.dump(ts.data, f, ensure_ascii=False, indent=4)
# with open('info.json', 'w', encoding='utf-8') as f:
#    json.dump(ts.info, f, ensure_ascii=False, indent=4)

if args.get == "dashboard":
    dashboard = ts.promptDashboard()
elif args.get == "dropdown":
    dashboard = ts.promptDropdown()
elif args.get == "select":
    dashboard = ts.promptSelect()

with pd.option_context(
    "display.max_rows", None, "display.max_columns", 5, "display.width", 1000
):
    for idx, worksheet in enumerate(dashboard.worksheets):
        if idx == 0:
            print("|" + ("-" * (os.get_terminal_size().columns - 2)) + "|")
        print("|" + worksheet.name.center(os.get_terminal_size().columns - 2) + "|")
        print("|" + ("-" * (os.get_terminal_size().columns - 2)) + "|")
        print(worksheet.data)
        print("")
        # selectable values
        selectableColumns = worksheet.getSelectableColumns()
        print(f"selectable columns for this worksheet : {len(selectableColumns)}")
        for columnName in selectableColumns:
            print("• " + columnName)
            # for value in worksheet.getValues(columnName):
            # 	print("\t•" + value)

        print("")
        print("|" + ("-" * (os.get_terminal_size().columns - 2)) + "|")

    # dropdown list
    dropdownInputs = dashboard.getDropdownInputs()
    print(f"drop down lists for this dashboard : {len(dropdownInputs)}")
    for inputName in dropdownInputs:
        print("• " + inputName)
        for inputValue in dashboard.getDropdownValues(inputName):
            print("\t• " + inputValue)
