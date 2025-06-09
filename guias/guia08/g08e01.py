def concatenar(*args, conector=' '):
    return conector.join(args)


print(concatenar('hola', 'pibe'))
print(concatenar('hola', 'pibe', conector='@'))
print(concatenar('techo', 'mesa', 'árbol', conector='###'))
print(concatenar('techo', 'mesa', 'árbol', conector='|||||||'))
