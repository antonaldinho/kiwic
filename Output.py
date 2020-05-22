class Output():
    # Usuario decide las lineas que quiere borrar    
    def choose(self):
        array = list()
        n = 0
        while n != 'd':
            n = input("enter the number of line you don't want in input\n When you are done type d\n")
            if n != 'd' or not isinstance(n, str):
                array.append(int(n)) 
        return array
    
    
    def output (self, sentences):  
        print("lineas leidas",len(sentences),"\n")
        r = input("Do you want to choose lines to delete? (y/n\n")
        if r == 'n':
            file1 = open("sorted.txt", "w")
            for i in sentences:
                print(i)
                a = [*i]
                for j in a:
                    file1.write(j + "")
                file1.write("\n")
            file1.close() 
        
#Se quiere borrar las lineas
        else:
            a = self.choose()
            for y in reversed(a):
                copy = sentences
                del copy[y-1]
                for i in copy:
                    a = [*i]
            file2 = open ("sortedOut.txt", "w")
            for j in copy:
                print(j)
                for b in j:
                    file2.write(b + "")
                file2.write("\n")
            file2.close() 
    
                
                
