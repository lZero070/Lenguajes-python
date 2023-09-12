from functools import reduce
import time
from Alphabet import Alfabeto
from language import Lenguaje

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
        
def opciones2():
    global alfabetosSeleccionados2
    aux = True
    while aux:
        eleccion = input(f"Ingrese los numeros de dos alfabetos separados por comas para utilizarlos para la creación de los dos lenguajes correspondientes (1-{len(alfabetos)}): ")
        numeros = [int(opcion) for opcion in eleccion.split(",")]
        if len(numeros) <= 1 or len(numeros) > 2:
            print("Debe elegir dos alfabetos.")
            continue
        valido = True
        for numero in numeros:
            if numero < 1 or numero > len(alfabetos):
                print(f"El número {numero} no es válido. Solo puede elegir números entre 1 y {len(alfabetos)}.")
                valido = False
                break;       
        if valido:
            alfabetosSeleccionados2 = [alfabetos[numero-1] for numero in numeros]
            break;
    
        
def crearLenguajes():
    l1 = Lenguaje([])
    l2 = Lenguaje([])
    mostrarAlfabetos()
    opciones2()
    cantidadl1 = int(input("Ingrese la cantidad de palabras que quiere que contenga el primer lenguaje: "))
    cantidadl2 = int(input("Ingrese la cantidad de palabras que quiere que contenga el segundo lenguaje: "))
    l1.generarPalabras([alfabetosSeleccionados2[0]], cantidadl1)
    l2.generarPalabras([alfabetosSeleccionados2[1]], cantidadl2)
    lenguajes.append(l1)
    lenguajes.append(l2)
    mostrarLenguajes()
    print(f"Se han creado correctamente los dos lenguajes.")

#crear alfabeto    
cantidadAlfabetos = int(input("Por favor, ingrese la cantidad de alfabetos a crear (mínimo dos): "))
if cantidadAlfabetos < 2:
    print("Recuerde que la cantidad mínima de alfabetos es dos. Por favor, elija otra cantidad.")
else:
    crearAlfabetos(cantidadAlfabetos)   
    mostrarAlfabetos()
    input("Presione la tecla ENTER para continuar...") 


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
    

#diferencia
if len(alfabetos) == 0:
    print("Primero debe crear los alfabetos.")
else: 
    print("¿De qué alfabetos deseas la diferencia?")
    mostrarAlfabetos()
    opciones(alfabetos, "alfabetos")
    diferencia = reduce(lambda a, b: a.diferencia(b), seleccionados)
    print("La diferencia de los alfabetos seleccionados es:")
    print(diferencia.get())
    input("Presione la tecla ENTER para continuar...")


#interseccion
if len(alfabetos) == 0:
    print("Primero debe crear los alfabetos.")
else: 
    print("¿De qué alfabetos deseas la intersección?")
    mostrarAlfabetos()
    opciones(alfabetos, "alfabetos")
    interseccion = reduce(lambda a, b: a.interseccion(b), seleccionados)
    print("La interseccion de los alfabetos seleccionados es:")
    print(interseccion.get())
    input("Presione la tecla ENTER para continuar...")


#cerradura
if len(alfabetos) == 0:
    print("Primero debe crear los alfabetos.")
else: 
    print("¿De qué alfabeto desea la cerradura de estrellas?")
    mostrarAlfabetos()
    opcion = int(input(f"Ingrese el número del alfabeto entre 1 y {len(alfabetos)}: "))
    while opcion < 1 or opcion > len(alfabetos):
        print(f"El número {opcion} no es válido. Solo puede elegir números entre 1 y {len(alfabetos)}.")
        opcion = int(input(f"Ingrese el número del alfabeto entre 1 y {len(alfabetos)}: ")) 
    cantidad = int(input("¿Qué cantidad de palabras quiere que haya?: "))
    print(alfabetos[opcion - 1].cerraduraEstrellas(cantidad).get())
    input("Presione la tecla ENTER para continuar...")
    

