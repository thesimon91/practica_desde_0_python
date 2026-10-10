def valor_min_lista(lista):
    menor = lista[0]
    for item in lista:
        if item < menor:
            menor = item
    return menor

def valor_max_lista(lista):
    mayor = lista[0]
    for item in lista:
        if item > mayor:
            mayor = item
    return mayor

