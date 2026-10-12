
class Animal ():
    def __init__(self):
        print("ANIMAL CREADO")

    def quien_soy(self):
        print("Soy un animal")

    def comer(self):
        print("Estoy cominedo")


class Perro(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Perro creado")

        def quien_soy(self):
            print("Soy un Perro")


dog = Perro()