# Python3
# -*- coding: utf-8 -*-

# Autor: Ines Pisetta

import re

def filterByPrep(content):

	with open(content, "r", encoding = "utf-8") as t:
		contentList = t.readlines()
		
	resultList = []
	
	listOfAcceptablePrepositions = ["abseits", "am", "an", "ans", "auf", "aufs", "aus", "außerhalb", "beidseits", "beiderseits", "beim", "bis", "diesseits", "durch", "entgegen", "entlang", "fern", "fernab", "gegen", "gegenüber", "gen", "hinter", "hinterm", "hinters", "im", "in", "inmitten", "innerhalb", "ins", "jenseits", "lang", "längs", "längsseits", "links", "nach", "nördlich", "nordöstlich", "nordwestlich", "oberhalb", "östlich", "rechts", "seitlich", "seitwärts", "südlich", "südöstlich", "südwestlich", "über", "überm", "übern", "übers", "um", "ums", "unfern", "unter", "unterhalb", "unterm", "untern", "unters", "unweit", "via", "vom", "von", "vor", "vorbehaltlich", "wider", "zu", "zum", "zur", "zwischen"]
		
	for line in contentList:
		if re.match("^\w+\s\w+\s([A-Z]|Ä|Ö|Ü)\w+", line):
			m = re.match("^(\w+)\s(\w+)\s(\w+)", line)
			if m.group(2) in listOfAcceptablePrepositions:
				resultList.append(line)
			else:
				continue
					
	with open(str(content).split(".")[0] + "_filteredByPrep.txt", "w", encoding = "utf-8") as f:
		f.writelines(resultList)
		
if __name__ == "__main__":
	filterByPrep("Results_sorted.txt")
			