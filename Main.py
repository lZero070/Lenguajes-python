from functools import reduce

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


def options_2():
    global alphabet_selected_2
    aux = True
    while aux:
        selection = input(f"Enter the numbers of two alphabets separated by commas to use for the creation of the two corresponding languages (1-{len(alphabets)}): ")
        numbers = [int(option) for option in selection.split(",")]
        if len(numbers) <= 1 or len(numbers) > 2:
            print("You must choose two alphabets.")
            continue
        valid = True
        for number in numbers:
            if number < 1 or number > len(alphabets):
                print(f"The number {number} is not valid. You can only choose numbers between 1 and {len(alphabets)}.")
                valid = False
                break;       
        if valid:
            alphabet_selected_2 = [alphabets[number-1] for number in numbers]
            break;


def creationLanguages():
    l1 = Language([])
    l2 = Language([])
    show_alphabets()
    options_2()
    quantity_l1 = int(input("Enter the number of words you want the first language to contain: "))
    quantity_l2 = int(input("Enter the number of words you want the second language to contain: "))
    l1.generate([alphabet_selected_2[0]], quantity_l1)
    l2.generate([alphabet_selected_2[1]], quantity_l2)
    languages.append(l1)
    languages.append(l2)
    show_languages()
    print(f"Both languages have been successfully created.")

print("\n")

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

print("\n")
#difference
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

print("\n")
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
    input("Press the ENTER key to continue.")

print("\n")
#Cerradure estrella
if len(alphabets) == 0:
    print("You must first create the alphabets.")
else: 
    print("From which alphabet would you like the star lock?")
    show_alphabets()
    option = int(input(f"Enter the alphabet number between 1 and {len(alphabets)}: "))
    while option < 1 or option > len(alphabets):
        print(f"The number {option} is not valid. You can only choose numbers between 1 and {len(alphabets)}.")
        option = int(input(f"Enter the alphabet number between 1 and {len(alphabets)}: ")) 
    cantidad = int(input("How many words do you want there to be?: "))
    print(alphabets[option - 1].kleene_closure(cantidad).get())
    input("Press the ENTER key to continue.")

print("\n")
print("Language")
print("\n")

#creacion de languages
if len(alphabets) == 0:
    print("You must first create the alphabets in order to generate the languages.")
else:
    creationLanguages()
    input("Press the ENTER key to continue.")

print("\n")

#union lenguaje
if len(languages) == 0:
    print("First you must create the languages.")
else:
    print("union of languages.")
    show_languages()
    options(languages, "languages")
    union = selected[0].union(selected[1])
    print("The union of the languages is:")
    print(union.get())
    input("Press the ENTER key to continue.")

print("\n")

#difference lenguaje
if len(languages) == 0:
    print("First you must create the languages.")
else:
    print("Language difference.")
    show_languages()
    options(languages, "languages")
    difference = selected[0].difference(selected[1])
    print("The difference in the languages is:")
    print(difference.get())
    input("Press the ENTER key to continue.")

print("\n")

#nterseccion lenguaje
if len(languages) == 0:
    print("First you must create the languages.")
else:
    print("Intersection of languages")
    show_languages()
    options(languages, "languages")
    intersection = selected[0].intersection(selected[1])
    print("The intersection of the languages is:")
    print(intersection.get())
    input("Press the ENTER key to continue.")

print("\n")

#concatenation
if len(languages) == 0:
    print("First you must create the languages.")
else:
    print("concatenation of languages.")
    show_languages()
    options(languages, "languages")
    print("The concatenation of the languages is:")
    print(selected[0].concatenation(selected[1]))
    input("Press the ENTER key to continue.")

print("\n")

#languagepotency
if len(languages) == 0:
    print("First you must create the languages.")
else: 
    print("To which language would you like to apply the potency?")
    show_languages()
    option = int(input(f"Enter the language number between 1 and 2: "))
    while option < 1 or option > 2:
        print(f"The number {option} is not valid. You can only choose numbers between 1 and 2.")
        option = int(input(f"Enter the language number between 1 and 2: ")) 
    cantidad = int(input("Enter the power value: "))
    print(languages[option - 1].potency(cantidad))
    input("Press the ENTER key to continue.")

print("\n")

#invert
if len(languages) == 0:
    print("First you must create the languages.")
else: 
    print("To which language would you like to apply the inverse?")
    show_languages()
    option = int(input(f"Enter the language number between 1 and 2: "))
    while option < 1 or option > 2:
        print(f"The number {option} is not valid. You can only choose numbers between 1 and 2.")
        option = int(input(f"Enter the language number between 1 and 2: ")) 
    print(f"The inverse of the language {option} is: ")
    print(languages[option - 1].invert().get())
    input("Press the ENTER key to continue.")

print("\n")

#cardinality
if len(languages) == 0:
    print("First you must create the languages.")
else: 
    print("From which language do you want to obtain its cardinality?")
    show_languages()
    option = int(input(f"Enter the language number between 1 and 2: "))
    while option < 1 or option > 2:
        print(f"The number {option} is not valid. You can only choose numbers between 1 and 2.no es válido.")
        option = int(input(f"Enter the language number between 1 and 2: ")) 
    print(f"The cardinality of language {option} is: ")
    print(languages[option - 1].cardinality())
    input("Press the ENTER key to continue.")

