#Use lambdas as in-place functions
from clearConsloe import *
clearConsole()

def CelsisusToFahrenheit (temp):
    return (temp*9/5)+32

def FahrenheitTocelsisus(temp):
    return (temp-32)*5/9

def main():
    ctemps=[0, 12, 34, 100]
    ftemps=[32, 65, 100, 212]
  
       
    #TODO: Use regular functions to convert temps
    print(list(map(FahrenheitTocelsisus , ftemps)))
    print(list(map(CelsisusToFahrenheit , ctemps)))
    print()
   
    
    
    
    #TODO: Use and
    print(list(map(lambda t: (t-32)*5/9 , ftemps)))
    print(list(map(lambda t: (t*9/5)+32 , ctemps)))
    print()
    
    
   
   
   
      
if __name__ == "__main__":
    main()