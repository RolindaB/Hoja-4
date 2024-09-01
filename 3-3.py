import numpy as np

# Datos iniciales de presión y volumen
presion = np.array([0.5, 1.0, 1.5, 2.0, 2.5, 3.0])
volumen = np.array([1.62, 1.0, 0.75, 0.62, 0.52, 0.46])

def diferencias_divididas(x, y):
    """
    Calcula la tabla de diferencias divididas de Newton.
    """
    n = len(y)
    coef = np.zeros([n, n])
    coef[:,0] = y

    for j in range(1, n):
        for i in range(n-j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
    
    return coef[0]

def polinomio_newton(coef, x_data, x):
    """
    Evalúa el polinomio interpolante de Newton en un punto x.
    """
    n = len(coef) - 1
    p = coef[n]
    
    for k in range(1, n+1):
        p = coef[n-k] + (x - x_data[n-k]) * p
        
    return p

# 3.3 Estimar el volumen cuando la presión es 1.75 usando el método de diferencias divididas de Newton
coeficientes_newton = diferencias_divididas(presion, volumen)
volumen_1_75 = polinomio_newton(coeficientes_newton, presion, 1.75)

# Imprimir el resultado
print(f"El volumen estimado para una presión de 1.75 usando el método de diferencias divididas de Newton es: {volumen_1_75:.4f}")
