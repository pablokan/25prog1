"""
12:00 am
12:15 am
.
.
.
11:30 pm
11:45 pm
"""

h = 12
ampm = "am"
ms = ["00", "15", "30", "45"]
c = 0
for linea in range(96):
    ampm = "am" if linea < 48 else "pm"
    print(f'{h}:{ms[c]} {ampm}')
    c += 1
    if c == 4:
        c = 0
        h += 1
        if h == 13:
            h = 1
    

    
