# CONDICIONALES
a = 5
b = 6
c = 8
# Condiciones pueden ser evaluadas fuera del if
a_mayor_que_b = a > b 
print(a_mayor_que_b)

# Bloque estándar (las tabulaciones importan)
if(a_mayor_que_b): # Igual que a > b
  if(a > c):
    print(f"{a} es mayor")
  else:
    print(f"{c} es mayor")
else:
  if(b > c):
    print(f"{b} es mayor")
  else:
    print(f"{c} es mayor")


# Operador ternario (mayor = condicion?a:b)
condicion = a > b
mayor = a if condicion else b 

# Solución anterior (aunque poco legible)
mayor = a if a>b & a>c else b if b>a & b>c else c
print('Numero mayor:', mayor)


# Bloque elif
opcion = input('Ingresa una letra (A, B, C): ')
opcion = opcion.upper()

if(opcion == 'A'):
  print("Código de la opción A")
elif(opcion == 'B'):
  print("Código de la opción B")
elif(opcion == 'C'):
  print("Código de la opción B")
else:
  print("Opción inválida")


