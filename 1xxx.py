import numpy as np
from scipy.interpolate import lagrange
import sympy as sp

# Definir la variable simbólica para el polinomio
x = sp.symbols('x')

# Datos para 1976
years_1976 = [1964, 1973, 1981, 1994]
population_1976 = [4.28, 5.16, 6.05, 8.33]

# Crear el polinomio de Lagrange para 1976
polinomio_1976 = lagrange(years_1976, population_1976)

# Convertir el polinomio a una expresión simbólica
polinomio_1976_expr = sum(polinomio_1976.coef[i] * x**i for i in range(len(polinomio_1976.coef)-1, -1, -1))

# Mostrar el polinomio y calcular el valor interpolado en 1976
print(f"Polinomio de Lagrange para 1976:\n{sp.expand(polinomio_1976_expr)}")
poblacion_1976 = polinomio_1976(1976)
print(f"Población interpolada en 1976: {poblacion_1976:.2f} millones\n")

# Datos para 2000
years_2000 = [1981, 1994, 2002, 2018]
population_2000 = [6.05, 8.33, 11.24, 14.90]

# Crear el polinomio de Lagrange para 2000
polinomio_2000 = lagrange(years_2000, population_2000)

# Convertir el polinomio a una expresión simbólica
polinomio_2000_expr = sum(polinomio_2000.coef[i] * x**i for i in range(len(polinomio_2000.coef)-1, -1, -1))

# Mostrar el polinomio y calcular el valor interpolado en 2000
print(f"Polinomio de Lagrange para 2000:\n{sp.expand(polinomio_2000_expr)}")
poblacion_2000 = polinomio_2000(2000)
print(f"Población interpolada en 2000: {poblacion_2000:.2f} millones")

