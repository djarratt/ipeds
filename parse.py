# -*- coding: iso-8859-15 -*-
import csv, json

with open('wikidata_query_result.json', 'rb') as f:
    data = json.loads(f.read())
    crosswalk = data["props"]["1771"]
    
def getQ(unitid):
    for i in crosswalk:
        if unitid == i[2]:
            return str(i[0])
    return "0"

with open('Qreligion.json', 'rb') as infile:
    Qreligions = json.loads(infile.read())

with open('religion.csv', 'rb') as csvfile:
    inflowFile = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in inflowFile:
        name = row['"institution name"'].strip('"')
        unitid = row['"unitid"'].strip('"')
        qid = getQ(unitid)
        if qid is not "0":
            religion = row['"IC2014.Religious affiliation"'].strip('"')
            if religion in Qreligions:
                Qreligion = Qreligions[religion]
                if Qreligion is not -1:
                    print("Q" + qid + "\t" + "P140" + "\t" + Qreligion + "\t" + "S248" + "\t" + "Q6042926")