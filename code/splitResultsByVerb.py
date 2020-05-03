# Python3
# -*- coding: utf-8 -*-

# Autor: Ines Pisetta

import re

def splitResultsVerbPrep(results):
	
	with open(results, "r", encoding = "utf-8") as t:
		resultList = t.readlines()
		
	verbPrepDict = {}
	
	# Iterieren über jede Zeile der Ergebnisdatei. Eine Zeile enthält Verb, Präposition, Nomen und Kasus
	for line in resultList:
		lineList = line.split()
		# Wenn es das Verb schon im Dictionary gibt, wird nur die Präposition zur Value-Liste hinzugefügt
		if lineList[0] in verbPrepDict:
			continue
		# Falls nicht, wird außerdem noch ein entsprechender Key erstellt
		else:
			verbPrepDict[lineList[0]] = []
	
	# Ein Dictionary-Eintrag enthält das Verb als Key und eine Liste von allen vorkommenden Präpositionen als Value
	# Da es sich um eine Liste handelt, werden auch Mehrfachvorkommen mitgezählt
	# Dies nutzt man aus, um mit "counter" eine Zählung zu machen und diese als Output in die Datei zu schreiben
	# Beispieloutput z.B. für Datei "gehen.txt" (Newlines anstelle von Kommas): in 3, auf 1, usw.
	for verb, preps in verbPrepDict.items():		
		fileName = verb + ".txt"
		with open(fileName, "w", encoding = "utf-8") as f:
			for line in resultList:
				if line.startswith(verb):
					f.write(line)
	
if __name__ == "__main__":
	splitResultsVerbPrep("Results_sorted_filteredByPrep.txt")