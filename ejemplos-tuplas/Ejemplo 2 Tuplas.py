def crear_cliente(nombre, direccion, telefono):
  """
  Función para crear una tupla que contiene información de un cliente.

  Parámetros:
    nombre: Cadena de texto con el nombre del cliente.
    direccion: Cadena de texto con la dirección del cliente.
    telefono: Cadena de texto con el número de teléfono del cliente.

  Retorno:
    Tupla que contiene la información del cliente.
  """
  return (nombre, direccion, telefono)

def mostrar_informacion_cliente(cliente):
  """
  Función para mostrar la información de un cliente almacenada en una tupla.

  Parámetro:
    cliente: Tupla que contiene la información del cliente.
  """
  print(f"Nombre: {cliente[0]}")
  print(f"Dirección: {cliente[1]}")
  print(f"Teléfono: {cliente[2]}")

# Ejemplo de uso
cliente1 = crear_cliente("Juan Pérez", "Avenida Los Andes 123", "+593 2 5555555")
cliente2 = crear_cliente("María Gómez", "Calle Libertad 456", "+593 9 8888888")

mostrar_informacion_cliente(cliente1)
mostrar_informacion_cliente(cliente2)
