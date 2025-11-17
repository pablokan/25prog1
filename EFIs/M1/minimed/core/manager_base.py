from database.connection import get_connection, close_connection

class ManagerBase:
    
    def __init__(self, tabla):
        self.tabla = tabla
        self.conn = get_connection() 

    def __del__(self):
        close_connection(self.conn)

    def _execute_query(self, query, params=(), fetch_one=False, fetch_all=False, commit=False):
        if not self.conn:
            print("Error: No hay conexión a la base de datos.")
            return None
        
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            
            if commit:
                self.conn.commit()
                return cursor.lastrowid
            
            if fetch_one:
                return cursor.fetchone()
            
            if fetch_all:
                return cursor.fetchall()
            
            if not fetch_one and not fetch_all:
                 self.conn.commit()
                 return cursor.rowcount

        except Exception as e:
            print(f"Error al ejecutar consulta en {self.tabla}: {e}")
            if commit:
                self.conn.rollback()
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()

    def get_by_id(self, id_val):
        query = f"SELECT * FROM {self.tabla} WHERE id = ?"
        return self._execute_query(query, (id_val,), fetch_one=True)
        
    def get_all(self):
        query = f"SELECT * FROM {self.tabla}"
        return self._execute_query(query, fetch_all=True)
    
    def get_by_dni(self, dni_val):
        if self.tabla != "Persona":
            print(f"Método get_by_dni solo debe usarse con la tabla Persona, no {self.tabla}.")
            return None
        query = f"SELECT * FROM {self.tabla} WHERE dni = ?"
        return self._execute_query(query, (dni_val,), fetch_one=True)
    
    def get_one_by_field(self, field_name, field_value):
        query = f"SELECT * FROM {self.tabla} WHERE {field_name} = ?"
        return self._execute_query(query, (field_value,), fetch_one=True)

    def insert(self, datos):
        try:
            columnas = ", ".join(datos.keys())
            valores = tuple(datos.values())
            marcadores = ", ".join(["?"] * len(datos))
            
            query = f"INSERT INTO {self.tabla} ({columnas}) VALUES ({marcadores})"
            
            return self._execute_query(query, valores, commit=True)
            
        except Exception as e:
            print(f"Error al construir el INSERT en {self.tabla}: {e}")
            return False
    def update(self, id_val, datos):
        if not datos:
            print("UPDATE: No hay datos para actualizar.")
            return False
            
        try:
            set_clause = ", ".join([f"{key} = ?" for key in datos.keys()])
            valores = tuple(datos.values()) + (id_val,)
            
            query = f"UPDATE {self.tabla} SET {set_clause} WHERE id = ?"
            filas_afectadas = self._execute_query(query, valores)
            
            if filas_afectadas is not None and filas_afectadas > 0:
                print(f"Registro {id_val} en {self.tabla} actualizado con éxito.")
                return True
            else:
                print(f"ℹ️ No se actualizó ningún registro en {self.tabla} (ID: {id_val}).")
                return False
                
        except Exception as e:
            print(f"Error al construir el UPDATE en {self.tabla}: {e}")
            return False
    def delete(self, id_val):
        query = f"DELETE FROM {self.tabla} WHERE id = ?"
        
        filas_afectadas = self._execute_query(query, (id_val,))
        if filas_afectadas is not None and filas_afectadas > 0:
            print(f"Registro {id_val} eliminado de {self.tabla} con éxito.")
            return True
        else:
            print(f"No se eliminó ningún registro en {self.tabla} (ID: {id_val}).")
            return False