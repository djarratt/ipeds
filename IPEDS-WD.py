# -*- coding: iso-8859-15 -*-
import csv
import json


def getQ(unitid):
    for i in crosswalk:
        if unitid == i[2]:
            return str(i[0])
    return "0"


with open('wikidata_query_result.json', 'rb') as f:
    data = json.loads(f.read())
    crosswalk = data["props"]["1771"]

countMatches = 0
with open('carnegieBasic.csv', 'rb') as csvfile:
    inflowFile = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in inflowFile:
        unitid = row['unitid']
        qid = getQ(unitid)
        if qid is not "0":
            targetData = row['Enrollment Profile']
            if targetData == "Exclusively graduate":
                targetQ = "Q23623496"
            elif targetData == "Exclusively undergraduate four-year":
                targetQ = "Q23623476"
            elif targetData == "Exclusively undergraduate two-year":
                targetQ = "Q23623474"
            elif targetData == "High undergraduate":
                targetQ = "Q23623483"
            elif targetData == "Majority graduate":
                targetQ = "Q23623491"
            elif targetData == "Majority undergraduate":
                targetQ = "Q23623487"
            elif targetData == "Very high undergraduate":
                targetQ = "Q23623479"                
            else:
                targetQ = None
            if targetQ is not None:
                countMatches += 1
                print("Q" + qid + "\t" + "P2643" + "\t" + targetQ +
                      "\t" + "S248" + "\t" + "Q4223026")

print("Identified {0} matches".format(countMatches))
