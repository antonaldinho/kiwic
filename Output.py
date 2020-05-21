class Output():

    def output (self, sentences):
        file1 = open("sorted.txt", "w")
    
        for i in sentences:
            print(i)
            a = [*i]
            for j in a:
                file1.write(j)
            file1.write("\n")
        file1.close()  
                
                
            
    # '''
    # input:

    # [[Clouds are white], [white are clouds], [Pittsburg is beautiful], [beautiful is Pittsburg]]

    # '''

    # l = []
    # a = ["Clouds", "are", "white" ]
    # b = [ "are", "white", "Clouds"]
    # c = [ "Pittsburg", "is", "beautiful"]
    # d = [ "beautiful", "is", "Pittsburg"]

    # l.append(a)
    # l.append(b)
    # l.append(c)
    # l.append(d)
    # output(l)

    # '''
    # output:

    # Clouds  are white 
    # white are clouds 
    # Pittsburg is beautiful
    # beautiful is Pittsburg
    # '''