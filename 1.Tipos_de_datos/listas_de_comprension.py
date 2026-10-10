"""
cadena = "hola"

mi_lista = []

for letter in cadena:
    mi_lista.append(letter)
print(mi_lista)

"""

# MEJOR FORMA

lista = [x for x in range(0,11)]

celcius = [0,10,20,34.5]
fahrenheit = [((9/5)* temp + 32) for temp in celcius]
print(fahrenheit)

fahrenheit = []

for temp in celcius:
    fahrenheit.append(((9/5)* temp + 32))