# telicity_analysis
A corpus-based analysis of telicity in German from summer 2016

This repository contains the code and results of an university project I worked on back in summer 2016.  
Goal of the project was to perform a statistical analysis regarding the telicity of certain German motion verbs.  
Database for the project was the corpus SDeWaC of [WaCky - The Web-As-Corpus Kool Initiative](https://wacky.sslmit.unibo.it/doku.php) (880 million tokens, annotated version 3; see M. Baroni, S. Bernardini, A. Ferraresi and E. Zanchetta. 2009. The WaCky Wide Web: A Collection of Very Large Linguistically Processed Web-Crawled Corpora. Language Resources and Evaluation 43 (3): 209-226.).  
The reasons for choosing SDeWaC were mainly the size of the corpus and existing annotations like POS-Tags, dependency and grammatical information.

## Approach
For 84 selected verb of motion all occurrences from SDeWaC have been extracted, where the verb has a dependent prepositional phrase in the same sentence. From there on, further steps have been taken to filter the results even more:
1. Keep only results that contained one of 68 selected prepositions
2. Remove results where the head of the prepositional phrase did not start with a capital letter
3. Remove results, where the head of the prepositional phrase belonged to a specific synset; considering the whole synset path from GermaNet

The results were calculated based on the remaining data. For that, my supervisor and I labelled the prepositions according to their telicity using three different labels (telic, atelic and unclear).  
Since the difference between atelic and unclear was hard to determine, the final results only contain results regarding the telicity ratio of the verbs (% of the contexts in which they occur that are actual telic).  
Aside from that, counts of the prepositions and their cases have been extracted for each verb.

## Structure
* code: contains all Python-Code used throughout the experiments; detailed information below
* counts: contains one CSV file for each verb, each listing the frequency of all (selected) prepositions together with the case of the noun (head of the prepositional phrase)
* material: contains the lists of the verbs that have been analyzed as well as the considered prepositions and the list of the unwanted synsets
* results: contains all results

## Code
1. extractVerbPrepNounCase.py - extracts all occurrences of the 84 selected verb of motion (see /material/Verbliste.txt) from SDeWaC that had a dependent prepositional phrase; extracted samples included: verb, preposition, noun (head of prepositional phrase), case of the noun, name of the file the sample has been taken from, ID of the verb (sentence ID and token position within the sentence)  
Output: Results.txt
2. sortAlphabeticallyResults.py - sorts the content of Results.txt alphabetically  
Output: Results\_sorted.txt
3. filterByPrep.py - filters the content of Results_sorted.txt, only keeping samples that contain any of the 68 selected prepositions (see /material/Präpositionsliste_labelled.txt); also remvoves results where the noun (head of the prepositional phrase) doesn't start with a capital letter  
Output: Results\_sorted\_filteredByPrep.txt
4. splitResultsByVerb.py - splits the content of Results_sorted_filteredByPrep.txt by verb, creating a separate text file for each verb  
Output: *verb*.txt
5. filterUnwantedNounsAll.py - filters the results in all verb files with respect to specific unwanted synsets (see /material/unwantedSynsets.txt); for each noun, the whole synset path in GermaNet is considered  
Output: *verb*\_filteredUnwantedNouns.txt
6. judgeAndExtract.py - uses the output files created in 5. to create several files (see /results) that contain information regarding the telicity of all the verbs; judging is performed based on the labelled prepositions (see /material/Präpositionsliste_labelled.txt); also covers some problematic cases where the case didn't match with the expectations (due to annotation errors in the corpus)  
Output: see /results: final\_results.csv, final\_results\_readable.txt, judgeProblems.txt, telicPercent.txt, telic.txt, atelic.txt, unclear.txt
7. sortResultsVerbPrep.py - uses the output files created in 5. to count the frequency of all prepositions together with all the cases for each verb; results are saved in one CSV file for each verb (see /counts)  
Output: see /counts: *verb*.csv

## License
The content of this project itself is licensed under the [Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/), and the underlying source code used to format and display that content is licensed under the [MIT license](https://github.com/inlpi/telicity_analysis/blob/master/LICENSE.md).  
I do not own any of the SDeWaC data. This repository only contains statistical evaluations of the SDeWaC data.  
For access to the SDeWaC data, see the website of [WaCky](https://wacky.sslmit.unibo.it/doku.php) (M. Baroni, S. Bernardini, A. Ferraresi and E. Zanchetta. 2009. The WaCky Wide Web: A Collection of Very Large Linguistically Processed Web-Crawled Corpora. Language Resources and Evaluation 43 (3): 209-226.).
