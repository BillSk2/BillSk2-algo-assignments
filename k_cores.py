import sys
import pprint

pat=sys.argv[1]
graph={}
#Ανοιγμα αρχείου και δημιουργία γράφου
with open(pat) as input_file:
	#Για καθε γραμμη του αρχειου
    for line in input_file:
        #Για καθε μερος της γραμμης
        parts=line.split()
        [n1, n2] = [x for x in parts] 
        #Λιστα γειτνιασης αρχικοποιηση
        if n1 not in graph:
            graph[n1] = []
        #Λιστα γειτνιασης αρχικοποιηση
        if n2 not in graph:
            graph[n2] = [] 	
	graph[n1].append(n2) 
	graph[n2].append(n1)

#Ελεγχος αρχικοποιησης γραφου
pprint.pprint(graph)