#crear lenguaje
if len(alfabetos) == 0:
    print("Primero debe crear los alfabetos para poder generar los lenguajes.")
else:
    crearLenguajes()
    input("Presione la tecla ENTER para continuar...")


#union lenguaje
if len(lenguajes) == 0:
    print("Primero debe crear los lenguajes.")
else:
    print("unión de lenguajes")
    mostrarLenguajes()
    opciones(lenguajes, "lenguajes")
    union = seleccionados[0].union(seleccionados[1])
    print("La unión de los lenguajes es:")
    print(union.get())
    input("Presione la tecla ENTER para continuar...")
        

#diferencia lenguaje
if len(lenguajes) == 0:
    print("Primero debe crear los lenguajes.")
else:
    print("Diferencia de lenguajes")
    mostrarLenguajes()
    opciones(lenguajes, "lenguajes")
    diferencia = seleccionados[0].diferencia(seleccionados[1])
    print("La diferencia de los lenguajes es:")
    print(diferencia.get())
    input("Presione la tecla ENTER para continuar...")


#nterseccion lenguaje
if len(lenguajes) == 0:
    print("Primero debe crear los lenguajes.")
else:
    print("Interseccion de lenguajes")
    mostrarLenguajes()
    opciones(lenguajes, "lenguajes")
    interseccion = seleccionados[0].interseccion(seleccionados[1])
    print("La interseccion de los lenguajes es:")
    print(interseccion.get())
    input("Presione la tecla ENTER para continuar...")


#concatenacion
if len(lenguajes) == 0:
    print("Primero debe crear los lenguajes.")
else:
    print("concatenacion de lenguajes")
    mostrarLenguajes()
    opciones(lenguajes, "lenguajes")
    print("La concatenacion de los lenguajes es:")
    print(seleccionados[0].concatenacion(seleccionados[1]))
    input("Presione la tecla ENTER para continuar...")


#potencia
if len(lenguajes) == 0:
    print("Primero debe crear los lenguajes.")
else: 
    print("¿A qué lenguaje le deseas aplicar la potencia?")
    mostrarLenguajes()
    opcion = int(input(f"Ingrese el número del lenguaje entre 1 y 2: "))
    while opcion < 1 or opcion > 2:
        print(f"El número {opcion} no es válido. Solo puede elegir números entre 1 y 2.")
        opcion = int(input(f"Ingrese el número del lenguaje entre 1 y 2: ")) 
    cantidad = int(input("Ingrese el valor de la potencia: "))
    print(lenguajes[opcion - 1].potencia(cantidad))
    input("Presione la tecla ENTER para continuar...")


#inversa
if len(lenguajes) == 0:
    print("Primero debe crear los lenguajes.")
else: 
    print("¿A qué lenguaje le deseas aplicar la inversa?")
    mostrarLenguajes()
    opcion = int(input(f"Ingrese el número del lenguaje entre 1 y 2: "))
    while opcion < 1 or opcion > 2:
        print(f"El número {opcion} no es válido. Solo puede elegir números entre 1 y 2.")
        opcion = int(input(f"Ingrese el número del lenguaje entre 1 y 2: ")) 
    print(f"La inversa del lenguaje {opcion} es: ")
    print(lenguajes[opcion - 1].inversa().get())
    input("Presione la tecla ENTER para continuar...")


#cardinalidad
if len(lenguajes) == 0:
    print("Primero debe crear los lenguajes.")
else: 
    print("¿De qué lenguaje quieres obtener su cardinalidad?")
    mostrarLenguajes()
    opcion = int(input(f"Ingrese el número del lenguaje entre 1 y 2: "))
    while opcion < 1 or opcion > 2:
        print(f"El número {opcion} no es válido. Solo puede elegir números entre 1 y 2.")
        opcion = int(input(f"Ingrese el número del lenguaje entre 1 y 2: ")) 
    print(f"La cardinalidad del lenguaje {opcion} es: ")
    print(lenguajes[opcion - 1].cardinalidad())
    input("Presione la tecla ENTER para continuar...")

