

def func(a,b):
    #retornar el 5% de la suma de a y b
    return sum((a,b)) * 0.05

print(func(40,50))

def func2(*args):
    print(args)
    return sum(args) * 0.05
print(func2(40,50,90,9000,31))