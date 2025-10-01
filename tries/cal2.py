import calendar
from rich import print

# Suponiendo que quieres resaltar las vacaciones de agosto
vacaciones_agosto = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

cal_plain = calendar.month(2025, 8)
cal_rich = cal_plain

for dia in vacaciones_agosto:
    # Aseguramos que el reemplazo solo afecte el día y no parte de otro número
    cal_rich = cal_rich.replace(f' {dia} ', f' [bold green]{dia}[/bold green] ')
    # Este caso es para el último día del mes, si no tiene espacio después
    cal_rich = cal_rich.replace(f' {dia}\n', f' [bold green]{dia}[/bold green]\n')

print(cal_rich)
print(1, 'a', True)