import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
years = np.array([1778, 1880, 1893, 1921, 1940, 1950, 1964, 1973, 1981, 1994, 2002, 2018])
population = np.array([0.4, 1.22, 1.36, 2.00, 2.38, 2.79, 4.28, 5.16, 6.05, 8.33, 11.24, 14.90])

# Ecuación de la regresión exponencial obtenida en la parte 1.3
def exponential_model(x, a, b):
    return a * np.exp(b * x)

# Coeficientes obtenidos de la regresión
a = 5e-13
b = 0.0152

# Predicción para el año 2024
year_to_predict = 2024
predicted_population = exponential_model(year_to_predict, a, b)
print(f"La población predicha para el año {year_to_predict} es: {predicted_population:.2f} millones")

# Graficar los puntos y la curva de la regresión
plt.scatter(years, population, color='red', label='Datos')
years_range = np.linspace(min(years), year_to_predict, 100)
plt.plot(years_range, exponential_model(years_range, a, b), label='Modelo exponencial', color='blue')
plt.scatter(year_to_predict, predicted_population, color='green', label=f'Predicción {year_to_predict}')
plt.xlabel('Año')
plt.ylabel('Población (millones)')
plt.legend()
plt.show()
