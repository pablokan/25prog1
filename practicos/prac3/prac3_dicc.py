nacidos2008 = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

nacidos2008 = nacidos2008.split(',') 
ddatos2008 = {'f': {}, 'm': {}}


for i in range(0, len(nacidos2008), 3):
    nombre = nacidos2008[i]
    cantidad = int(nacidos2008[i+1])
    sexo = nacidos2008[i+2]
    ddatos2008[sexo][cantidad] = nombre

#print(ddatos2008)
d = {17039: 'Eva', 17434: 'Emily', 18813: 'Emma', 18616: 'Julia', 17081: 'Olivia'}
dd = sorted(d.items(), reverse=True)
print(dd)