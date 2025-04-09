edad = 25
if edad < 12:
    print('es un niño')
elif edad >=12 and edad <20:
    print('es un adolescente')
elif edad >=20 and edad <=40:
    print('es un joven')
elif edad >40 and edad <=58:
    print('es un adulto')
else:
    print('es un anciano')      

# mismo resultado con match
edad = 25
match edad:
    case _ if edad < 12:
        print('es un niño')
    case _ if 12 <= edad < 20:
        print('es un adolescente')
    case _ if 20 <= edad <= 40:
        print('es un joven')
    case _ if 40 < edad <= 58:
        print('es un adulto')
    case _:
        print('es un anciano')
        