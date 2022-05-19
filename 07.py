#advanced iteration functions in the itertools package
from clearConsloe import * 
clearConsole()
import itertools

def testFunction(x):
    return x < 40 

def main():
    #TODO: cycle iterator can be used to cycle overacollection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print()
    #TODO: use count to createasimple counter
    count1 = itertools.count(100,10)
    print(next(count1))
    print(next(count1))
    print(next(count1))    
    print(next(count1))
    print()

    #TODO: accumulate creates an iterator that accumulates values
    vals=[10,20,30,40,50,40,30]
    acc = itertools.accumulate(vals, max)
    print(list(acc))
    print()
    #TODO: use chain to connect sequences together
    x = itertools.chain("ABCD","1234")
    print(list(x))
    print()
    
    
    #TODO: dropwhile and takewhile will return values until
    print(list(itertools.dropwhile(testFunction,vals)))
    print(list(itertools.takewhile(testFunction,vals)))
    print()
    
    #acertain condition that stops them
    
if __name__ == "__main__":
    main()