import re 
from .manager_base import ManagerBase

class PacienteManager:
    def __init__(self, paciente_dni):
        self.paciente_dni = paciente_dni
        self.turno_db = ManagerBase(tabla="Turnos")
        self.paciente_db = ManagerBase(tabla="Paciente") 
        self.persona_db = ManagerBase(tabla="Persona") 
        
        self.medico_db = ManagerBase(tabla="Medico")

    def _get_paciente_id(self):
        try:
            info_persona = self.persona_db.get_by_dni(self.paciente_dni)
            if not info_persona:
                print("Error: No se encontraron los datos de la persona.")
                return None
            
            id_persona = info_persona['id']
            
            info_paciente = self.paciente_db.get_one_by_field('id_persona', id_persona)
            if not info_paciente:
                print("Error: No se encontraron los datos del paciente.")
                return None
                
            return info_paciente['id']
        except Exception as e:
            print(f"Error obteniendo ID del paciente: {e}")
            return None

    def _listar_medico(self):
        print("\n--- Médicos Disponibles ---")
        conn = self.medico_db.conn
        if not conn:
            print("Error de conexión al listar médicos.")
            return None
        
        cursor = conn.cursor()
        query = """
        SELECT 
            ME.id,
            PE.nombre,
            PE.apellido,
            ME.especializacion
        FROM Medico AS ME
        JOIN Persona AS PE ON ME.id_persona = PE.id
        ORDER BY PE.apellido
        """
        
        try:
            cursor.execute(query)
            medicos = cursor.fetchall()
            
            if not medicos:
                print("No hay médicos registrados en el sistema.")
                return None
            
            print("ID | Nombre Completo (Especialización)")
            print("-" * 50)
         
            medicos_lista = [dict(row) for row in medicos]
            for medico in medicos_lista:
                print(f"{medico['id']} | Dr/a. {medico['nombre']} {medico['apellido']} ({medico['especializacion']})")
            return medicos_lista
            
        except Exception as e:
            print(f"Error al listar médicos: {e}")
            return None
        finally:
            cursor.close()

    def ver_mis_turnos(self):
        
        print(f"\n--- Mis Turnos Agendados ---")
        
        id_paciente = self._get_paciente_id()
        if not id_paciente:
            print("No se pudo verificar la información del paciente.")
            return []

       
        conn = self.turno_db.conn
        if not conn: return []
        
        cursor = conn.cursor()
        query = """
        SELECT 
            T.fecha_turno, 
            T.hora,
            T.detalle,
            P_MEDICO.nombre AS nombre_medico, 
            P_MEDICO.apellido AS apellido_medico,
            ME.especializacion  
        FROM Turnos AS T
        JOIN Medico AS ME ON T.id_medico = ME.id
        JOIN Persona AS P_MEDICO ON ME.id_persona = P_MEDICO.id
        WHERE T.id_paciente = ?
        ORDER BY T.fecha_turno, T.hora
        """
        
        try:
            cursor.execute(query, (id_paciente,))
            citas = cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar citas: {e}")
            return []
        finally:
            cursor.close()

        if citas:
            print(f"Total de turnos encontrados: {len(citas)}")
            for i, cita_row in enumerate(citas):
                cita = dict(cita_row) 
                print("-" * 50)
                print(f"Turno {i+1} | Fecha: {cita['fecha_turno']} | Hora: {cita['hora']}")
                print(f"  Médico: Dr. {cita['apellido_medico']} ({cita['especializacion']})")
                if cita['detalle']:
                    print(f"  Detalle: {cita['detalle']}")
        else:
            print("No tienes turnos agendados.")
            
        return citas


    def agendar_turno(self):
        
        print("\n--- Agendar Nuevo Turno ---")
        
        
        id_paciente = self._get_paciente_id()
        if not id_paciente:
            return

        medicos_disponibles = self._listar_medico()
        if not medicos_disponibles:
            print("No es posible agendar un turno en este momento.")
            return

        id_medico_input = input("\nIngrese el ID del médico seleccionado: ").strip()
        
        medico_seleccionado = None
        for med in medicos_disponibles:
            if str(med['id']) == id_medico_input:
                medico_seleccionado = med
                break
        
        if not medico_seleccionado:
            print("Error: ID de médico no válido.")
            return
            
        print(f"Ha seleccionado a: Dr/a. {medico_seleccionado['apellido']} ({medico_seleccionado['especializacion']})")


        while True:
            fecha_input = input("Ingrese la fecha (AAAA-MM-DD): ").strip()
            if re.match(r"^\d{4}-\d{2}-\d{2}$", fecha_input):
                break
            print("Formato de fecha incorrecto. Use AAAA-MM-DD.")
            
        while True:
            hora_input = input("Ingrese la hora (HH:MM): ").strip()
            if re.match(r"^\d{2}:\d{2}$", hora_input):
                hora_input += ":00" 
                break
            print("Formato de hora incorrecto. Use HH:MM.")

      
        detalle_input = input("Ingrese un detalle o motivo (opcional): ").strip()
        
       
        datos_turno = {
            "id_paciente": id_paciente,
            "id_medico": medico_seleccionado['id'],
            "fecha_turno": fecha_input,
            "hora": hora_input,
            "detalle": detalle_input or None,
            "metodo_de_pago": "Particular" 
        }

        id_turno_nuevo = self.turno_db.insert(datos_turno)
        
        if id_turno_nuevo:
            print("\n¡Turno agendado con éxito!")
            print(f"Fecha: {fecha_input} Hora: {hora_input}")
            print(f"Médico: Dr/a. {medico_seleccionado['apellido']}")
        else:
            print("Error: No se pudo agendar el turno.")


    def actualizar_mis_datos(self):
        print(f"\n--- Actualizar mis datos (Paciente {self.paciente_dni}) ---")
        print("Deje el campo vacío y presione ENTER para no cambiar el dato.")

        try:
            info_persona = self.persona_db.get_by_dni(self.paciente_dni)
            if not info_persona:
                print("Error: No se encontraron los datos de la persona.")
                return
            id_persona = info_persona['id']
            print(f"Nombre actual ({info_persona['nombre']})")
            nuevo_nombre = input("Nuevo Nombre: ").strip()
            
            print(f"Apellido actual ({info_persona['apellido']})")
            nuevo_apellido = input("Nuevo Apellido: ").strip()

            telefono_actual = info_persona['telefono'] or 'N/A'
            print(f"Teléfono actual ({telefono_actual})")
            nuevo_telefono = input("Nuevo Teléfono: ").strip()
            
            datos_persona_actualizar = {}
            if nuevo_nombre:
                datos_persona_actualizar['nombre'] = nuevo_nombre
            if nuevo_apellido:
                datos_persona_actualizar['apellido'] = nuevo_apellido
            if nuevo_telefono:
                datos_persona_actualizar['telefono'] = nuevo_telefono
            
            if datos_persona_actualizar:
                if self.persona_db.update(id_persona, datos_persona_actualizar):
                    print("Datos personales actualizados.")
                else:
                    print("Error al actualizar datos personales.")
            else:
                print("ℹNo se ingresó ningún dato nuevo. No se realizó ninguna actualización.")
            
        except Exception as e:
            print(f"Ocurrió un error inesperado durante la actualización: {e}")