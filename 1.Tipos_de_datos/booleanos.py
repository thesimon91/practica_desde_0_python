
def vida(life,life_base):
    print(f"Vida actual: {life}/{int(life_base)}")
life_base = 100
life = 100
vida(life,life_base)
print("EVENTO")
respuesta = input("Deseas pasar por la puerta misteriosa? (y/n)")
if respuesta == "y":
    life -= 20
    print("Te han dañado pero a cambio obtuviste un amuleto de aumento del %20 de vida maxima!!")
    life_base = (life_base * 0.20 + life_base)
    vida(life,life_base)
elif respuesta == "n":
    print ("Siga nomas")


     
