import math

def area_circulo(radio):
  return math.pi * radio ** 2

def area_cuadrado(lado):
  return lado**2

def area_rectangulo(ancho, largo):
  return ancho*largo

def vol_prisma(base, altura):
  """Calcula el volumen de un prisma cuadrangular""" 
  return base**2 * altura