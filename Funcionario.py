from dataclasses import dataclass
from datetime import datetime


@dataclass
class Funcionario:
    run: str
    nombre: str
    fecha_nacimiento: datetime
    direccion: str
    fecha_ingreso: datetime

    def __init__(self, run: str, nombre: str,  direccion: str, fecha_nacimiento: datetime, fecha_ingreso: datetime):
        self.setRun(run)
        self.setNombre(nombre)
        self.setDireccion(direccion)
        self.setFechaIngreso(fecha_ingreso)
        self.setFechaNacimiento(fecha_nacimiento)

    # Validaciones
    def setRun(self, run: str):
        if 10 <= len(run) <= 12:
            self.run = run
        else:
            raise Exception("El run debe ser mayor o igual que 10 caracteres y menor o igual que 12")

    def setNombre(self, nombre: str):
        if 6 <= len(nombre) < 20:
            self.nombre = nombre
        else:
            raise Exception("El nombre debe ser mayor o igual que 6 caracteres y menor que 20")

    def setDireccion(self, direccion: str):
        if 6 <= len(direccion) <= 50:
            self.direccion = direccion
        else:
            raise Exception("La dirección debe ser mayor a 6 caracteres y menor a 50")

    def setFechaIngreso(self, fecha_ingreso: datetime):
        if fecha_ingreso < datetime.now():
            self.fecha_ingreso = fecha_ingreso
        else:
            raise Exception("La Fecha de ingreso no puede ser mayor que la fecha actual")

    def setFechaNacimiento(self, fecha_nacimiento: datetime):
        if datetime(1930, 1, 1) < fecha_nacimiento < datetime(2005, 1, 1):
            self.fecha_nacimiento = fecha_nacimiento
        else :
            raise Exception("La Fecha de ingreso no puede ser mayor que 2005 ni menores que 1930")

    def mostrarDatos(self):
        print(self.run)
        print(self.nombre)
        print(self.direccion)
        print(self.fecha_ingreso)
        print(self.fecha_nacimiento)
