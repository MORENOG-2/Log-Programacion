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
diccionario = {"nombre": "Rafael", 
               "apellido": "Moreno", 
               "edad": "26",
               "ciudad": "Santa Marta",
               "carrera": "Ingeniería electrónica"} #Los diccionarios son estructuras de datos que almacenan pares de clave-valor
print(diccionario)
print(diccionario["edad"]) #Acceder a un valor del diccionario por su clave
diccionario["email"] = "rafaemore846@gmail.com" #Agregar una nueva pareja de clave-valor al diccionario 
diccionario["edad"] = "27" #Modificar el valor de una clave existente en el diccionario
print(diccionario["edad"])
print(diccionario)
diccionario.keys() #Obtener una lista de las claves del diccionario
print(diccionario.keys())
diccionario.values() #Obtener una lista de los valores del diccionario
print(diccionario.values())
del diccionario["ciudad"] #Eliminar una pareja de clave-valor del diccionario por su clave
print(diccionario)
diccionario.pop("apellido") #Eliminar una pareja de clave-valor del diccionario por su clave y devolver su valor
print(diccionario)
diccionario = dict(sorted(diccionario.items())) #Ordenar el diccionario por sus claves y convertirlo de nuevo a diccionario
print(diccionario)

diccionario.clear() #Eliminar todos los elementos del diccionario
print(diccionario)
print("Fin de diccionarios")


