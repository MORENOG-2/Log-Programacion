# Ejemplo de craciones de todas las estructuras soportadas en python

# Listas
print("Ejemplo de listas")
lista = [1, 2, 3, 4, 5]
print(lista)
lista.append(6) #Para agregar un elemento a la lista
print(lista)
lista.remove(3) #Para eliminar un elemento de la lista
print(lista)
lista[1]  #Acceder a un elemento de la lista por su índice
print(lista[1])
lista[1] = 10 #Modificar un elemento de la lista por su índice
print(lista)
lista.sort() #Ordenar la lista
print(lista)

# Tuplas
print("Ejemplo de tuplas")
tupla = (1, 2, 3, 4, 5) #Las tuplas son inmutables, no se pueden modificar después de su creación
print(tupla)
print(tupla[1]) #Acceder a un elemento de la tupla por su índice
tupla = tuple(sorted(tupla)) #Ordenar la tupla y convertirla de nuevo a tupla
print(tupla)

#Sets
print("Ejemplo de sets")
conjunto = {1, 2, 2, 3, 4, 4, 5} #Los sets no permiten elementos duplicados
print(conjunto)
conjunto.add(6)  #Agregar un elemento al set
print(conjunto)
conjunto.remove(2) #Eliminar un elemento del set
print(conjunto)
conjunto.update({7, 8, 9}) #Agregar varios elementos al set
print(conjunto)
conjunto.clear() #Eliminar todos los elementos del set 
print(conjunto)


# Diccionarios
print("Ejemplo de diccionarios")
diccionario = {"nombre": "Rafael", "apellido": "Moreno", "edad": 26}
print(diccionario)

# Conjuntos
conjunto = {1, 2, 3, 4, 5}
print(conjunto)

# Funciones
def saludar(nombre):
    print(f"Hola {nombre}, bienvenido a la programación")
saludar("Rafael")

# Clases
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        print(f"Hola {self.nombre} {self.apellido}, bienvenido a la programación")
persona1 = Persona("Rafael", "Moreno", 26)
persona1.saludar()

# Módulos
def saludar_modulo(nombre):
    print(f"Hola {nombre}, bienvenido a la programación")
saludar_modulo("Rafael")

