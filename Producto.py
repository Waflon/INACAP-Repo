from dataclasses import dataclass


@dataclass
class Producto:
    nombre: str
    desc: str
    valor: int
    stock: int

    def __init__(self, nombre: str, desc: str, valor: int, stock: int):
        self.setNombre(nombre)
        self.setDescripcion(desc)
        self.setValor(valor)
        self.setStock(stock)

    def setNombre(self, nombre: str):
        if len(nombre) > 5:
            self.nombre = nombre
        else:
            raise Exception("El nombre del Producto debe tener más de 5 caracteres")

    def setValor(self, valor: int):
        if valor > 0:
            self.valor = valor
        else:
            raise Exception("El valor no puede ser menor o igual a 0")

    def setDescripcion(self, desc: str):
        if len(desc) <= 40:
            self.desc = desc
        else:
            raise Exception("La descripción solo puede tener como máximo 40 Carácteres")

    def setStock(self, stock: int):
        if stock >= 0:
            self.stock = stock
        else:
            raise Exception("El stock no puede ser menor a 0")

    def mostrarDatos(self):
        print(self.nombre)
        print(self.desc)
        print(self.valor)
        print(self.stock)