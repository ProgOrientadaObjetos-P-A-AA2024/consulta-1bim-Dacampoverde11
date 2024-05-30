# Definición de la clase Empleado
class Empleado:
    def __init__(self, nombre, posicion, salario):
        self.nombre = nombre
        self.posicion = posicion
        self.salario = salario

    def __str__(self):
        return f"Nombre: {self.nombre}, Posición: {self.posicion}, Salario: ${self.salario:.2f}"

# Definición de la clase Empresa para gestionar empleados
class Empresa:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, nombre, posicion, salario):
        nuevo_empleado = Empleado(nombre, posicion, salario)
        self.empleados.append(nuevo_empleado)
        print(f"Empleado {nombre} agregado con éxito.")

    def mostrar_empleados(self):
        if not self.empleados:
            print("No hay empleados en la empresa.")
        else:
            print("Lista de empleados:")
            for empleado in self.empleados:
                print(empleado)

    def calcular_salario_total(self):
        total_salarios = sum(empleado.salario for empleado in self.empleados)
        print(f"El salario total de todos los empleados es: ${total_salarios:.2f}")

# Programa principal
def main():
    empresa = Empresa()

    while True:
        print("\n--- Menú de Gestión de Empleados ---")
        print("1. Agregar empleado")
        print("2. Mostrar empleados")
        print("3. Calcular salario total")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del empleado: ")
            posicion = input("Ingrese la posición del empleado: ")
            try:
                salario = float(input("Ingrese el salario del empleado: "))
                empresa.agregar_empleado(nombre, posicion, salario)
            except ValueError:
                print("Error: El salario debe ser un número.")

        elif opcion == '2':
            empresa.mostrar_empleados()

        elif opcion == '3':
            empresa.calcular_salario_total()

        elif opcion == '4':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
