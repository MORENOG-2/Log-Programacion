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


# Punto Extra
print("Ejercicio Extra")

print("Agenda de contactos")
agenda = {} #Crear un diccionario vacío para almacenar los contactos
while True:
    opcion = input("""Que desea hacer? 
                1) Agregar contacto
                2) Ver contactos
                3) Actualizar contacto
                4) Eliminar contacto
                5) Salir
                : """)
    if opcion.lower() == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el número de teléfono del contacto: ") 
        if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 10: 
            agenda[nombre] = telefono #Agregar el contacto al diccionario
            print("Contacto agregado exitosamente")
        else:
            print("El numero de telefono tiene mas de 10 digitos o no es un numero, por favor ingrese un numero de telefono valido")

    elif opcion.lower() == "2":
        if len(agenda) == 0:
            print("No hay contactos en la agenda")
        else:
            print("Contactos en la agenda:")
            for nombre, telefono in agenda.items(): #Iterar sobre los elementos del diccionario para mostrar los contactos
                print(f"{nombre}: {telefono}")

    elif opcion.lower() == "3":
        nombre = input("Ingrese el nombre del contacto a actualizar: ")
        if nombre in agenda:
            telefono = input("Ingrese el nuevo número de teléfono del contacto: ")
            if telefono.isdigit() and len(telefono) > 0 and len(telefono) <= 10:
                agenda[nombre] = telefono #Agregar el contacto al diccionario
                print("Contacto actualizado exitosamente")
            else:
                print("El numero de telefono tiene mas de 10 digitos o no es un numero, por favor ingrese un numero de telefono valido")
        else:
            print(f"El contacto {nombre} no existe en la agenda")

    elif opcion.lower() == "4":
        nombre = input("Ingrese el nombre del contacto a eliminar: ")
        if nombre in agenda:
            del agenda[nombre] #Eliminar el contacto del diccionario
            print("Contacto eliminado exitosamente")
        else:
            print(f"El contacto {nombre} no existe en la agenda")
    elif opcion.lower() == "5":
        print("Saliendo de la agenda de contactos")
        break
    else:
        print("Opción no válida, por favor ingrese una opción del 1 al 5")

