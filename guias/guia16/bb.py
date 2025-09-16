mi_lista = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
objetivo = 8

def b_b_con_indice(lista, objetivo, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1

    if inicio > fin:
        return 'El elemento no está en la lista'
    
    m = (inicio + fin) // 2

    if objetivo == lista[m]:
        return f'Encontrado en la posición {m}'
    elif objetivo < lista[m]:
        return b_b_con_indice(lista, objetivo, inicio, m - 1)
    else:
        return b_b_con_indice(lista, objetivo, m + 1, fin)

print(b_b_con_indice(mi_lista, objetivo))