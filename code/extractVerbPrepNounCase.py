# Python3
# -*- coding: utf-8 -*-

# Autor: Ines Pisetta

import re
import os, sys

def extractVerbPrepNounCase(corpus):
	
	with open(corpus, "r", encoding = "utf-8") as t:
		corpusList = t.readlines()
		
	verbList = ["bummeln", "eiern", "eilen", "fahren", "flanieren", "flattern", "fliegen", "fliehen", "fließen", "flitzen", "galoppieren", "gehen", "gleiten", "hasten", "hetzen", "hinken", "hoppeln", "hopsen", "humpeln", "hüpfen", "huschen", "joggen", "klettern", "krabbeln", "kriechen", "kullern", "latschen", "laufen", "marschieren", "pilgern", "promenieren", "purzeln", "radeln", "rasen", "reisen", "reiten", "rennen", "robben", "rollen", "rudern", "rutschen", "sausen", "schlappen", "schleichen", "schlendern", "schlurfen", "schreiten", "schwanken", "schweben", "schweifen", "schwimmen", "segeln", "sinken", "skaten", "spazieren", "springen", "sprinten", "stapfen", "steigen", "stolpern", "stolzieren", "streichen", "streifen", "streunen", "strömen", "stromern", "stürmen", "tapsen", "tauchen", "taumeln", "tigern", "tippeln", "torkeln", "traben", "trampeln", "treiben", "trippeln", "trotten", "wandeln", "wandern", "wanken", "watscheln", "wieseln", "ziehen"]

	sentenceList = []
	tempSentenceList = []
	
	# zusammenfügen der Wörter eines Satzes, sodass das Korpus als Liste von Sätzen verarbeitet werden kann
	for word in corpusList:
	
		if word == "\n":
			sentenceList.append("".join(tempSentenceList))
			del tempSentenceList[:]
			
		else:
			tempSentenceList.append(word)
			
	resultList = []
	
	for sentence in sentenceList:
		
		sentenceInternListWithNewline = sentence.split("\n")
		sentenceInternList = []
		
		# Ausschließen der Newline-Elemente
		for el in sentenceInternListWithNewline:
			if el == "":
				pass
			else:
				sentenceInternList.append(el)
				
		idsOfMatchedVerbs = []
		idOfVerbAndSentence = []
		
		# Überprüfen, ob ein Verb im Satz vorkommt
		# Extrahieren der IDs der Verben (werden als verbDict Keys verwendet)
		for parse in sentenceInternList:
			if "VV" in parse:
				parseList = parse.split("\t")
				if parseList[3] in verbList:
					idsOfMatchedVerbs.append(int(parseList[0].split("_")[1]))
					idOfVerbAndSentence.append(int(parseList[0].split("_")[1]))
		
		# Dictionary mit den VerbIDs als Keys und den zugehörigen Verben als Values
		verbDict = dict.fromkeys(idsOfMatchedVerbs, "")
		
		# Dictionary mit den VerbIDs als Keys und den IDs der Präpositionen als String, wobei die einzelnen IDs (bei mehreren Präpositionen) durch Leerzeichen getrennt sind
		idDictionaryNonStripped = dict.fromkeys(idsOfMatchedVerbs, "")
		
		idOfVerbAndSentenceDict = dict.fromkeys(idOfVerbAndSentence, "")
		
		# Überprüfen, ob ein Verb im Satz vorkommt
		# Zuordnen des Verbs zu seiner ID im Dicitonary
		for parse in sentenceInternList:
			if "VV" in parse:
				parseList = parse.split("\t")
				idKey = int(parseList[0].split("_")[1])
				if idKey in verbDict:
					verbDict[idKey] += parseList[3]
					idOfVerbAndSentenceDict[idKey] += parseList[0]

		# Dictionary mit den IDs der Präpositionen als Keys und den zugehörigen Präpositionen als Values
		prepIDprepDict = {}
		
		# Überprüfen, ob es Präpositionen gibt, die auf das Verb zeigen
		# Extrahieren der Präpositionen und ihrer IDs
		for parse in sentenceInternList:
			if "APPR" in parse:
				parseList = parse.split("\t")
				if int(parseList[9]) in verbDict:
					# ID der Präposition wird dem ID-Dictionary hinzugefügt
					idDictionaryNonStripped[int(parseList[9])] += " " + parseList[0].split("_")[1]
					# Präposition wird dem Präpositions-Dictionary hinzugefügt
					prepIDprepDict[int(parseList[0].split("_")[1])] = parseList[3]
		
		# überflüssige Leerzeichen werden entfernt
		idDictionary = {key:value.strip() for key, value in idDictionaryNonStripped.items()}
		
		# Umkehren des ID-Dictionarys, um auf die IDs der Präpositionen zugreifen zu können
		# Vorteil: Dieses Dictionary enthält nur die IDs von Verben (in den Values), auf die sich auch Präpositionen beziehen
		reverseIdDictionary = {int(v):k for k, values in idDictionary.items() for v in values.split() if not v == ""}
		
		# Kopie des umgekehrten ID-Dictionarys - ID des Verbs wird hier im Verlauf durch das zur Präposition gehörige Nomen ersetzt
		# das umgekehrte ID-Dictionary bleibt unberührt
		prepDict = dict(reverseIdDictionary)
		
		# Überprüfen, ob es Nomen gibt, die auf das Verb zeigen
		# Extrahieren der Nomen und ihrer Fälle
		for parse in sentenceInternList:
			if "NN" in parse:
				parseList = parse.split("\t")
				if parseList[9] ==  "_":
					pass
				elif int(parseList[9]) in reverseIdDictionary:
					prepDict[int(parseList[9])] = parseList[3]
					prepDict[int(parseList[9])] += " " + parseList[7].split("|")[0]
		
		# Iterieren über die Präpositionen, weil ein Iterieren über die Verben ungünstig ist, da ein Verb mehrere Präpositionen haben kann und man aber jeden Fall einzeln haben will
		# Vorteil: Verben ohne Präpositionen werden gar nicht beachtet
		for prepID in prepDict:
				
			# Ausschließen von den Präpositionen, bei denen kein Nomen steht
			if type(prepDict[prepID]) is int:
				pass
			
			# Beispielergebnis: gehen in Haus acc
			else:
				result = verbDict[reverseIdDictionary[prepID]]
				result += " " + prepIDprepDict[prepID]
				result += " " + prepDict[prepID]
				result += " " + str(corpus)
				result += " " + idOfVerbAndSentenceDict[reverseIdDictionary[prepID]]
				resultList.append(result + "\n")
	
	# Ergebnisse werden in Ergebnisdatei geschrieben; falls keine existiert, wird eine erstellt; falls sie schon Inhalt hat, wird dieser nicht überschrieben
	# a ermöglicht, dass alle Ergebnisse (aus verschiedenen Programmdurchläufen) in eine Ergebnisdatei geschrieben werden können
	with open("Results.txt", "a", encoding = "utf-8") as f:
		f.writelines(resultList)
		
	print(str(corpus) + " fertig")
		
if __name__ == "__main__":
	currentPath = os.path.dirname(os.path.abspath( __file__ ))
	allFiles = os.listdir(currentPath)
	for file in allFiles:
		if file[0].isalpha():
			pass
		else:
			extractVerbPrepNounCase(file)