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

def ajustar_bisiesto(dma):
    

d_m_a = val_formato_fecha('03/06/1965')
if not d_m_a:
    print('mal')
else:
    print(d_m_a)