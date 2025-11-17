class Turno:
    def __init__(self, id_turno, fecha, hora, id_medico, paciente_info):
        self.__id = id_turno
        self.__fecha = fecha
        self.__hora = hora
        self.__id_medico = id_medico
        self.paciente_info = paciente_info 

    def __str__(self):
        paciente_nombre = self.paciente_info.get('nombre_completo', 'Desconocido')
        return f"Turno {self.__id} | Fecha: {self.__fecha} {self.__hora} | Dr. ID: {self.__id_medico} | Paciente: {paciente_nombre}"
        
    def get_detalles(self):
        return {
            'id': self.__id, 
            'fecha': self.__fecha, 
            'hora': self.__hora,
            'medico_id': self.__id_medico
        } 