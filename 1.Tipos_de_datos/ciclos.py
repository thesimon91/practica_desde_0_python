"""
mi_lista = [1,2,3,4,5,6,7,8,9,10]

suma_lista = 0

for num in mi_lista:
    #chequear numeros pares
    if num % 2 == 0:
        print(f"Numero par: {num}")
    else:
        print(f"Numero impar: {num}")

for num in mi_lista:
    #Sumar num de la lista
    suma_lista += num
    print(suma_lista)
"""

#for letter in "hola mundo":
#    print(letter)

"""
#Tuple unpacking
mi_lista = [(1,2),(3,4),(5,6),(7,8)]

print(len(mi_lista))

for (a,b) in mi_lista:
    print(a)
    print(b)
"""
"""
d = {"l1":1,"l2":2,"l3":3}

for llave,valor in d.items():
    print(llave,valor)
"""
"""
x = 0

while x < 5:
    x += 1
    print ("Valor actual de x: ",x)
else: 
    print("X NO es mayor que 5")

"""

x = "JUAN DOMINGO PERON"

for letter in x:
    pass



for letter in x:
    if letter == "O":
        continue
    print(letter)

for letter in x:
    if letter == "R":
        break
    print(letter)
