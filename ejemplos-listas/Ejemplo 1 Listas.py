# Definición de funciones para gestionar la lista de estudiantes

def agregar_estudiante(estudiantes, nombre, calificacion):
    estudiantes.append({'nombre': nombre, 'calificacion': calificacion})


def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes en la lista.")
    else:
        print("Lista de estudiantes:")
        for estudiante in estudiantes:
            print(f"Nombre: {estudiante['nombre']}, Calificación: {estudiante['calificacion']}")


def calcular_promedio(estudiantes):
    if not estudiantes:
        return 0
    total_calificaciones = sum(estudiante['calificacion'] for estudiante in estudiantes)
    return total_calificaciones / len(estudiantes)


def buscar_estudiante(estudiantes, nombre):
    for estudiante in estudiantes:
        if estudiante['nombre'].lower() == nombre.lower():
            return estudiante
    return None


# Programa principal
def main():
    estudiantes = []

    while True:
        print("\n--- Menú de Gestión de Estudiantes ---")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Calcular promedio de calificaciones")
        print("4. Buscar estudiante")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del estudiante: ")
            try:
                calificacion = float(input("Ingrese la calificación del estudiante: "))
                agregar_estudiante(estudiantes, nombre, calificacion)
                print(f"Estudiante {nombre} agregado con éxito.")
            except ValueError:
                print("Error: La calificación debe ser un número.")

        elif opcion == '2':
            mostrar_estudiantes(estudiantes)

        elif opcion == '3':
            promedio = calcular_promedio(estudiantes)
            if promedio == 0:
                print("No hay estudiantes para calcular el promedio.")
            else:
                print(f"El promedio de calificaciones es: {promedio:.2f}")

        elif opcion == '4':
            nombre = input("Ingrese el nombre del estudiante a buscar: ")
            estudiante = buscar_estudiante(estudiantes, nombre)
            if estudiante:
                print(
                    f"Estudiante encontrado: Nombre: {estudiante['nombre']}, Calificación: {estudiante['calificacion']}")
            else:
                print("Estudiante no encontrado.")

        elif opcion == '5':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
