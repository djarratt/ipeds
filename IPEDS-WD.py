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
            targetData = row['Basic']
            # if targetData == "Tribal Colleges":
            #     targetQ = "Q23542851"
            # elif targetData == "Doctoral Universities: Highest Research Activity":
            #     targetQ = "Q23334765"
            # elif targetData == "Doctoral Universities: Higher Research Activity":
            #     targetQ = "Q23334891"
            # elif targetData == "Doctoral Universities: Moderate Research Activity":
            #     targetQ = "Q23334993"
            # if targetData == "Master's Colleges & Universities: Larger Programs":
            #     targetQ = "Q23335394"
            # elif targetData == "Master's Colleges & Universities: Medium Programs":
            #     targetQ = "Q23335494"
            # elif targetData == "Master's Colleges & Universities: Small Programs":
            #     targetQ = "Q23335549"
            if targetData == "Baccalaureate Colleges: Diverse Fields":
                targetQ = "Q23336120"
            elif targetData == "Baccalaureate Colleges: Arts & Sciences Focus":
                targetQ = "Q23336065"
            elif targetData == "Baccalaureate/Associate's Colleges: Mixed Baccalaureate/Associate's":
                targetQ = "Q23336577"
            elif targetData == "Baccalaureate/Associate's Colleges: Associate's Dominant":
                targetQ = "Q23336706"
            else:
                targetQ = None
            if targetQ is not None:
                countMatches += 1
                print("Q" + qid + "\t" + "P2643" + "\t" + targetQ +
                      "\t" + "S248" + "\t" + "Q4223026")

print("Identified {0} matches".format(countMatches))
