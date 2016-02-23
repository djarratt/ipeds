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
    
def findDelimiter(string):
    possibilities = ["|", ";", ":", "/", "\\", "„"]
    for p in possibilities:
        if p in string:
            return p
    return "none"
    
def trim(string):
    toOmit = ["formerly", "(former name)", "dba", "DBA", "Formerly"]
    for o in toOmit:
        string.strip(o)
    return string.strip()

with open('aliases.csv', 'rb') as csvfile:
    inflowFile = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in inflowFile:
        name = row['"institution name"'].strip('"')
        unitid = row['"unitid"'].strip('"')
        qid = getQ(unitid)
        if qid is not "0":
            aliases = row['"HD2014.Institution name alias"'].strip('"')
            if aliases is not "":
                delimiter = findDelimiter(aliases)
                if delimiter == "none":
                    aliasList = [aliases]
                else:
                    aliasList = aliases.split(delimiter)
                for alias in aliasList:
                    alias = trim(alias)
                    if alias is not "": 
                        secondDelim = findDelimiter(alias)
                        if secondDelim == "none" and len(alias) > 1:
                            alias = alias[0].capitalize() + alias[1:]
                            print("Q" + qid + "\t" + "Aen" + "\t" + alias)
                        else:
                            theresMore = alias.split(secondDelim)
                            for m in theresMore:
                                m = trim(m)
                                if len(m) > 1:
                                    m = m[0].capitalize() + m[1:]
                                    print("Q" + qid + "\t" + "Aen" + "\t" + m)
                
#"S248" + "\t" + "Q6042926")

# at end go through and look at longest strings to manually check