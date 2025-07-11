# Sobreescribe los caracteres en la posición dada
with open('archivos/MOCK_DATA.csv', 'r+') as f:
    f.seek(200)  # Ir a la posición exacta
    f.write('Federico')
