from typing import Dict, Tuple

def input_choice_keys(options_map: Dict[str, str], message: str = 'Elija una opción') -> str:
    """
    Prompts the user to choose from options using a single-letter key.

    Args:
        options_map: A dictionary where keys are the single-letter input
                     (e.g., 's', 'n') and values are the full option strings
                     (e.g., 'Sí', 'No'). Keys should be unique and ideally
                     single characters.
        message: The prompt message to display to the user.

    Returns:
        The full string of the selected option.
    """
    
    # Prepare the display string for options (e.g., " (s) Sí / (n) No")
    display_options = []
    for key, value in options_map.items():
        display_options.append(f"({key}) {value}")
    
    # Convert keys to lowercase for validation
    valid_keys = {key.lower() for key in options_map.keys()}
    
    while True:
        # Construct the full prompt message
        prompt_message = f"{message} {' / '.join(display_options)}: "
        
        user_input = input(prompt_message).strip().lower() # Read and convert to lowercase
        
        if user_input in valid_keys:
            # Find the original case key to get the correct option string
            for original_key, option_value in options_map.items():
                if original_key.lower() == user_input:
                    return option_value
        else:
            print("❌ Opción no válida. Por favor, ingrese una de las letras indicadas.")

# --- Example Usage ---
if __name__ == "__main__":
    # Example 1: Simple Yes/No
    yes_no_options = {
        's': 'Sí',
        'n': 'No'
    }
    response = input_choice_keys(yes_no_options, "¿Desea continuar?")
    print(f"\nSu respuesta fue: {response}")

    # Example 2: Options with shared initials, resolved by custom keys
    game_menu_options = {
        'j': 'Jugar',
        'c': 'Cargar Partida',
        'o': 'Opciones',
        's': 'Salir',
        'a': 'Acerca de' # 'A' for About, as 's' is taken by Salir
    }
    selected_option = input_choice_keys(game_menu_options, "Menú del Juego")
    print(f"Has elegido: {selected_option}")

    # Example 3: Different options, showing flexibility
    color_options = {
        'r': 'Rojo',
        'v': 'Verde',
        'a': 'Azul',
        'm': 'Amarillo' # 'M' for aMarillo, 'a' taken by Azul
    }
    chosen_color = input_choice_keys(color_options, "Elija su color favorito")
    print(f"Su color favorito es: {chosen_color}")