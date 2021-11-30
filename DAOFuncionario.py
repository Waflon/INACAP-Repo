from dataclasses import dataclass
from Funcionario import Funcionario
import mysql.connector


@dataclass
class DAOFuncionario:
    # INSERT
    def insertarFuncionario(self, funcionario: Funcionario):
        conexion = mysql.connector.connect(user='root', password='Pink11235', database='s3_base_bodega')
        cursor = conexion.cursor()
        sql = "insert into funcionarios values(%s,%s,%s,%s,%s)"
        cursor.execute(sql, (funcionario.run,
                             funcionario.nombre,
                             funcionario.direccion,
                             funcionario.fecha_nacimiento,
                             funcionario.fecha_ingreso))
        conexion.commit()
        conexion.close()

    # UPDATE
    def actualizarFuncionario(self, funcionario: Funcionario):
        conexion = mysql.connector.connect(user='root', password='Pink11235', database='s3_base_bodega')
        cursor = conexion.cursor()
        sql = "update funcionarios set nombre = %s, direccion = %s, fecha_nacimiento=%s,fecha_ingreso=%s where rut like %s"
        cursor.execute(sql, (funcionario.nombre,
                             funcionario.direccion,
                             funcionario.fecha_nacimiento,
                             funcionario.fecha_ingreso,
                             funcionario.run
                             ))
        conexion.commit()
        conexion.close()

    # DELETE
    def eliminarFuncionario(self, funcionario: Funcionario):
        conexion = mysql.connector.connect(user='root', password='Pink11235', database='s3_base_bodega')
        cursor = conexion.cursor()
        sql = f"delete from funcionarios where rut like '{funcionario.run}'"
        cursor.execute(sql)
        conexion.commit()
        conexion.close()

    # SEARCH
    def buscarFuncionario(self, run: str):
        if len(run) < 13:
            conexion = mysql.connector.connect(user='root', password='Pink11235', database='s3_base_bodega')
            cursor = conexion.cursor()
            sql = f"select * from funcionarios where rut like '{run}'"
            cursor.execute(sql)
            fila = cursor.fetchone()
            conexion.close()
            funcionario = Funcionario(fila[0], fila[1], fila[2], fila[3], fila[4])
            return funcionario
        else:
            return None  # Retornamos dato vacio

    # LISTAR
    def listarFuncionario(self):

        conexion = mysql.connector.connect(user='root', password='Pink11235', database='s3_base_bodega')
        cursor = conexion.cursor()
        sql = 'select * from funcionarios'
        cursor.execute(sql)
        filas = cursor.fetchall()
        conexion.close()
        lista_funcionarios = list()  #

        for registro in filas:
            funcionario = Funcionario(registro[0], registro[1], registro[2], registro[3], registro[4])
            lista_funcionarios.append(funcionario)
        return lista_funcionarios
