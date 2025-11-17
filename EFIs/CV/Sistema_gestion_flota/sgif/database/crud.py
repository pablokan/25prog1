from sgif.database.database_manager import BaseDeDatos

class CRUD:
    nombre_tabla = ''
    columnas = ()

    def __init__(self) -> None:
        self.db = BaseDeDatos()

    def insertar(self, valores: tuple):
        if len(valores) != len(self.columnas):
            raise ValueError(f"Número de valores ({len(valores)}) no coincide con columnas ({len(self.columnas)})")
        
        columnas_sql = ', '.join(self.columnas)
        cant_valores = ', '.join('%s' for _ in valores)
        consulta = f'INSERT INTO {self.nombre_tabla} ({columnas_sql}) VALUES ({cant_valores})'
        self.db.ejecutar_consulta(consulta, valores)
    
    def obtener_datos(self, columna = None, valor = None):
        if columna is not None and valor is not None:
            consulta = f"SELECT * FROM {self.nombre_tabla} WHERE {columna} = %s"
            valores = (valor,)
        else:
            consulta = f"SELECT * FROM {self.nombre_tabla}"
            valores = ()

        resultados = self.db.ejecutar_consulta(consulta, valores)
        return resultados
    
    def listar_columnas(self, *columnas):
        columnas_sql = ', '.join(columnas)
        consulta = f'SELECT {columnas_sql} FROM {self.nombre_tabla}'
        resultados = self.db.ejecutar_consulta(consulta, ())
        return resultados

    def actualizar(self, columna_objetivo, nuevo_dato, columna_clave, valor_clave):
        consulta = f"UPDATE {self.nombre_tabla} SET {columna_objetivo} = %s WHERE {columna_clave} = %s"
        valores = (nuevo_dato, valor_clave)
        self.db.ejecutar_consulta(consulta, valores)

    def eliminar(self, columna_clave, valor_clave, restaurar = False):
        columna_estado = 'activo' if 'activo' in self.columnas else 'eliminado'
        consulta = f"UPDATE {self.nombre_tabla} SET {columna_estado} = %s WHERE {columna_clave} = %s"
        valores = (0 if not restaurar else 1, valor_clave)
        self.db.ejecutar_consulta(consulta, valores)

class Vehiculo(CRUD):
    nombre_tabla = 'vehiculos'
    columnas = ('modelo_id', 'patente', 'n_chasis', 'n_motor', 'comb_id', 'anio',
                'fecha_adquisicion', 'km_adquisicion', 'km_actual', 'estado_id', 'empresa_aseguradora', 'n_poliza')

    def obtener_datos(self, columna, valor):
        consulta = f"""
            SELECT 
                v.vehiculo_id,
                v.patente,
                m.nombre AS marca,
                mo.nombre AS modelo,
                t.nombre AS tipo_vehiculo,
                c.tipo_comb AS combustible,
                v.anio,
                v.fecha_adquisicion,
                v.km_actual,
                e.nombre AS estado,
                v.empresa_aseguradora,
                v.n_poliza
            FROM vehiculos v
            INNER JOIN modelos_vehiculos mo ON v.modelo_id = mo.modelo_id
            INNER JOIN marcas_vehiculos m ON mo.marca_id = m.marca_id
            INNER JOIN tipo_vehiculos t ON mo.tipo_id = t.tipo_id
            INNER JOIN combustibles c ON v.comb_id = c.comb_id
            INNER JOIN estado_vehiculo e ON v.estado_id = e.estado_id
            WHERE v.{columna} = %s
        """
        return self.db.ejecutar_consulta(consulta, (valor,))

class Persona(CRUD):
    nombre_tabla = 'personas'
    columnas = ('nombre', 'edad')

class Modelo(CRUD):
    nombre_tabla = 'modelos_vehiculos'
    columnas = ('nombre', 'marca_id', 'tipo_id')

class Marca(CRUD):
    nombre_tabla = 'marcas_vehiculos'
    columnas = ('nombre',)

class Estado(CRUD):
    nombre_tabla = 'estado_vehiculo'
    columnas = ('nombre',)