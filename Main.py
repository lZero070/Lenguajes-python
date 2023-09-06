from functools import reduce
import time
from Alphabet import Alfabeto
#from Lenguaje import Lenguaje

alfabetos = []
lenguajes = []

def crearAlfabetos(cantidad):
    print("En este programa el elemento vacío es el #")
    for i in range(cantidad):
        simbolos = input(f"Ingrese los símbolos del alfabeto {i+1} separados por comas: ").split(",")
        alfabeto = Alfabeto(simbolos)
        alfabetos.append(alfabeto)
    print(f"Se han creado {cantidad} alfabetos.")
    
def mostrarAlfabetos():    
    for i, alfabeto in enumerate(alfabetos):
        print(f"Alfabeto {i+1}: {alfabeto.get()}")
        
def mostrarLenguajes():    
    for i, lenguaje in enumerate(lenguajes):
        print(f"Lenguaje {i+1}: {lenguaje.get()}")

#ingreso
cantidadAlfabetos = int(input("Por favor, ingrese la cantidad de alfabetos a crear (mínimo dos): "))
if cantidadAlfabetos < 2:
    print("Recuerde que la cantidad mínima de alfabetos es dos. Por favor, elija otra cantidad.")
else:
    crearAlfabetos(cantidadAlfabetos)   
    mostrarAlfabetos()
    input("Presione la tecla ENTER para continuar...")

def opciones(objeto, mensaje):
    global seleccionados
    aux = False
    while not aux:
        eleccion = input(f"Ingrese los numeros de los {mensaje} separados por comas (1-{len(objeto)}): ")
        numeros = [int(opcion) for opcion in eleccion.split(",")]
        if len(numeros) <= 1:
            print(f"Debe elegir mínimo dos {mensaje}.")
            continue
        aux = True
        for numero in numeros:
            if numero < 1 or numero > len(objeto):
                print(f"El número {numero} no es válido. Solo puede elegir números entre 1 y {len(objeto)}.")
                aux = False
                break;
    if aux:
        seleccionados = [objeto[numero-1] for numero in numeros]

#union
if len(alfabetos) == 0:
    print("Primero debe crear los alfabetos.")
else: 
    print("¿Qué alfabetos desea unir?")
    mostrarAlfabetos()
    opciones(alfabetos, "alfabetos")
    union = reduce(lambda a, b: a.union(b), seleccionados)
    print("La union de los alfabetos seleccionados es:")
    print(union.get())
    input("Presione la tecla ENTER para continuar...")