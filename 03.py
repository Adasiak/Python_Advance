#demonstrate template string functions
from turtle import title
from clearConsloe import *
from string import Template

def main():
    #Usual st`ring formatting with format()
    str1= "You' re watching {0} by {1}".format("Advanced Python", "Joe Marini")
    print(str1)
    
    #TODO: createatemplate with placeholders
    templ = Template("You're watching ${title} by ${author}")
    
    #TODO: use the substitute method with keyword arguments
    str2 =  templ.substitute(title="Advance", author = "Wiktor")
    print(str2)    
    
    #TODO: us`e the substitute method withadictionary
    data =  {
        "author" : "Adasiak", 
        "title" : "Advance"
    }

    str3 =  templ.substitute(data)
    print(str3)
if __name__ == "__main__":
  main()