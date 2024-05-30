# Definición de la clase Coche
class Coche:
    # Método constructor para inicializar los atributos
    def __init__(self, marca, modelo, año):
        self.marca = marca       # Atributo de instancia
        self.modelo = modelo     # Atributo de instancia
        self.año = año           # Atributo de instancia
        self.arrancado = False   # Atributo de instancia para el estado del coche

    # Método para mostrar la información del coche
    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}"

    # Método para arrancar el coche
    def arrancar(self):
        if not self.arrancado:
            self.arrancado = True
            return f"El {self.marca} {self.modelo} ha arrancado."
        else:
            return f"El {self.marca} {self.modelo} ya está arrancado."

# Programa principal
def main():
    # Crear instancias (objetos) de la clase Coche
    coche1 = Coche("Toyota", "Corolla", 2020)
    coche2 = Coche("Ford", "Mustang", 2021)

    # Mostrar la información de los coches
    print(coche1.mostrar_informacion())  # Output: Marca: Toyota, Modelo: Corolla, Año: 2020
    print(coche2.mostrar_informacion())  # Output: Marca: Ford, Modelo: Mustang, Año: 2021

    # Arrancar los coches
    print(coche1.arrancar())  # Output: El Toyota Corolla ha arrancado.
    print(coche2.arrancar())  # Output: El Ford Mustang ha arrancado.

    # Intentar arrancar de nuevo los coches
    print(coche1.arrancar())  # Output: El Toyota Corolla ya está arrancado.
    print(coche2.arrancar())  # Output: El Ford Mustang ya está arrancado.

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
