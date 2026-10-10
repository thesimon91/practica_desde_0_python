
def elegir_clase():
    print("Que clase quieres elegir?")
    clase = 0
    while clase < 1 or clase > 4:
        clase = int(input("\n1. MAGO \n2.ASESINO \n3.GUERRERO \n4.ARQUERO \n"))
        
        if clase < 1 or clase > 4:
            print("\n\n\nSelecciona correctamente una de las clases")
        if clase == 1:
            print("Clase elegida MAGO")
        elif clase == 2:
            print("Clase elegida ASESINO")
        elif clase == 3:
            print("Clase elegida GUERRERO")
        elif clase == 4:
            print("Clase elegida ARQUERO")
    return clase

def inicio():
    print("Bienvenido")
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre}.")
    clase = elegir_clase()

def chequear_numero_par_en_lista(num_list):
    for number in num_list:
        if number % 2 == 0:
            print("True")
            return True
        else:
            pass
    print("False")
    return False

chequear_numero_par_en_lista([1,3,5,7,9,10])