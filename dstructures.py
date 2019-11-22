# ESTRUCTURAS DE DATOS
# Listas (Arrays)
lista = [2, 4, 6, 7]
print(lista)

# Si no copias, modificas el archivo original
mi_lista = lista
# mi_lista = lista.copy()

# Operaciones de lista
mi_lista.append(8) # Añadir 8...
print(mi_lista)

mi_lista.insert(2, 5) #...y 5 (en pos. 2)
print(mi_lista)

mi_lista.extend([9, 10]) # Añadir 9 y 10
print(mi_lista)

mi_lista.pop() # Eliminar el 10
print(mi_lista)

mi_lista.remove(2) # Quitar 2
print(mi_lista)

print("Elementos en lista", len(mi_lista))

# Con o sin copia
print(lista)
print(mi_lista)

mi_lista.reverse() # Es "inplace"
print(mi_lista)
mi_lista.reverse()

# Slicing: Iterable[start, stop, step]
print('Slicing')
print(mi_lista[:2]) # Primeros 2

print(mi_lista[2:5]) # De pos. 2 a pos. 4

print(mi_lista[::2]) # De dos en dos

print(mi_lista[::-1]) # De reversa


# Diccionarios (Mapas)
mi_mapa_edades = {'Sergio': 14, 'Andrea': 19, 'Luis': 21}

print("Sergio:", mi_mapa_edades['Sergio']) # Error si no existe
print(mi_mapa_edades.get('Esteban', 'Es nulo'))

print(mi_mapa_edades.keys())
print(mi_mapa_edades.values())
print(mi_mapa_edades.items())

# Añadiendo llave
mi_mapa_edades['Carlos'] = 22
print(mi_mapa_edades.items())

# Eliminando llave
del mi_mapa_edades['Carlos']
print(mi_mapa_edades.items())

