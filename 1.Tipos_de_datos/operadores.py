from random import shuffle,randint
import funciones


"""
lista = [1,2,3]

for num in range(0,11,2):
    print(num)

print(list(range(0,11,2)))

"""
"""
contador_indice = 0
palabra = "hola"

for letter in palabra:
    print(palabra[contador_indice])
    contador_indice += 1

for index,letter in enumerate(palabra):
    print(index,letter)
"""
"""
lista1 = [1,2,3,4,5]
lista2 = ["a","b","c"]
lista3 = [100,200,300,400]
for item in zip(lista1,lista2,lista3):
    print(item)
"""
"""
lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = ["a","b","c"]
d = {"k1":1}
lista3 = [100,200,300]

print(list(zip(lista1,lista2)))

if "a" in lista2:
    print("True")

if "k1" in d:
    print("True")

if 1 in d.keys():
    print("True")
else:
    print("Flase")

print(funciones.valor_min_lista(lista1))
print(funciones.valor_max_lista(lista1))

shuffle(lista1)
print(lista1)
"""
r = input("Escribe un numero: ")


print(type(int(r)))
