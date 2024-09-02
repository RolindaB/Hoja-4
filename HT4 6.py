import numpy as np
from scipy.interpolate import lagrange

# Definir los puntos de interpolación
x_values = np.linspace(-5, 5, 11)
f_values = 1 / (1 + x_values**2)

# Crear el polinomio de Lagrange de grado 10 usando scipy
poly = lagrange(x_values, f_values)

# Convertir los coeficientes del polinomio a una forma más legible
coef_list = np.poly1d(poly).coefficients

# Formatear el polinomio para imprimirlo en forma de ecuación
poly_str = " + ".join([f"{coef:.6f}x^{len(coef_list)-i-1}" if i < len(coef_list)-1 else f"{coef:.6f}" 
                       for i, coef in enumerate(coef_list)])

# Imprimir el polinomio de grado 10
print("El polinomio de interpolación de grado 10 es:")
print(poly_str)