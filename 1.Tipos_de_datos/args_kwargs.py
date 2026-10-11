

def func(a,b):
    #retornar el 5% de la suma de a y b
    return sum((a,b)) * 0.05

print(func(40,50))

def func2(*args):
    print(args)
    return sum(args) * 0.05
print(func2(40,50,90,9000,31))

def func3(**kwargs):
    if "fruit" in kwargs:
        print(f"Mi fruta escogida es: {kwargs["fruit"]}")
    else:
        print("No hay fruta")

func3(fruit = "manzana", veggie = "lechuga")

def func4(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f"Me gustaria {args[3]} unidades de {kwargs["comida"]} para mi {kwargs["animal"]} {kwargs["nombre_animal"]}")
func4(10,30,50,4, fruta = "naranja", comida = "Whiskas", animal = "gato", nombre_animal = "Pepito")
    