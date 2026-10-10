
def sortear(lista):
    num_menor = lista[0]
    pos = 0
    lista_ordenada = []
    while lista:
        num_menor = lista[0]
        pos = 0
        for i in range(len(lista)):
            if (lista[i] < num_menor):
                num_menor = lista[i]
                pos = i
        lista_ordenada.append(num_menor)
        lista.pop(pos)


def test(lista):
    lista.pop()
    return lista
lista = [500,60,100,30,8,7,2,11,3245,6456,342,56,1]
lista2 = [1,2,3]

pepe = test(lista2)
print(lista2,pepe)



lista_nueva = sortear(lista)

print(lista)
print(lista_nueva)




     