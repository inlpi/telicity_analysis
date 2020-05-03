# Python3
# -*- coding: utf-8 -*-

# Autor: Ines Pisetta

import re
import os, sys

# judgeAndExtract.py = extract.py
# Erweiterung von judge.py

# 41 als atelisch gelabelte Präpositionen
atelic = ["abseits", "am", "außerhalb", "beidseits", "beiderseits", "beim", "diesseits", "entgegen", "entlang", "fern", "fernab", "gegenüber", "gen", "hinterm", "im", "inmitten", "innerhalb", "jenseits", "lang", "längs", "längsseits", "links", "nördlich", "nordöstlich", "nordwestlich", "oberhalb", "östlich", "rechts", "seitlich", "seitwärts", "südlich", "südöstlich", "südwestlich", "überm", "unfern", "unterhalb", "unterm", "unweit", "via", "wider", "zwischen"]
# 16 als telisch gelabelte Präpositionen; "telisch" entfernt
telic = ["ans", "aufs", "aus", "bis", "gegen", "hinters", "ins", "nach", "ums", "untern", "unters", "vom", "von", "zu", "zum", "zur"]
# 5 als unklar gelabelte Präpositionen
unclear = ["durch", "über", "übern", "übers", "um"]
# 6 Präpositionen, die mit Akk. telisch sind und mit Dat. atelisch
telAtel = ["an", "auf", "hinter", "in", "unter", "vor"]

def judgeAndExtract(content):
    
    with open(content, "r", encoding = "utf-8") as t:
        contentList = t.readlines()
    
    atelicCounter = 0
    telicCounter = 0
    unclearCounter = 0
    
    verb = content.split("_")[0]
    
    error1Counter = 0
    error2Counter = 0
    
    error1List = []
    error2List = []
    
    telicList = []
    atelicList = []
    unclearList = []
    
    for line in contentList:
        line = line[:-2]
        lineList = line.split()
        if lineList[1] in atelic:
            atelicCounter += 1
            atelicList.append(line)
            atelicList.append("\n")
        elif lineList[1] in telic:
            telicCounter += 1
            telicList.append(line)
            telicList.append("\n")
        elif lineList[1] in unclear:
            unclearCounter += 1
            unclearList.append(line)
            unclearList.append("\n")
        elif lineList[1] in telAtel:
            if lineList[3] == "acc":
                telicCounter += 1
                telicList.append(line)
                telicList.append("\n")
            elif lineList[3] == "dat":
                atelicCounter += 1
                atelicList.append(line)
                atelicList.append("\n")
            else:
                error1Counter += 1
                error1List.append(line + "\n")
        else:
            error2Counter += 1
            error2List.append(line + "\n")
            
    total = atelicCounter + telicCounter + unclearCounter
    atelicPercent = atelicCounter/total*100
    telicPercent = telicCounter/total*100
    unclearPercent = unclearCounter/total*100
    
    # ehem. "judgeResults.txt"
    with open("final_results_readable.txt", "a", encoding = "utf-8") as f:
        f.write(verb + " ist zu" + "\n" + str(telicPercent) + "% telisch" + "\n" + str(atelicPercent) + "% atelisch" + "\n" + str(unclearPercent) + "% unklar" + "\n\n")
        f.write("absolute Zahlen:\nSumme der Vorkommen: " + str(total) + "\ntelisch: " + str(telicCounter) + "\natelisch: " + str(atelicCounter) + "\nunclear: " + str(unclearCounter) + "\n\n\n")
        #f.write(str(error1Counter) + "\n" + str(error2Counter) + "\n\n")
    
    with open("final_results.csv", "a", encoding = "utf-8") as fr:
        fr.write(verb + ", " + str(total) + ", " + str(telicCounter) + ", " + str(atelicCounter) + ", " + str(unclearCounter) + "\n")
        
    with open("judgeProblems.txt", "a", encoding = "utf-8") as g:
        g.write(verb + " hat" + "\n" + str(error1Counter) + " Fälle von 'an', 'auf', 'hinter', 'in', 'unter' oder 'vor', die weder mit Akk. noch mit Dat. vorkommen" + "\n" + str(error2Counter) + " Fälle, die nicht von der Präpositionsliste abgedeckt werden" + "\n")
        g.write("\n")
        g.writelines(error1List)
        g.write("\n")
        g.writelines(error2List)
        g.write("\n\n")
        
    with open("telicPercent.txt", "a", encoding = "utf-8") as h:
        h.write(verb + " " + str(telicPercent))
        h.write("\n")
    
    telicFile = "telic.txt"
    atelicFile = "atelic.txt"
    unclearFile = "unclear.txt"
    
    with open(telicFile, "a", encoding = "utf-8") as m:
        m.writelines(telicList)
        m.write("\n\n")
        
    with open(atelicFile, "a", encoding = "utf-8") as n:
        n.writelines(atelicList)
        n.write("\n\n")
        
    with open(unclearFile, "a", encoding = "utf-8") as o:
        o.writelines(unclearList)
        o.write("\n\n")
        
    print(str(content) + " fertig") 
    
if __name__ == "__main__":
    currentPath = os.path.dirname(os.path.abspath( __file__ ))
    allFiles = os.listdir(currentPath)
    f = open("final_results_readable.txt", "w", encoding = "utf-8")
    f.close()
    with open("final_results.csv", "w", encoding = "utf-8") as fr:
        fr.write("Verb, Anzahl Vorkommen gesamt, Anzahl Vorkommen telisch, Anzahl Vorkommen atelisch, Anzahl Vorkommen unklar\n")
    g = open("judgeProblems.txt", "w", encoding = "utf-8")
    g.close()
    h = open("telicPercent.txt", "w", encoding = "utf-8")
    h.close()
    m = open("telic.txt", "w", encoding = "utf-8")
    m.close()
    n = open("atelic.txt", "w", encoding = "utf-8")
    n.close()
    o = open("unclear.txt", "w", encoding = "utf-8")
    o.close()
    for file in allFiles:
        if "filteredUnwantedNouns" in file:
            judgeAndExtract(file)
        else:
            pass