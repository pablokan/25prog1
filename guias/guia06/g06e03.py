amigos = {'pela': 1.78, 'luke': 1.85, 'luis': 1.70, 'jimmy': 1.83}
print(len(amigos))
for nombre, altura in amigos.items():
    mensaje = ''
    if altura > 1.8:
        mensaje = '(es alto)'
    print(f'{nombre} mide {altura} {mensaje}')