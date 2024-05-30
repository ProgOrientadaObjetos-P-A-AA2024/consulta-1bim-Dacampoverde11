# Definición de la clase Libro
class Libro:
    # Método constructor para inicializar los atributos
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo               # Atributo de instancia
        self.autor = autor                 # Atributo de instancia
        self.año_publicacion = año_publicacion # Atributo de instancia
        self.prestado = False              # Atributo de instancia para el estado del libro

    # Método para mostrar la información del libro
    def mostrar_informacion(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año de Publicación: {self.año_publicacion}"

    # Método para prestar el libro
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return f"El libro '{self.titulo}' ha sido prestado."
        else:
            return f"El libro '{self.titulo}' ya está prestado."

    # Método para devolver el libro
    def devolver(self):
        if self.prestado:
            self.prestado = False
            return f"El libro '{self.titulo}' ha sido devuelto."
        else:
            return f"El libro '{self.titulo}' no estaba prestado."

# Programa principal
def main():
    # Crear instancias (objetos) de la clase Libro
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)

    # Mostrar la información de los libros
    print(libro1.mostrar_informacion())  # Output: Título: Cien Años de Soledad, Autor: Gabriel García Márquez, Año de Publicación: 1967
    print(libro2.mostrar_informacion())  # Output: Título: Don Quijote de la Mancha, Autor: Miguel de Cervantes, Año de Publicación: 1605

    # Prestar los libros
    print(libro1.prestar())  # Output: El libro 'Cien Años de Soledad' ha sido prestado.
    print(libro2.prestar())  # Output: El libro 'Don Quijote de la Mancha' ha sido prestado.

    # Intentar prestar de nuevo los libros
    print(libro1.prestar())  # Output: El libro 'Cien Años de Soledad' ya está prestado.
    print(libro2.prestar())  # Output: El libro 'Don Quijote de la Mancha' ya está prestado.

    # Devolver los libros
    print(libro1.devolver())  # Output: El libro 'Cien Años de Soledad' ha sido devuelto.
    print(libro2.devolver())  # Output: El libro 'Don Quijote de la Mancha' ha sido devuelto.

    # Intentar devolver de nuevo los libros
    print(libro1.devolver())  # Output: El libro 'Cien Años de Soledad' no estaba prestado.
    print(libro2.devolver())  # Output: El libro 'Don Quijote de la Mancha' no estaba prestado.

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
