import json
from datetime import datetime
import multiline

with open('archivo.json') as archivo:
    datos = multiline.load(archivo,multiline=True)

nombre = datos["nombre"]
run = datos['run']
direccion = datos['direccion']
fechaNacimiento = datetime.strptime(datos['fechaNacimiento'], '%d/%m/%Y')
fechaIngreso = datetime.strptime(datos['fechaIngreso'], '%d/%m/%Y')
print(run)
print(nombre)
print(direccion)
print(fechaNacimiento)
print(fechaIngreso)
