def input_date():
    def val_formato_fecha(fecha): 
        """
        verifica si es 'dd/mm/aaaa' y si son enteros
        """
        if len(fecha) == 10 and fecha[2] == '/' and fecha[5] == '/':
            try:
                dia, mes, anio = int(fecha[:2]), int(fecha[3:5]), int(fecha[6:])
                return dia, mes, anio
            except ValueError:
                return False
            
    while True:
        fecha = input("Ingrese una fecha (dd/mm/aaaa): ")
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        d_m_a = val_formato_fecha(fecha)
        if not d_m_a:
            continue
        dia, mes, anio = d_m_a
        dias_por_mes[1] = 29 if (anio%400 == 0) or (anio%4 == 0 and anio%100 != 0) else 28
        anio_v = True if anio > 0 else False
        if 1 <= mes <= 12:
            mes_v = True
            max_dias = dias_por_mes[mes - 1]
            dia_v = True if 1 <= dia <= max_dias else False
        else:
            continue
        if anio_v and mes_v and dia_v:
            return dia, mes, anio
        
d, m, a = input_date()
print("Fecha ingresada correctamente:")
print(f"Día: {d}, Mes: {m}, Año: {a}")