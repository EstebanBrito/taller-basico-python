# FUNCIONES
def mi_funcion(a, b):
  return a + b

print(mi_funcion(3, 4))

def saludar(nombre, saludo="Hola", otro="ghg"): # El orden importa
  """Esta función ofrece un saludo personalizado al usuario"""
  return f"{saludo} {nombre}"


print(saludar('Luis')) # Normal (con valores default)
print(saludar('Luis', 'Buenos días,')) # Argumentos definidos
print(saludar(saludo='Buenos días,', nombre='Luis')) # Orden modificable


# FUNCIONES LAMBDA
# lambda valores : expresion)
sumar = lambda a, b : a + b

print(sumar(5, 4))

# Útil para funciones matemáticas (es más legible)
area_triangulo = lambda base, alt : (base * alt) / 2

print(area_triangulo(4, 3))


# Comprensión de listas (Lists Comprehension)
# [returno for valor in Iterable if condicion]
cuadrados = [x**2 for x in range(5)]
print(cuadrados)

pares = [x for x in range(20) if x % 2 == 0]
print(pares)


# Filtros y mapeos


