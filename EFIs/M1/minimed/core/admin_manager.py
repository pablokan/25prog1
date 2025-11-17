from .manager_base import ManagerBase

class AdminManager:
    def __init__(self, admin_user):
        self.admin_user = admin_user
        self.medico_db = ManagerBase(tabla="Medico")
        self.turno_db = ManagerBase(tabla="Turnos")
        self.persona_db = ManagerBase(tabla="Persona") 

  
    def listar_medico(self):
        print("\n--- Médico Registrado ---")
       
        conn = self.medico_db.conn
        if not conn:
            print("Error de conexión al listar médicos.")
            return
        cursor = conn.cursor()
        query = """
        SELECT 
            ME.id,
            PE.nombre,
            PE.apellido,
            ME.especializacion,
            ME.matricula
        FROM Medico AS ME
        JOIN Persona AS PE ON ME.id_persona = PE.id
        ORDER BY PE.apellido
        """
        try:
            cursor.execute(query)
            medicos = cursor.fetchall() 
            if not medicos:
                print("No hay médicos registrados en el sistema.")
                return
            print(f"Total de médicos: {len(medicos)}")
            print("ID | Apellido, Nombre (Especialización) | Matrícula")
            print("-" * 60)
            for medico in medicos:
                print(f"{medico['id']} | {medico['apellido']}, {medico['nombre']} ({medico['especializacion']}) | {medico['matricula']}")
        except Exception as e:
            print(f"Error al listar médicos: {e}")
        finally:
            cursor.close()

    
    def ver_turnos(self, fecha=None):
        if fecha:
            titulo = f"Turnos por Fecha: {fecha}"
           
            filtro_sql = "WHERE T.fecha_turno = ?"
            params = (fecha,)
        else:
            titulo = "Mostrar TODOS los Turnos"
            filtro_sql = "" 
            params = ()
            
        print(f"\n--- {titulo} ---")
        
        conn = self.turno_db.conn
        if not conn: 
            print("Error de conexión.")
            return []
        
        cursor = conn.cursor()
     
        query = f"""
        SELECT 
            T.fecha_turno, 
            T.hora, 
            P_PACIENTE.nombre AS nombre_paciente, 
            P_PACIENTE.apellido AS apellido_paciente,
            P_MEDICO.nombre AS nombre_medico, 
            P_MEDICO.apellido AS apellido_medico,
            ME.especializacion  
        FROM Turnos AS T
        JOIN Paciente AS PA ON T.id_paciente = PA.id
        JOIN Persona AS P_PACIENTE ON PA.id_persona = P_PACIENTE.id
        JOIN Medico AS ME ON T.id_medico = ME.id
        JOIN Persona AS P_MEDICO ON ME.id_persona = P_MEDICO.id
        {filtro_sql}
        ORDER BY T.fecha_turno DESC, T.hora ASC
        """
    
        try:
            cursor.execute(query, params)
            turnos = cursor.fetchall() 
        except Exception as e:
            print(f"Error al ejecutar la consulta de turnos: {e}") 
            return []
        finally:
            cursor.close()

        if turnos:
            print(f"Total de turnos encontrados: {len(turnos)}")
            for i, turno_row in enumerate(turnos):
                turno = dict(turno_row)
                print("-" * 50)
                print(f"Turno {i+1} | Fecha: {turno['fecha_turno']} Hora: {turno['hora']}")
                print(f"  Paciente: {turno['nombre_paciente']} {turno['apellido_paciente']}")
                print(f"  Médico: Dr. {turno['apellido_medico']} ({turno['especializacion']})")
        else:
            print("No se encontraron turnos bajo este criterio.")
            
        return turnos