import numpy as np
import matplotlib.pyplot as plt

# Datos
horas = [6, 8, 10, 12, 14, 16, 18, 20]
temperaturas = [7, 9, 12, 18, 21, 19, 15, 10]

# Ajustar un polinomio de grado 7 (n-1) a los datos
coeficientes = np.polyfit(horas, temperaturas, 7)
polinomio = np.poly1d(coeficientes)

# Mostrar el polinomio
print("El polinomio interpolante es:")
print(polinomio)
# 60 - 100%
# 10 - ?
# 10 == 16.67
# Estimar las temperaturas para horas específicas
horas_a_estimar = [7, 9, 12.5, 18.167]
temperaturas_estimadas = polinomio(horas_a_estimar)

# Mostrar los resultados de las estimaciones
print("\nEstimaciones de temperatura:")
for hora, temp in zip(horas_a_estimar, temperaturas_estimadas):
    print(f"Temperatura estimada para las {hora:.2f} horas: {temp:.2f} °C")

# Graficar los puntos y el polinomio
horas_continuas = np.linspace(min(horas), max(horas), 500)
temperaturas_interpoladas = polinomio(horas_continuas)

plt.plot(horas, temperaturas, 'o', label='Datos de temperatura')
plt.plot(horas_continuas, temperaturas_interpoladas, '-', label='Polinomio interpolante')
plt.xlabel('Hora del día (h)')
plt.ylabel('Temperatura (°C)')
plt.title('Temperatura Ambiente a Diferentes Horas del Día')
plt.grid(True)
plt.legend()
plt.show()
