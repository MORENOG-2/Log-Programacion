"""
Funciones definidas por el usuario
"""

# funcion Simple
def saludar():
    print("Hola, bienvenido a la programación")

saludar()

#Funcion con retorno
def return_saludar():
    return "Hola, bienvenido"

print(return_saludar())

#Funcion con un argumentos
def saludar_nombre(nombre):
    return f"Hola {nombre}, bienvenido a la programación"

print(saludar_nombre("rafael"))

#Funcion con varios argumentos
def saludar_nombre_apellido(nombre, apellido):
    return f"Hola {nombre} {apellido}, bienvenido a la programación"

print(saludar_nombre_apellido("Rafael", "moreno"))

#Funcion con argumentos predeterminados
def saludar_nombre_apellido_predeterminado(nombre="Rafael", apellido="Moreno"):
    return f"Hola {nombre} {apellido}, bienvenido a la programación"

print(saludar_nombre_apellido_predeterminado())
print(saludar_nombre_apellido_predeterminado("Carlos"))