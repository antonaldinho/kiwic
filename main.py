from ShifterFactory import Creator, CircularShifterCreator
from Input import Input
from SorterFactory import SorterCreator, AscendingSortCreator, DescendingSortCreator
from Output import Output

def client_code(creator: Creator, entrada, sorter: SorterCreator) -> str:
    print("Client: I'm not aware of the creator's class, but it still works.")
    #print(creator.some_operation(entrada))
    sentences = creator.some_operation(entrada)
    sortedSentences = sorter.some_operation(sentences)
    print(sortedSentences)
    return sortedSentences
    


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    filename = 'KWIC2_input1.txt'
    stopBool = input("Do you want to use stop words (S/N) \n")
    if  stopBool == 'S' or stopBool == 's':
        stopFile = input("Type the stopwords file name \n")
        inp = Input().process(filename, stopFile)
    else: 
        inp = Input().process(filename)
    sortType = input("Do you want the sort to be ascending (A) or descending (D)\n")
    if sortType == 'A' or sortType == 'a':
        sentences = client_code(CircularShifterCreator(), inp, AscendingSortCreator())
    else:
        sentences = client_code(CircularShifterCreator(), inp, DescendingSortCreator())
    Output().output(sentences)
    print("\n")