class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def saludar(self):
    print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Juan", 30)
persona2 = Persona("María", 25)

persona1.saludar()
persona2.saludar()
