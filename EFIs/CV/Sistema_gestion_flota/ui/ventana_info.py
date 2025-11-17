from screeninfo import get_monitors

ANCHO_MONITOR = 0
ALTO_MONITOR = 0

for info in get_monitors():
    ANCHO_MONITOR = info.width
    ALTO_MONITOR = info.height

ANCHO_BOTONES_PRINCIPALES = ANCHO_MONITOR / 9
ALTO_BOTONES_PRINCIPALES = ALTO_MONITOR / 9

VENTANA_ACTUAL = 'moviles'