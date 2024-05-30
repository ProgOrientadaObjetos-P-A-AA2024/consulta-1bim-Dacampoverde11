def calcular_promedio(notas):
  """
  Función para calcular el promedio de un grupo de notas.

  Parámetros:
    notas: Tupla que contiene las notas de los estudiantes.

  Retorno:
    El promedio de las notas, como un valor flotante.
  """
  if len(notas) == 0:
    return None

  suma_notas = 0
  for nota in notas:
    suma_notas += nota

  promedio = suma_notas / len(notas)
  return promedio

# Ejemplo de uso
notas_estudiantes = (9.5, 8.7, 10.0, 7.8, 6.5)

promedio_general = calcular_promedio(notas_estudiantes)

print(f"El promedio general de los estudiantes es: {promedio_general:.2f}")
