# Python3
# -*- coding: utf-8 -*-

# Autor: Ines Pisetta

# Modifikation von sortResultsVerbPrep.py, zusammen mit sortByNumberVerbs.py und Unterscheidung des Kasus für jede Präposition

import os
import re
import collections

def sortResultsVerbPrep(results):
    
    with open(results, "r", encoding = "utf-8") as t:
        resultList = t.readlines()
        
    prepCaseDict = {}
    
    # Iterieren über jede Zeile der Ergebnisdatei. Eine Zeile enthält Verb, Präposition, Nomen und Kasus
    for line in resultList:
        lineList = line.split()
        prep = lineList[1]
        case = lineList[3]
        # Wenn es die Präposition schon im Dictionary gibt, wird nur der Kasus zur Value-Liste hinzugefügt
        if prep in prepCaseDict:
            if case == "acc":
                prepCaseDict[prep][0] += 1
            elif case == "dat":
                prepCaseDict[prep][1] += 1
            elif case == "gen":
                prepCaseDict[prep][2] += 1
            elif case == "nom":
                prepCaseDict[prep][3] += 1
            else:
                prepCaseDict[prep][4] += 1
        
        # Falls nicht, wird außerdem noch ein entsprechender Key erstellt
        else:
            prepCaseDict[prep] = [0,0,0,0,0]
            if case == "acc":
                prepCaseDict[prep][0] += 1
            elif case == "dat":
                prepCaseDict[prep][1] += 1
            elif case == "gen":
                prepCaseDict[prep][2] += 1
            elif case == "nom":
                prepCaseDict[prep][3] += 1
            else:
                prepCaseDict[prep][4] += 1
    
    # Ein Dictionary-Eintrag enthält die Präposition als Key und eine Liste der Frequenzen aller Kasus als Value
    fileName = "counts/" + results.split("_")[0] + ".csv"
    with open(fileName, "w", encoding = "utf-8") as f:
        f.write("Präposition, Gesamt, Akk., Dat., Gen., Nom., Unbekannt\n")
        for prep, cases in sorted(prepCaseDict.items(),key=lambda i:sum(i[1]),reverse=True):
            f.write(prep + ", " + str(sum(cases)) + ", " + str(cases[0]) + ", " + str(cases[1]) + ", " + str(cases[2]) + ", " + str(cases[3]) + ", " + str(cases[4]) + "\n")

    
if __name__ == "__main__":
    # Wende die Funktion auf alle Dateien im aktuellen Pfad an
    currentPath = os.path.dirname(os.path.abspath( __file__ ))
    allFiles = os.listdir(currentPath)
    for file in allFiles:
        if "_filteredUnwantedNouns" in file:
            sortResultsVerbPrep(file)
