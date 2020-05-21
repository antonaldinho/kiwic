import re
import csv



#example1 =  '''
#            "Clouds are white."
#            "Pittsburgh is beautiful."
#            '''

#example2 = '''
#            """Clouds,are,white."""
#            """Pittsburg,is,beautiful."""
#            '''


class Input():
    
    def process(self, fileString, stopFile):
        file = open(stopFile, "r")
        stopWords = []
        for w in file:
            word = re.sub(r'\W+', '', w)
            stopWords.append(word)
        if '.txt' in fileString:
            return self.txtFile(fileString, stopWords)
        elif '.csv' in fileString:
            return self.csvFile(fileString, stopWords)
        else:
            print('Formato de archivo no soportado')

    def txtFile(self, filename, stopWords):
        f = open(filename, "r")
        words = []
        for x in f:
            proc = re.sub(r'\W+', ' ', x)
            notFiltered = proc.lower().split()
            filtered = [x for x in notFiltered if x not in stopWords]
            words.append(filtered)
        return words

    def csvFile(self, filename):
        f = open(filename)
        csv_f = csv.reader(f)
        words = []
        finalWords = []
        for row in csv_f:
            proc = row[0].split(',')
            for i in proc:
                word = re.sub(r'\W+', '', i).lower()
                words.append(word)
            finalWords.append(words)
            words = []
        return finalWords
    

    