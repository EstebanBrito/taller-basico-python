# CICLO FOR
nombres = ['Andrea', 'Carlos', 'Daniel', 'Roberto', 'Sergio']

# For básico (range)
for i in range(5):
  print(i)

# For básico (for each)
for nombre in nombres:
  print(nombre)

# For básico, con índice
for i in range(len(nombres)):
  print(f"En posición {i} encontramos: {nombres[i]}")

# For con enumerate
for i, nombre in enumerate(nombres):
  print(f"Posición {i}: {nombre}")

# For multiple (combina elementos de dos Iterables) (importa el orden)
for i, j in zip(nombres, range(10)):
  print(i, j)

# El for, internamente funciona diferente (Iterable)