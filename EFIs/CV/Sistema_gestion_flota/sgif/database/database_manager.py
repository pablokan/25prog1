import mysql.connector  
import configparser     
from pathlib import Path

class BaseDeDatos:
    def __init__(self, config_file: str | None = None) -> None:
        config = configparser.ConfigParser()

        if config_file is None:
            config_path = Path(__file__).resolve().parent / 'config.ini'
            config_file = str(config_path)

        leer_config = config.read(config_file)
        
        if not leer_config:
            raise FileNotFoundError(f"No se pudo leer el archivo de configuración: {config_file}")
        
        if 'database' not in config:
            raise KeyError("Sección 'database' no encontrada en el archivo de configuración")
        
        self.db_config = {
            'host': config['database']['host'],
            'port': int(config['database']['port']),
            'user': config['database']['user'],
            'password': config['database']['password'],
            'database': config['database']['database']
        }

    def conectar_db(self):
        try:
            self.conexion = mysql.connector.connect(**self.db_config)
            print("Conexión a la base de datos exitosa.")
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos:", error)
            raise

    def desconectar_db(self):
        try:
            if hasattr(self, 'conexion') and self.conexion.is_connected():
                self.conexion.close()
                print("Conexión a la base de datos cerrada.")
        except Exception:
            pass

    def ejecutar_consulta(self, consulta: str, valores: tuple = ()):
        try:
            if not hasattr(self, "conexion") or not self.conexion.is_connected():
                self.conectar_db()

            cursor = self.conexion.cursor(dictionary=True)
            cursor.execute(consulta, valores)

            if consulta.strip().upper().startswith("SELECT"):
                resultados = cursor.fetchall()
                return resultados
            else:
                self.conexion.commit()
                return True

        except mysql.connector.Error as error:
            print("Error al ejecutar la consulta:", error)
            return False

        finally:
            if 'cursor' in locals():
                cursor.close()

if __name__ == '__main__':
    db = BaseDeDatos()
    resultados = db.ejecutar_consulta("SELECT NOW();")
    print("Resultado del SELECT:", resultados)