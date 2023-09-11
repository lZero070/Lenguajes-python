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


def options2():
    global alfabetosSeleccionados2
    aux = True
    while aux:
        eleccion = input(f"Ingrese los numeros de dos alfabetos separados por comas para utilizarlos para la creación de los dos lenguajes correspondientes (1-{len(alphabets)}): ")
        numeros = [int(opcion) for opcion in eleccion.split(",")]
        if len(numeros) <= 1 or len(numeros) > 2:
            print("Debe elegir dos alfabetos.")
            continue
        valido = True
        for numero in numeros:
            if numero < 1 or numero > len(alphabets):
                print(f"El número {numero} no es válido. Solo puede elegir números entre 1 y {len(alphabets)}.")
                valido = False
                break;       
        if valido:
            alfabetosSeleccionados2 = [alphabets[numero-1] for numero in numeros]
            break;


def crearLenguajes():
    l1 = Language([])
    l2 = Language([])
    show_alphabets()
    options2()
    cantidadl1 = int(input("Ingrese la cantidad de palabras que quiere que contenga el primer lenguaje: "))
    cantidadl2 = int(input("Ingrese la cantidad de palabras que quiere que contenga el segundo lenguaje: "))
    l1.generatewords([alfabetosSeleccionados2[0]], cantidadl1)
    l2.generatewords([alfabetosSeleccionados2[1]], cantidadl2)
    languages.append(l1)
    languages.append(l2)
    show_languages()
    print(f"Se han creado correctamente los dos lenguajes.")
    
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
    opcion = int(input(f"Ingrese el número del alfabeto entre 1 y {len(alphabets)}: "))
    while opcion < 1 or opcion > len(alphabets):
        print(f"El número {opcion} no es válido. Solo puede elegir números entre 1 y {len(alphabets)}.")
        opcion = int(input(f"Ingrese el número del alfabeto entre 1 y {len(alphabets)}: ")) 
    cantidad = int(input("¿Qué cantidad de palabras quiere que haya?: "))
    print(alphabets[opcion - 1].kleene_closure(cantidad).get())
    input("Presione la tecla ENTER para continuar...")

print("\n")
print("Language")
print("\n")

#creacion de lenguajes
if len(alphabets) == 0:
    print("Primero debe crear los alfabetos para poder generar los lenguajes.")
else:
    crearLenguajes()
    input("Presione la tecla ENTER para continuar...")