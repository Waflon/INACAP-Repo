import json
from Funcionario import Funcionario
from datetime import datetime

# Comienzo
lineaFuncionario = '{"run": "17763907-9", "nombre":"Alvaro", "direccion":"casa bonita", "fechaNacimiento":"21/12/2000", "fechaIngreso": "01/12/2020"}'  # Un JSON siempre está entre 
datos = json.loads(lineaFuncionario)
nombre = datos['nombre']
run = datos['run']
direccion = datos['direccion']
fechaNacimiento = datetime.strptime(datos['fechaNacimiento'], '%d/%m/%Y')
fechaIngreso = datetime.strptime(datos['fechaIngreso'], '%d/%m/%Y')

fun = Funcionario(run, nombre, direccion,fechaNacimiento, fechaIngreso)
print(fun)