from conexion import Conexion
from cliente import Cliente

class ClienteDao:
    @staticmethod
    def listar_clientes():
        conexion = Conexion.obtener_conexion()
        clientes = []
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT id, nombre, apellido, membresia FROM cliente")
                resultados = cursor.fetchall()
                for fila in resultados:
                    cliente = Cliente(fila[0], fila[1], fila[2], fila[3])
                    clientes.append(cliente)
            except Exception as e:
                print(f"Error al listar clientes: {e}")
            finally:
                conexion.close()
        return clientes
