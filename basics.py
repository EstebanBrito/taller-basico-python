# VARIABLES EN PYTHON
# No es necesario definir tipo (static, public, etc)
# ni tipo (int, float, etc)
mi_variable = 45
print(mi_variable)

mi_variable = 3.9
print(mi_variable)

mi_variable = True
print(mi_variable)

mi_variable = "otro valor"
print(mi_variable)

mi_variable = [1, 6, 3, 3]
print(mi_variable)


# Operaciones (+, -, *, /)
resul = 4 // 7
print(resul) 

resul = 3**3
print(resul)


# I/0
# Detecta entre números...
mi_variable = input("Ingresa un número:")
print(mi_variable)

# ...y cadenas
mi_cadena = input("Ingresa una cadena")
print(mi_cadena)


# FORMATEO DE CADENAS
nombre = "Alejandro"
apellido = "Pérez"
valor1 = 8.6
valor2 = 4.2

# Estandar
print("Me llamo %s %s. Mucho gusto" % (nombre, apellido))

print("El producto de %d y %d es %.2f" % (valor1, valor2, valor1*valor2))

# Usando format()
print("Me llamo {0} {1}. Mucho gusto".format(nombre, apellido))

print("El producto de %d y %d es %.2f".format(valor1, valor2, valor1*valor2))

# Cadenas f (f strings). Introducidas en Python 3.6. Evaluan la expresión.
print(f"Me llamo {nombre.lower()} {apellido}. Mucho gusto.")

print(f"Me llamo {valor1} y {valor2} es .{valor1*valor2}")
