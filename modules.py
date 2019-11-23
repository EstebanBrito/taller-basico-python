import my_module # Import estándar 
# import ./modules/my_module
# from my_module import vol_prisma # Import específico (o todos, con *)
# from my_module import vol_prisma as vol_prisma_cuad # Import con renombre

print(f"{my_module.area_circulo(3):.2f}")

print(my_module.area_cuadrado(4))

print(my_module.area_rectangulo(2, 4))


# Mezclando namespaces
def vol_prisma(area_base, altura):
  """Calcula el volumen de cualquier prisma"""
  return area_base * altura

# ¿Qué valor regresa la función? ¿100 o 20?
print(vol_prisma(5, 4))