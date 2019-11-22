# FUNCIONES
def mi_funcion(a, b):
  return a + b

print(mi_funcion(3, 4))

def saludar(nombre, saludo="Hola "): # El orden importa
  return f"{saludo}, {nombre}"

print(saludar('Luis'))
print(saludar('Luis', 'Buenos días'))

print(saludar(saludo='Buenos días', nombre='Luis')) # Orden modificable


# FUNCIONES LAMBDA
# lambda valores : expresion)
sumar = lambda a, b : a + b

print(sumar(5, 4))

# Comprensión de listas (List Comprehension)
# [return_value for value in Iterable if condition]
cuadrados = [x**2 for x in range(5)]

pares = [x for x in range(20) if x % 2 == 0]

