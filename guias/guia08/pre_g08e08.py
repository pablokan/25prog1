def input_date():
    def validar():
        dias_por_mes[1] = 29 if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0) else 28
        anio_v = True if anio > 0 else False
        mes_v = True if 1 <= mes <= 12 else False
        max_dias = dias_por_mes[mes - 1]
        dia_v = True if 1 <= dia <= max_dias else False
        
        if anio_v and mes_v and dia_v:
            return True

    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    validado = False
    while not validado:
        fecha = input("Ingrese una fecha (dd/mm/aaaa): ")
        
            if validar():
                validado = True
    return dia, mes, anio

d, m, a = input_date()
print("Fecha ingresada correctamente:")
print(f"Día: {d}, Mes: {m}, Año: {a}")