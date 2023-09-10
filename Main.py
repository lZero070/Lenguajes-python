from functools import reduce
import time
from Alphabet import Alphabets
from language import Language

alphabets = []
languages = []

def create_alphabets(quantity):
    print("In this program, the empty element is represented as #")
    for i in range(quantity):
        symbols = input(f"Enter the symbols for alphabet {i+1} separated by commas: ").split(",")
        alphabet = Alphabets(symbols)
        alphabets.append(alphabet) #
    print(f"{quantity} alphabets have been created.")
    
def show_alphabets():    
    for i, alphabet in enumerate(alphabets):#
        print(f"Alfabet {i+1}: {alphabet.get()}")
        
def show_languages():    
    for i, language in enumerate(languages):
        print(f"Lenguaje {i+1}: {language.get()}")

#ingreso
quantity_alphabets = int(input("Please enter the number of alphabets to create (minimum two): "))
if quantity_alphabets < 2:
    print("Remember that the minimum number of alphabets is two. Please choose another quantity.")
else:
    create_alphabets(quantity_alphabets)   
    show_alphabets()
    input("Press the ENTER key to continue...")

def options(object, message):
    global selected
    aux = False
    while not aux:
        election = input(f"Enter the numbers of the {message} separated by commas (1-{len(object)}): ")
        numbers = [int(option) for option in election.split(",")]
        if len(numbers) <= 1:
            print(f"You must choose at least two {message}.")
            continue
        aux = True
        for number in numbers:
            if number < 1 or number > len(object):
                print(f"The number {number} is not valid. You can only choose numbers between 1 and {len(object)}.")
                aux = False
                break;
    if aux:
        selected = [object[number-1] for number in numbers]

#union
if len(alphabets) == 0:#
    print("You must first create the alphabets.")
else: 
    print("Which alphabets do you want to unite?")
    show_alphabets()
    options(alphabets, "alphabets")#
    union = reduce(lambda a, b: a.union(b), selected)
    print("The union of the selected alphabets is:")
    print(union.get())
    input("Press the ENTER key to continue...")

#diferencia
if len(alphabets) == 0:
    print("You must first create the alphabets.")
else: 
    print("What alphabets do you want the difference?")
    show_alphabets()
    options(alphabets, "alphabets")
    difference = reduce(lambda a, b: a.difference(b), selected)
    print("The difference of the selected alphabets is:")
    print(difference.get())
    input("Press the ENTER key to continue...")   

#Intercepcion
if len(alphabets) == 0:
    print("You must first create the alphabets.")
else: 
    print("What alphabets do you want the interception")
    show_alphabets()
    options(alphabets, "alphabets")
    intersection = reduce(lambda a, b: a.intersection(b), selected)
    print("The interception of the selected alphabets is:")
    print(intersection.get())
    input("Press the ENTER key to continue...")   