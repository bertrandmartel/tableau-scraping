# The following script will get the session token, get the data, 
# prompt the user to select a worksheet, parse the data into a dataframe
import requests
from bs4 import BeautifulSoup
import json
import re
import pandas as pd

#replace the hostname and the path if necessary
host_url = "https://results.mo.gov"
path = "/t/COVID19/views/Demographics/Public-Demographics"

url = f"{host_url}{path}"

r = requests.get(
    url,
    params= {
        ":embed": "y",
        ":showVizHome": "no"
    }
) 
soup = BeautifulSoup(r.text, "html.parser")

tableauData = json.loads(soup.find("textarea",{"id": "tsConfigContainer"}).text)

dataUrl = f'{host_url}{tableauData["vizql_root"]}/bootstrapSession/sessions/{tableauData["sessionid"]}'

r = requests.post(dataUrl, data= {
    "sheet_id": tableauData["sheetId"],
})

dataReg = re.search('\d+;({.*})\d+;({.*})', r.text, re.MULTILINE)
info = json.loads(dataReg.group(1))
data = json.loads(dataReg.group(2))

worksheets = list(data["secondaryInfo"]["presModelMap"]["vizData"]["presModelHolder"]["genPresModelMapPresModel"]["presModelMap"].keys())

for idx, ws in enumerate(worksheets):
    print(f"[{idx}] {ws}")

selected = input("select worksheet by index: ")
worksheet = worksheets[int(selected)]
print(f"you selected : {worksheet}")

columnsData = data["secondaryInfo"]["presModelMap"]["vizData"]["presModelHolder"]["genPresModelMapPresModel"]["presModelMap"][worksheet]["presModelHolder"]["genVizDataPresModel"]["paneColumnsData"]
result = [ 
    {
        "fieldCaption": t.get("fieldCaption", ""), 
        "valueIndices": columnsData["paneColumnsList"][t["paneIndices"][0]]["vizPaneColumns"][t["columnIndices"][0]]["valueIndices"],
        "aliasIndices": columnsData["paneColumnsList"][t["paneIndices"][0]]["vizPaneColumns"][t["columnIndices"][0]]["aliasIndices"],
        "dataType": t.get("dataType"),
        "paneIndices": t["paneIndices"][0],
        "columnIndices": t["columnIndices"][0]
    }
    for t in columnsData["vizDataColumns"]
    if t.get("fieldCaption")
]
dataFull = data["secondaryInfo"]["presModelMap"]["dataDictionary"]["presModelHolder"]["genDataDictionaryPresModel"]["dataSegments"]["0"]["dataColumns"]

def onAlias(it, value, cstring):
	return value[it] if (it >= 0) else cstring["dataValues"][abs(it)-1]

frameData = {}
cstring = [t for t in dataFull if t["dataType"] == "cstring"][0]
for t in dataFull:
    for index in result:
        if (t["dataType"] == index["dataType"]):
            if len(index["valueIndices"]) > 0:
                frameData[f'{index["fieldCaption"]}-value'] = [t["dataValues"][abs(it)] for it in index["valueIndices"]]
            if len(index["aliasIndices"]) > 0:
                frameData[f'{index["fieldCaption"]}-alias'] = [onAlias(it, t["dataValues"], cstring) for it in index["aliasIndices"]]

df = pd.DataFrame.from_dict(frameData, orient='index').fillna(0).T
with pd.option_context('display.max_rows', None, 'display.max_columns', None, 'display.width', 1000):
    print(df)