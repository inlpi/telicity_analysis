# Python3
# -*- coding: utf-8 -*-

# Autor: Ines Pisetta

import os

def sortAlphabetically(content):
	
	with open(content, "r", encoding = "utf-8") as t:
		contentList = t.readlines()
		
	with open(str(content).split(".")[0] + "_sorted.txt", "w", encoding = "utf-8") as f:
		f.writelines(sorted(contentList))
		
if __name__ == "__main__":
	currentPath = os.path.dirname(os.path.abspath( __file__ ))
	allFiles = os.listdir(currentPath)
	for file in allFiles:
		if (file.startswith("Results") and file.endswith("Results")):
			sortAlphabetically(file)
		else:
			pass