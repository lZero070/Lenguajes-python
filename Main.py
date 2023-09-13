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


def options_2():
    global alphabet_selected_2
    aux = True
    while aux:
        selection = input(f"Ingrese los numbers de dos alfabetos separados por comas para utilizarlos para la creación de los dos languages correspondientes (1-{len(alphabets)}): ")
        numbers = [int(option) for option in selection.split(",")]
        if len(numbers) <= 1 or len(numbers) > 2:
            print("Debe elegir dos alfabetos.")
            continue
        valid = True
        for number in numbers:
            if number < 1 or number > len(alphabets):
                print(f"El número {number} no es válido. Solo puede elegir números entre 1 y {len(alphabets)}.")
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
    quantity_l1 = int(input("Ingrese la cantidad de palabras que quiere que contenga el primer lenguaje: "))
    quantity_l2 = int(input("Ingrese la cantidad de palabras que quiere que contenga el segundo lenguaje: "))
    l1.generate([alphabet_selected_2[0]], quantity_l1)
    l2.generate([alphabet_selected_2[1]], quantity_l2)
    languages.append(l1)
    languages.append(l2)
    show_languages()
    print(f"Se han creado correctamente los dos languages.")
    
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
    input("Press the ENTER key to continue...")

print("\n")
#Cerradure estrella
if len(alphabets) == 0:
    print("Primero debe crear los alfabetos.")
else: 
    print("¿De qué alfabeto desea la cerradura de estrellas?")
    show_alphabets()
    option = int(input(f"Ingrese el número del alfabeto entre 1 y {len(alphabets)}: "))
    while option < 1 or option > len(alphabets):
        print(f"El número {option} no es válido. Solo puede elegir números entre 1 y {len(alphabets)}.")
        option = int(input(f"Ingrese el número del alfabeto entre 1 y {len(alphabets)}: ")) 
    cantidad = int(input("¿Qué cantidad de palabras quiere que haya?: "))
    print(alphabets[option - 1].kleene_closure(cantidad).get())
    input("Presione la tecla ENTER para continuar...")

print("\n")
print("Language")
print("\n")

#creacion de languages
if len(alphabets) == 0:
    print("Primero debe crear los alfabetos para poder generar los languages.")
else:
    creationLanguages()
    input("Presione la tecla ENTER para continuar...")

#union lenguaje
if len(languages) == 0:
    print("Primero debe crear los languages.")
else:
    print("unión de languages")
    show_languages()
    options(languages, "languages")
    union = selected[0].union(selected[1])
    print("La unión de los languages es:")
    print(union.get())
    input("Presione la tecla ENTER para continuar...")
        

#difference lenguaje
if len(languages) == 0:
    print("Primero debe crear los languages.")
else:
    print("Diferencia de languages")
    show_languages()
    options(languages, "languages")
    difference = selected[0].difference(selected[1])
    print("La difference de los languages es:")
    print(difference.get())
    input("Presione la tecla ENTER para continuar...")


#nterseccion lenguaje
if len(languages) == 0:
    print("Primero debe crear los languages.")
else:
    print("Interseccion de languages")
    show_languages()
    options(languages, "languages")
    intersection = selected[0].intersection(selected[1])
    print("La intersection de los languages es:")
    print(intersection.get())
    input("Presione la tecla ENTER para continuar...")


#concatenation
if len(languages) == 0:
    print("Primero debe crear los languages.")
else:
    print("concatenation de languages")
    show_languages()
    options(languages, "languages")
    print("La concatenation de los languages es:")
    print(selected[0].concatenation(selected[1]))
    input("Presione la tecla ENTER para continuar...")


#languagepotency
if len(languages) == 0:
    print("Primero debe crear los languages.")
else: 
    print("¿A qué lenguaje le deseas aplicar la potencia?")
    show_languages()
    option = int(input(f"Ingrese el número del lenguaje entre 1 y 2: "))
    while option < 1 or option > 2:
        print(f"El número {option} no es válido. Solo puede elegir números entre 1 y 2.")
        option = int(input(f"Ingrese el número del lenguaje entre 1 y 2: ")) 
    cantidad = int(input("Ingrese el valor de la potencia: "))
    print(languages[option - 1].potency(cantidad))
    input("Presione la tecla ENTER para continuar...")


#invert
if len(languages) == 0:
    print("Primero debe crear los languages.")
else: 
    print("¿A qué lenguaje le deseas aplicar la invert?")
    show_languages()
    option = int(input(f"Ingrese el número del lenguaje entre 1 y 2: "))
    while option < 1 or option > 2:
        print(f"El número {option} no es válido. Solo puede elegir números entre 1 y 2.")
        option = int(input(f"Ingrese el número del lenguaje entre 1 y 2: ")) 
    print(f"La invert del lenguaje {option} es: ")
    print(languages[option - 1].invert().get())
    input("Presione la tecla ENTER para continuar...")


#cardinality
if len(languages) == 0:
    print("Primero debe crear los languages.")
else: 
    print("¿De qué lenguaje quieres obtener su cardinality?")
    show_languages()
    option = int(input(f"Ingrese el número del lenguaje entre 1 y 2: "))
    while option < 1 or option > 2:
        print(f"El número {option} no es válido. Solo puede elegir números entre 1 y 2.")
        option = int(input(f"Ingrese el número del lenguaje entre 1 y 2: ")) 
    print(f"La cardinality del lenguaje {option} es: ")
    print(languages[option - 1].cardinality())
    input("Presione la tecla ENTER para continuar...")

