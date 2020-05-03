# Python3
# -*- coding: utf-8 -*-

# Autor: Ines Pisetta

import nltk
import re
import os
import sys
sys.path.append("C:\\Users\\Ines\\Documents\\Uni\\Projekt_Verbsemantik\\pygermanet-master\\pygermanet")
import germanet
gn = germanet.load_germanet()
from time import sleep
from tqdm import tqdm

def filterUnwantedNounsAll(content):

	with open(content, "r", encoding = "utf-8") as t:
		contentList = t.readlines()
		
	resultList = []
	
	unwantedSynsets = ["Zeiteinheit", "Zeitpunkt", "Wetter", "Temperatur", "Naturereignis", "Grad", "Uhr", "kognitiver Prozess", "Körperteil", "Körperregion", "Handlung", "Prozent"]
	
	for line in tqdm(contentList):
		m = re.match("^(\w+)\s(\w+)\s(\S+)", line)
		synsetsNoun = gn.synsets(m.group(3))
		if len(synsetsNoun) == 0:
			if "tag" in m.group(3):
				continue
			else:
				resultList.append(line)
		else:
			synsetList = []
			for synset in synsetsNoun:
				synsetList.append(synset.hypernym_paths)
			synsetHyperString = str(synsetList)
			if any(x in synsetHyperString for x in unwantedSynsets):
				continue
			else:
				resultList.append(line)
				continue
	with open(str(content).split(".")[0] + "_filteredUnwantedNouns.txt", "w", encoding = "utf-8") as f:
		f.writelines(resultList)
		
if __name__ == "__main__":
	currentPath = os.path.dirname(os.path.abspath( __file__ ))
	allFiles = os.listdir(currentPath)
	for file in allFiles:
		if (file.startswith("split") or file.startswith("filter") or file.startswith("Results") or file.endswith("_filteredUnwantedNouns.txt")):
			pass
		else:
			filterUnwantedNounsAll(file)
			print(file + " done")