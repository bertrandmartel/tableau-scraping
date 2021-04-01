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
    choices=["workbook", "parameter", "select"],
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

if args.get == "workbook":
    workbook = ts.promptDashboard()
elif args.get == "parameter":
    workbook = ts.promptParameters()
elif args.get == "select":
    workbook = ts.promptSelect()

with pd.option_context(
    "display.max_rows", None, "display.max_columns", 5, "display.width", 1000
):
    for idx, worksheet in enumerate(workbook.worksheets):
        if idx == 0:
            print("|" + ("-" * (os.get_terminal_size().columns - 2)) + "|")
        print("|" + worksheet.name.center(os.get_terminal_size().columns - 2) + "|")
        print("|" + ("-" * (os.get_terminal_size().columns - 2)) + "|")
        print(worksheet.data)
        print("")
        print("selectable values")
        # selectable values
        selection = worksheet.getSelectableItems()
        print(
            f"selectable items for this worksheet : {len(selection)}")
        for select in selection:
            print(f'column: ${select["column"]}')
            print(f'values: {select["values"]}')
            print("--------------")

        print("filterable values")
        # filterable values
        filters = worksheet.getFilters()
        for t in filters:
            print(f'column: ${t["column"]}')
            print(f'values: {t["values"]}')
            print("--------------")

        print("")
        print("|" + ("-" * (os.get_terminal_size().columns - 2)) + "|")

    # parameters list
    parameters = workbook.getParameters()
    print(f"parameters lists for this workbook : {len(parameters)}")
    for param in parameters:
        print(param)
        print(param["values"])
