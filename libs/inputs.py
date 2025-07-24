from typing import Literal
infinite = float('inf')  # python infinite

def input_number(
        data_type: Literal["entero", "real"] , 
        msg="Ingrese un número", 
        min_val=-infinite, 
        max_val=infinite
) -> float | int:
    
    msg_suffix = ''
    num_type = {'entero': int, 'real': float}
    if min_val != -infinite and max_val != infinite:
        msg_suffix = f'(entre {min_val} y {max_val})'
    elif min_val != -infinite:
        msg_suffix = f'(mayor o igual a {min_val})'
    elif max_val != infinite:
        msg_suffix = f'(menor o igual a {max_val})'
    full_msg = f'{msg} {msg_suffix}: '
    user_input: str
    numero: int|float = 0
    validated = False
    while not validated:
        user_input = input(full_msg)
        try:
            numero = num_type[data_type](user_input)
            if min_val <= numero <= max_val:
                validated = True
            else:
                print('valor fuera de rango') 
        except ValueError:
            print(f"Error. Debe ingresar un número {data_type}.")
    return numero

def input_choice(options: str, msg: str = 'Elija una opción') -> str:
    options_list = options.split('/')
    print(f"\n{msg} ", end='')
    for i, option in enumerate(options_list):
        print(f"{i + 1}){option}", end=' - ')

    valid_choices = [str(i + 1) for i in range(len(options_list))]
    choice_index = -1
    validated = False
    while not validated:
        user_input = input(f"(1-{len(options_list)}): ").strip()
        if user_input in valid_choices:
            choice_index = int(user_input) - 1
            validated = True
        else:
            print("Opción inválida.", end=' ')
    return options_list[choice_index]

def input_str(msg, min=0, max=infinite) -> str:
    validated = False
    s: str = ''
    while not validated:
        s = input(msg)
        if min <= len(s) <= max:
            validated = True
    return s

if __name__ == "__main__":
    altura = input_number('real', 'Altura', 1.2, 2.5)
    #edad = input_number('entero', 'Edad', 0, 200)
    #edad = input_number('entero', 'Edad', 0)
    #negativo = input_number('qq', 'Ingresa un negativo', max_val=-1)
    #print(negativo)
    

