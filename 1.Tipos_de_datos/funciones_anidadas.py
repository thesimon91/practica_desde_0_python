
#GLOBAL
name = "VARIABLE GLOBAL"

def saludo():
    #ENCLOSING
    name = "Pepe Argento"

    def hola():
        #LOCAL
        name = "Variable Local"
        print("Hola " + name)
    hola()


#saludo()


# REASIGNAR VARIABLES

x = 50

def func():
    global x
    print(f"X es {x}")
    #Re Aignacion Local
    x = "NUEVO VALOR"
    print(f"Fui localmente cambiada de X a {x}")
func()
print(x)
