import re
import csv

class Input():
    
    def process(*args):
        if len(args) == 4 and isinstance(args[1], str) and isinstance(args[2], str) and isinstance(args[3], list):
            file = open(args[2], "r")
            stopWords = []
            for w in file:
                word = re.sub(r'\W+', '', w)
                stopWords.append(word)
            contador = 1
            f = open(args[1], "r")
            words = []
            for x in f:
                print(contador)
                if not contador in args[3]:
                    proc = re.sub(r'\W+', ' ', x)
                    notFiltered = proc.lower().split()
                    line = ""
                    for item in notFiltered:
                        line+= item + " "
                    print(line)
                    filtered = [x for x in notFiltered if x not in stopWords]
                    words.append(filtered)
                else:
                    contador+= 1
            return words
    
        elif len(args) == 3 and isinstance(args[1], str) and isinstance(args[2], str):
            file = open(args[2], "r")
            stopWords = []
            for w in file:
                word = re.sub(r'\W+', '', w)
                stopWords.append(word)
            
            f = open(args[1], "r")
            words = []
            for x in f:
                proc = re.sub(r'\W+', ' ', x)
                notFiltered = proc.lower().split()
                filtered = [x for x in notFiltered if x not in stopWords]
                words.append(filtered)
            return words
        
            
        elif len(args) == 2 and isinstance(args[1], str):
            f = open(args[1], "r")
            words = []
            for x in f:
                proc = re.sub(r'\W+', ' ', x)
                words.append(proc.lower().split())
            return words
    
    
    