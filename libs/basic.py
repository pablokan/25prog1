# Funciones generales
import sys
import os
from typing import Literal

def raya(ubicacion:Literal['inicio', 'fin']|str='', caracter: str='-', longitud:int=80):
    file_name = os.path.basename(sys.argv[0])[:-3]
    if ubicacion == 'inicio':
        cartel = f' Programa {file_name} '
    elif ubicacion == 'fin':
        cartel = f' Fin de {file_name} '
    else:
        cartel = ubicacion
    
    media_raya = f'{caracter*((longitud-len(cartel))//2)}'
    print(f'\n{media_raya}{cartel}{media_raya}\n')


if __name__ == '__main__':
    raya('inicio')
