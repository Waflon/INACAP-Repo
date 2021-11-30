from dataclasses import dataclass
from Producto import Producto
import mysql.connector


@dataclass
class DAOProducto:
    # INSERT
    def insertarProducto(self, producto: Producto):
        conexion = mysql.connector.connect(user='root', password='Pink11235', database='s3_base_bodega')
        cursor = conexion.cursor()
        sql = "insert into productos (nombre, descripcion, valor, cantidad) values(%s, %s, %s, %s);"
        cursor.execute(sql, (producto.nombre,
                             producto.desc,
                             producto.valor,
                             producto.stock))
        conexion.commit()
        conexion.close()

    # UPDATE
    def actualizarProducto(self, producto: Producto, numero: int):  # producto e indice a editar
        conexion = mysql.connector.connect(user='root', password='Pink11235', database='s3_base_bodega')
        cursor = conexion.cursor()
        sql = f"update productos set nombre = %s, descripcion = %s, valor=%s, cantidad=%s where numero_producto like '%s'"
        cursor.execute(sql, (producto.nombre,
                             producto.desc,
                             producto.valor,
                             producto.stock,
                             numero
                             ))
        conexion.commit()
        conexion.close()

    # DELETE
    def eliminarProducto(self, numero: int):
        conexion = mysql.connector.connect(user='root', password='Pink11235', database='s3_base_bodega')
        cursor = conexion.cursor()
        sql = f"delete from productos where numero_producto like '{numero}'"
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    # SEARCH
    def buscarProducto(self, numero: int):
        try:
            conexion = mysql.connector.connect(user='root', password='Pink11235', database='s3_base_bodega')
            cursor = conexion.cursor()
            sql = f"select * from productos where numero_producto like '{numero}'"
            cursor.execute(sql)
            fila = cursor.fetchone()
            conexion.close()
            producto = Producto(fila[1], fila[2], fila[3], fila[4])
            return producto
        except:
            return None

    # LISTAR
    def listarProducto(self):
        conexion = mysql.connector.connect(user='root', password='Pink11235', database='s3_base_bodega')
        cursor = conexion.cursor()
        sql = 'select * from productos'
        cursor.execute(sql)
        filas = cursor.fetchall()
        conexion.close()
        lista_productos = list()  #

        for registro in filas:
            producto = Producto(registro[1], registro[2], registro[3], registro[4])
            lista_productos.append(producto)
        return lista_productos
