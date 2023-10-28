import re

# Texto de ejemplo que contiene direcciones de correo electrónico
texto = """
Hola, mi dirección de correo es usuario1@example.com.
Por favor, envíame un correo a contacto@example.net.
"""

# Definir una expresión regular para buscar direcciones de correo electrónico
patron = r'\S+@\S+'

# Encontrar todas las coincidencias en el texto
coincidencias = re.findall(patron, texto)

# Imprimir las direcciones de correo electrónico encontradas
for direccion in coincidencias:
    print(direccion)
