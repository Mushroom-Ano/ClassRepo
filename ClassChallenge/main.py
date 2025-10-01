from person import *
from graduate import *

def main():
    guy = Person("Jibril", "Abdul", 25)
    print(guy.get_last_name())
    print(guy._last_name) #Semi-protected, can be printed.
    #print(guy.__age) #Since age is private, can't be accessed. 


    grad = Graduate("Software Engineer", "Leeds", "John", "Doe", 25)
    grad.set_age(-1)
    print(grad._Graduate__location)
    grad.location = "Leeds"
    print(grad._Graduate__location)
    print(grad.location)
    #print(grad.__location)

if __name__ == "__main__" :
    main()