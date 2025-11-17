# database/connection.py

import sqlite3
import os

def get_connection():
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(current_dir, 'minimed_local.db')
        
        connection = sqlite3.connect(db_path)
        connection.row_factory = sqlite3.Row 
        
        return connection
    except sqlite3.Error as e:
        print(f"Error al conectar a SQLite: {e}")
        return None

def close_connection(connection):
    if connection:
        connection.close()

def init_database():
    try:
        connection = get_connection()
        if connection:
            cursor = connection.cursor()
            current_dir = os.path.dirname(os.path.abspath(__file__))
            sql_file_path = os.path.join(current_dir, 'db_local_sqlite.sql')
            
            with open(sql_file_path, 'r', encoding='utf-8') as sql_file:
                sql_script = sql_file.read()
            
            for statement in sql_script.split(';'):
                if statement.strip():
                    try:
                        cursor.execute(statement)
                    except sqlite3.Error as e:
                        if "already exists" not in str(e):
                            print(f"Error en sentencia: {statement}")
                            print(f"Error: {e}")
            
            connection.commit()
            print("Base de datos inicializada correctamente")
            
            cursor.close()
            close_connection(connection)
            
    except sqlite3.Error as e:
        print(f"Error al inicializar la base de datos: {e}")

def test_connection():
    try:
        print("Inicializando la base de datos...")
        init_database()
        print("\nProbando la conexión...")
        connection = get_connection()
        
        if connection:
            cursor = connection.cursor()
            
            cursor.execute("SELECT sqlite_version()")
            db_version = cursor.fetchone()
            print(f"Conectado a SQLite versión: {db_version[0]}")
            
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = cursor.fetchall()
            print("\nTablas creadas en la base de datos:")
            for table in tables:
                print(f"- {table[0]}")
            
            cursor.close()
            close_connection(connection)
            print("\nPrueba de conexión completada con éxito")
            
    except sqlite3.Error as e:
        print(f"Error durante la prueba: {e}")

if __name__ == "__main__":
    test_connection()