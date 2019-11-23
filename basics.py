# VARIABLES EN PYTHON
# No es necesario definir tipo (static, public, etc)
# ni tipo (int, float, etc)
mi_variable = 45
print(mi_variable)

mi_variable = 3.9
print(mi_variable)

mi_variable = True
print(mi_variable)

mi_variable = 'otro valor'
print(mi_variable)

mi_variable = [1, 6, 3, 3]
print(mi_variable)


# Operaciones (+, -, *, /)
resul = 4 // 7
print(resul) 

resul = 3**3
print(resul)


# I/0
# Cadenas
mi_cadena = input('Ingresa una cadena: ')
print(mi_cadena * 3)

# Números (conversión explícita)
mi_variable = int(input('Ingresa un número: '))
print(mi_variable * 3)




# FORMATEO DE CADENAS
nombre = 'Alejandro'
apellido = 'Pérez'
valor1 = 8.6
valor2 = 4.2

# Estandar
print('Me llamo %s %s. Mucho gusto' % (nombre, apellido))
# %d (enteros), %f (flotantes)
print('El producto de %d y %d es %.2f' % (valor1, valor2, valor1*valor2))

# Usando format()
print('Me llamo {} {}. Mucho gusto'.format(nombre, apellido))

print('El producto de {1} y {0} es {2}'.format(valor1, valor2, valor1*valor2))

# Cadenas f (f strings). Introducidas en Python 3.6. Evaluan la expresión.
print(f'Me llamo {nombre.upper()} {apellido}. Mucho gusto.')

print(f'Me llamo {valor1} y {valor2} es {valor1*valor2}')
