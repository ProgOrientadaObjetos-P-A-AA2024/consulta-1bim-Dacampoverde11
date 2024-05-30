# Definición de funciones para gestionar la lista de tareas

def agregar_tarea(tareas, descripcion):
    tareas.append({'descripcion': descripcion, 'completada': False})
    print(f"Tarea '{descripcion}' agregada con éxito.")


def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas en la lista.")
    else:
        print("Lista de tareas:")
        for i, tarea in enumerate(tareas):
            estado = "Completada" if tarea['completada'] else "Pendiente"
            print(f"{i + 1}. {tarea['descripcion']} - {estado}")


def marcar_tarea_completada(tareas, numero):
    if 0 < numero <= len(tareas):
        tareas[numero - 1]['completada'] = True
        print(f"Tarea '{tareas[numero - 1]['descripcion']}' marcada como completada.")
    else:
        print("Número de tarea no válido.")


def eliminar_tareas_completadas(tareas):
    tareas[:] = [tarea for tarea in tareas if not tarea['completada']]
    print("Tareas completadas eliminadas.")


# Programa principal
def main():
    tareas = []

    while True:
        print("\n--- Menú de Gestión de Tareas ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tareas completadas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            descripcion = input("Ingrese la descripción de la tarea: ")
            agregar_tarea(tareas, descripcion)

        elif opcion == '2':
            mostrar_tareas(tareas)

        elif opcion == '3':
            mostrar_tareas(tareas)
            try:
                numero = int(input("Ingrese el número de la tarea a marcar como completada: "))
                marcar_tarea_completada(tareas, numero)
            except ValueError:
                print("Error: Debe ingresar un número válido.")

        elif opcion == '4':
            eliminar_tareas_completadas(tareas)

        elif opcion == '5':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()

