import re
import csv

class Input():
    
    def process(self, *args):
        #Imprime lineas, pregunta si quiere borrar lineas
        if len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], str):
            file = open(args[1], "r")
            stopWords = []
            for w in file:
                word = re.sub(r'\W+', '', w)
                stopWords.append(word)

            contador = 1
            f = open(args[0], "r")
            words = []
            notFiltered = self.process(args[0])
            line = ""
            for item in notFiltered:
                for ele in item:
                    line += ele + " "
                print(str(contador) + " - " + line)
                line= ""
                contador += 1
            input_string = input("Write the line numbers to remove, separated by a comma.Hit enter when you finished:\n")
            unwantedLines = input_string.replace(" "," ").split(",")
            
            con = 1
            for sentence in notFiltered:
                if not str(con) in unwantedLines:
                    filtered = [x for x in sentence if x not in stopWords]
                    words.append(filtered)
                    print(con)
                con = con + 1
            return words
        
        #No toma en cuenta stopWords    
        elif len(args) == 1 and isinstance(args[0], str):
            f = open(args[0], "r")
            words = []
            for x in f:
                proc = re.sub(r'\W+', ' ', x)
                words.append(proc.lower().split())
            return words
        
        else:
            print("No hay suficiente informacion para procesar")

        #Quita stopWords
        '''elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], str):
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
        '''
        
        
    
    
    