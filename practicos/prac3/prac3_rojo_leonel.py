#Practico 3

nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

personas_nacidas2018 = [
    {"rank": 1, "nombre": "Liam", "cantidad": 19837, "sexo": "m"},
    {"rank": 1, "nombre": "Emma", "cantidad": 18688, "sexo": "f"},
    {"rank": 2, "nombre": "Noah", "cantidad": 18267, "sexo": "m"},
    {"rank": 2, "nombre": "Olivia", "cantidad": 17921, "sexo": "f"},
    {"rank": 3, "nombre": "Michael", "cantidad": 14516, "sexo": "m"},
    {"rank": 3, "nombre": "Ava", "cantidad": 14924, "sexo": "f"},
    {"rank": 4, "nombre": "James", "cantidad": 13525, "sexo": "m"},
    {"rank": 4, "nombre": "Isabella", "cantidad": 14464, "sexo": "f"},
    {"rank": 5, "nombre": "Oliver", "cantidad": 13389, "sexo": "m"},
    {"rank": 5, "nombre": "Sophia", "cantidad": 13928, "sexo": "f"}
]

elementos_de_nacidos2008 = nacidos2008.split(",")
personas_nacidas2008 = []

for i in range(0, len(elementos_de_nacidos2008), 3):
    nombre = elementos_de_nacidos2008[i]
    cantidad = elementos_de_nacidos2008[i+1]
    sexo = elementos_de_nacidos2008[i+2]
    personas_nacidas2008.append({"nombre": nombre, "cantidad": cantidad, "sexo": sexo})

#Esto es lo que pude averiguar de la funcion sort, y lo utilice para ordenar a las personas por "cantidad de nacidos"
personas_nacidas2008.sort(key = lambda persona: int(persona["cantidad"]), reverse=True)

rank_m = 1
rank_f = 1

top5_m_2008 = []
top5_f_2008 = []

for persona in personas_nacidas2008:
    if persona["sexo"] == "m" and len(top5_m_2008) < 5:
        top5_m_2008.append({
            "rank": rank_m,
            "nombre": persona["nombre"],
            "cantidad": int(persona["cantidad"]),
            "sexo": persona["sexo"]
        })
        rank_m += 1
    elif persona["sexo"] == "f" and len(top5_f_2008) < 5:
        top5_f_2008.append({
            "rank": rank_f,
            "nombre": persona["nombre"],
            "cantidad": int(persona["cantidad"]),
            "sexo": persona["sexo"]
        })
        rank_f += 1

#La diferencia en cantidad de bebés que existe entre los nombres de misma posición y mismo sexo.

solicitud_posicion = int(input("Ingrese la posicion del rank(1-5): "))
solicitud_sexo = input("Ingrese el sexo del rank solicitado(m/f): ")

for persona2018 in personas_nacidas2018:
    if persona2018["sexo"] == solicitud_sexo and persona2018["rank"] == solicitud_posicion:
        if solicitud_sexo == "m":
            for persona2008 in top5_m_2008:
                if persona2008["sexo"] == solicitud_sexo and persona2008["rank"] == solicitud_posicion:
                    diferencia = persona2008["cantidad"] - persona2018["cantidad"]
                    print(f"Varones en posición #{persona2018['rank']}: {diferencia} es la diferencia de 2008 {persona2008['nombre']} sobre {persona2018['nombre']} del 2018.")
        if solicitud_sexo == "f":
            for persona2008 in top5_f_2008:
                if persona2008["sexo"] == solicitud_sexo and persona2008["rank"] == solicitud_posicion:
                    diferencia = persona2008["cantidad"] - persona2018["cantidad"]
                    print(f"Mujeres en posición #{persona2018['rank']}: {diferencia} es la diferencia de 2008 {persona2008['nombre']} sobre {persona2018['nombre']} del 2018.")

#Los nombres de todos los bebés que comienzan con la misma letra considerando ambos periodos.

solicitud_letra = input("Ingrese la letra inicial de los nombres (En mayuscula): ")
nombres_con_letra = []

for persona in personas_nacidas2008:
    if persona["nombre"][0] == solicitud_letra:
        if persona["nombre"] not in nombres_con_letra:
            nombres_con_letra.append(persona["nombre"])

for persona in personas_nacidas2018:
    if persona["nombre"][0] == solicitud_letra:
        if persona["nombre"] not in nombres_con_letra:
            nombres_con_letra.append(persona["nombre"])

print(f"Nombres con {solicitud_letra}: ", end = "")
for nombre in nombres_con_letra:
    print(nombre, end=" ")
print()

#Los nombres que se repiten en ambos años.

nombres_que_se_repiten = []

for persona2018 in personas_nacidas2018: 
    for persona2008 in personas_nacidas2008:
        if persona2018["nombre"] == persona2008["nombre"]:
            if persona2018["nombre"] not in nombres_que_se_repiten:
                nombres_que_se_repiten.append(persona2018["nombre"])

print("Nombres que se repiten: ", end = "")
for nombre in nombres_que_se_repiten:
    print(nombre, end=" ")