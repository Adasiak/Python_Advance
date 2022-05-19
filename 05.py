#use iterator functions like enumerate, zip, iter, next
from clearConsloe import *
clearConsole()
def main():
    #definealist of days in English and French

    days=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr=["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    #TODO: use iter to create an iterator overacollection
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))
    
    #TODO: iterate usingafunction andasentinel
    with open("text.txt" , "r") as fp:
        for line in iter(fp.readline ,''):
            print(line)
    print()
    #TODO: use regular interation over the days
    for day in range(len(days)):
        print(day +1, days[day])
    
    print()
    #TODO: using enumerate reduces code and providesacounter
    for i , m in enumerate(days , start=1):
        print(i,m)
    print()
    #TODO: use zip to combine sequences
    for n in zip(days, daysFr):
        print(n)
    print()
    for q,wm in enumerate(zip(days,daysFr),start = 1):
        print(q , wm[0] , "=" , wm[1] ,"in freach")
        

if __name__ == "__main__":
   main()