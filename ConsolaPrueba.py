from Funcionario import Funcionario
from Producto import Producto
from DAOFuncionario import DAOFuncionario
from DAOProducto import DAOProducto
from datetime import datetime

dao = DAOFuncionario()  # DAO PARA EL MANEJO DE FUNCIONARIOS
dao_p = DAOProducto()   # DAO PARA EL MANEJO DE PRODUCTOS

# Crear funcionarios y productos
funcionario1 = Funcionario("12332323-9", "Alvaro", "Azapa 1401",  datetime(1991,3,17), datetime(2009,2,1))
funcionario2 = Funcionario("12040403-5", "Javier", "New York 111",  datetime(2000,8,26), datetime(2015,1,2))
funcionario3 = Funcionario("20304404-3", "Pedro J", "Colombia 1234",  datetime(2004,1,22), datetime(2015,4,2))
funcionario4 = Funcionario("22039482-2", "Jocelyn", "Salesianos 392",  datetime(2003,6,19), datetime(2002,12,11))
funcionario5 = Funcionario("17322211-1", "Natalia", "Tehualda 2",  datetime(1993,4,17), datetime(2012,5,3))

producto1 = Producto("Cajonera", "Un mueble muy bonito", 19990, 23)
producto2 = Producto("Alfrombra","Una alfombra para patio", 42990,  31)
producto3 = Producto("Casa para mascotas", "Una casa para perros de tamaño pequeño", 32990, 17)
producto4 = Producto("Cama 2 plazas", "Una cama matrimonial color castaño",  109990, 11)
producto5 = Producto("Veladores",  "Un set de veladores para la pieza", 89990, 4)

# Comentados por comodidad, descomente para compilar
'''insertar 5 personas y 5 funcionarios '''
#dao.insertarFuncionario(funcionario1)
#dao.insertarFuncionario(funcionario2)
#dao.insertarFuncionario(funcionario3)
#dao.insertarFuncionario(funcionario4)
#dao.insertarFuncionario(funcionario5)

#dao_p.insertarProducto(producto1)
#dao_p.insertarProducto(producto2)
#dao_p.insertarProducto(producto3)
#dao_p.insertarProducto(producto4)
#dao_p.insertarProducto(producto5)

''' Modificar 2 Funcionarios y 1 Producto '''
#funcionario3.nombre = "Joaquin"
#funcionario5.nombre = "Rodrigo"
#dao.actualizarFuncionario(funcionario3)
#dao.actualizarFuncionario(funcionario5)

#producto1.valor = 19999
#dao_p.actualizarProducto(producto1, 1)  # inserta los datos en producto1 en el indice 1 de la BD

''' Buscar 1 Funcionario y 1 Producto'''
#print(dao.buscarFuncionario("12332323-9"))
#print(dao_p.buscarProducto(6))

''' Eliminar 1 Funcionario y 1 Producto (Eliminación a través del numero_producto'''
#dao.eliminarFuncionario(funcionario1)
#dao_p.eliminarProducto(6)}

''' Listar Productos y Funcionarios'''
#listaFuncionario= dao.listarFuncionario()
#for i in listaFuncionario:
#    print(i)

#listaProducto = dao_p.listarProducto()
#for i in listaProducto:
#    print(i)

