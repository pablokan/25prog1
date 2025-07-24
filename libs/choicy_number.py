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

if __name__ == "__main__":
    menu_options = "Iniciar Juego/Cargar Partida/Opciones/Salir"
    selected_option = input_choice(menu_options, "Menú Principal")
    print(f"\nHas elegido: {selected_option}")

    yes_no_options = "Sí/No"
    response = input_choice(yes_no_options, "¿Desea continuar?")
    print(f"Su respuesta fue: {response}")