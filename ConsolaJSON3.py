import json
from datetime import datetime
import multiline
from Funcionario import Funcionario
from DAOFuncionario import DAOFuncionario


with open('archivo2.json') as archivo:
    datos = multiline.load(archivo, multiline=True)
dao = DAOFuncionario()

for registro in datos:
    nombre = registro["nombre"]
    run = registro['rut']
    direccion = registro['direccion']
    fechaNacimiento = datetime.strptime(registro['fechaNacimiento'], '%d-%m-%Y')
    fechaIngreso = datetime.strptime(registro['fechaIngreso'], '%d-%m-%Y')
    func = Funcionario(run, nombre, direccion, fechaNacimiento, fechaIngreso)
    print(func.mostrarDatos())
    print(fechaIngreso)
    try:
        dao.insertarFuncionario(func)
    except:
        print(f"No se puede ingresar a {func.nombre}")