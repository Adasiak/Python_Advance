#Demonstrate the use of function docstrings


from ast import arg
from clearConsloe import *
clearConsole()

def myFunction(arg1, arg2=None):
    """"" myFunction(arg1 , arg2=None) 
    
    Parameters:
    arg1: the first argument. Whatever you f`eel like passing.
    arg2: second argument. Defaults to None.`
    """""
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)
    print("kasia")

if  __name__ == "__main__":
  main()