import mysql.connector
from mysql.connector import Error

class Conexion:
    @staticmethod
    def obtener_conexion():
        try:
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='tenerife',  # tu contraseña de MySQL en XAMPP (por defecto es vacío)
                database='zona_fit'
            )
            return conexion
        except Error as e:
            print(f"Error al conectar a MySQL: {e}")
            return None
