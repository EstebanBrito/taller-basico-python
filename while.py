# CICLO WHILE
# Caso: Pedir números hasta encontrar un impar
# While basico
es_par = True
while es_par:
  a = input('Ingresar un número')
  es_par = a % 2 == 0 # También se podría usar break

print("Se ingresó un número impar")


# While con break
while True:
  a = input('Ingresar un número')
  if a % 2 != 0: break # Centinela

print("Se ingresó un número impar")


# No existe el do while
# Caso: Almacenar número hasta que rebase un límite
limite = 30
contador = 0

a = input('Ingresa un número')
contador += a
while contador < limite:
  a = input('Ingresa un número')
  contador += a

print('Se superó el límite')


# Igual se puede hacer con un centinela
limite = 30
contador = 0

while True:
  a = input('Ingresa un número')
  contador += a
  if contador > limite: break

print('Se superó el límite')