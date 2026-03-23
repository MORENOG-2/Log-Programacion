"""
Operaciones
"""
r1 = "Hola"
r2 = "Mundo"

# Concatenacion 
print(r1 + " " + r2 + "!")

# Repeticion
print(r1 * 3)

#indexacion
print(r1[2] + r1[0])

# Longitud
print(len(r2))

#porcionamiento
print(r2[0:3])
print(r2[3:])

#Busqueda
print("Ho" in r1) # True porque Hola tiene la H mayuscula,
print("ho" in r1) # si fuera "ho" seria False porque no hay una h minuscula en Hola

#Reemplazo
print(r1.replace("o", "a")) # Reemplaza la letra o por la letra a, entonces Hola se convierte en Hala

#Division
print(r2.split("n")) # Divide la palabra Mundo en dos partes

#Mayusculas, minusculas y primeras letras mayusculas
print(r1.upper()) # Convierte Hola en HOLA
print(r1.lower()) # Convierte Hola en hola
print("rafael moreno".capitalize()) # Convierte la primera letra de Hola en mayuscula.
print("rafael moreno".title()) # Convierte la primera letra de cada palabra en mayuscula.

#Eliminacion de espacios
r3 = "   rafael moreno   "
print(r3) # Imprime la cadena con los espacios en blanco
print(r3.strip()) # Elimina los espacios en blanco al principio y al final
print(r3.lstrip()) # Elimina los espacios en blanco al principio
print(r3.rstrip()) # Elimina los espacios en blanco al final

#Busqueda al principio y al final
print(r1.startswith("H")) # True porque Hola empieza con H
print(r1.endswith("p")) # True porque Hola termina con a

r4 = "Rafael Moreno Guerra"
r5 = 26

#Busqueda de posicion
print(r4.find("Moreno")) # Devuelve la posicion de la primera letra Moreno.
print(r4.find("Guerra")) # Devuelve la posicion de la ultima letra Guerra.
print(r4.find("Rafael")) # Devuelve la posicion de la primera letra Rafael.
print(r4.lower().find("moreno")) # Devuelve la posicion de la primera letra rafael, sin importar mayusculas o minusculas.

#Busqueda de ocurrencias
print(r4.count("a")) # Devuelve el numero de veces que aparece la letra a.
print(r4.count("e")) # Devuelve el numero de veces que aparece la letra e.

#Formateo de cadenas
print("Mi nombre es {} y tengo {} años".format(r4, r5)) # Reemplaza los {} por los valores que se pasan como argumentos a format.

#Interpolacion de cadenas
print(f"Mi nombre es {r4} y tengo {r5} años") # Reemplaza los {} por los valores de las variables r4 y r5.

#transformacion en lista caracteres y palabras
print(list(r4)) # Convierte la cadena en una lista de caracteres.
print(r4.split()) # Convierte la cadena en una lista de palabras, separando por espacios en blanco.

#transformacion de lista a cadena
print("_".join(r4.split())) # Convierte la lista de palabras en una cadena, uniendo las palabras con un espacio en blanco.