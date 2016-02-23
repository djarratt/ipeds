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

with open('student-count.csv', 'rb') as csvfile:
    inflowFile = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in inflowFile:
        unitid = row['"unitid"'].strip('"')
        qid = getQ(unitid)
        if qid is not "0":
            enrollment = row['"DRVEF2014.Total  enrollment"'].strip('"')
            if enrollment != "":
                enrollmentNum = int(enrollment)
                if enrollmentNum > 0:
                    enrollment = str(enrollmentNum)
                    print("Q" + qid + "\t" + "P2196" + "\t" + enrollment +
                          "\t" + "P585" + "\t" +
                          "+00000002014-09-01T00:00:00Z/10" + "\t" + "S248" +
                          "\t" + "Q6042926")
