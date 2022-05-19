#use transform functions like sorted, filter, map
from clearConsloe import *
clearConsole()

def filterFunc(x):
    if x % 2 == 0:
        return False
    return True

def filterFunc2(x):
    if x.isupper():
       return False
    return True

def squareFunc(x):
   return x ** 2

def toGrade(x):
    if (x>=90):
        return "A"
    if (x>=80 and x<90):
        return  "B"
    if (x>=70 and x<80):
        return  "C"
    if (x>=60 and x<70):
        return  "D"
    if (x>=50 and x<60):
        return  "E"
    if (x>=40 and x<50):
        return  "F"
       
def main():
   #define some sample sequences to operate on
        nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
        chars = "abcDeFGHiJklmnoP"
        grades = (81, 89, 94, 78, 61, 66, 99, 74) 
        #TODO: use filter to remove items fromalist
        odds = list(filter(filterFunc,nums))
        print(odds)
        print()
        #TODO: use filter on non-numeric sequence
        odds = list(filter(filterFunc2,chars))
        print(odds)
        print()
        #TODO: use map to createanew sequence of values
        squartes  =  list(map(squareFunc,grades))
        print(squartes)
        print()
        #TODO: use sorted and map to change numbers to grades
        grades = sorted(grades)
        letters = list(map(toGrade,grades))
        print(letters)
        
if __name__ == "__main__":
    main()