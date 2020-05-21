from ShifterFactory import Creator, CircularShifterCreator
from Input import Input
from SorterFactory import SorterCreator, AscendingSortCreator
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
    inp = Input().process('ex1.txt')
    sentences = client_code(CircularShifterCreator(), inp, AscendingSortCreator())
    Output().output(sentences)
    print("\n")