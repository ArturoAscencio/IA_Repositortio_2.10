import re

# Texto de ejemplo que contiene direcciones de correo electr�nico
texto = """
Hola, mi direcci�n de correo es usuario1@example.com.
Por favor, env�ame un correo a contacto@example.net.
"""

# Definir una expresi�n regular para buscar direcciones de correo electr�nico
patron = r'\S+@\S+'

# Encontrar todas las coincidencias en el texto
coincidencias = re.findall(patron, texto)

# Imprimir las direcciones de correo electr�nico encontradas
for direccion in coincidencias:
    print(direccion)
