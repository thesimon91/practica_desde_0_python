from random import randint
import subprocess
import os
import sys

def clean_cmd():
    comand = "cls" if os.name == "nt" else "clear"
    subprocess.run(comand, shell=True)

class Weapons():

    def __init__(self,name,level,dmg,rarity,weapon,xp):
        #Atributos
        self.name = name
        self.level = level
        self.dmg = dmg
        self.rarity = rarity
        self.weapon = weapon
        self.xp = xp

    def gain_xp(self,exp):
        self.xp[0] += exp
        if self.xp[0] >= self.xp[1]:
            self.xp[0] -= self.xp[1]
            self.xp[1] = self.xp[1] * 2
            self.level += 1
            self.dmg[0] += 1
            self.dmg[1] += randint(1,2) 
            print(f"El {self.name} ha subido de nivel!!")
            print(f"LVL: {self.level} | XP: {self.xp[0]}/{self.xp[1]} | DMG: {self.dmg}")

    def hit(self):
        if self.weapon == 4:
            return randint(self.dmg[0], self.dmg[1])


        
class wood_bow (Weapons):
    def __init__(self):
        super().__init__(
            name = "arco_de_madera",
            level=1,
            dmg=[1,4],
            rarity=0,
            weapon=4,
            xp = [0,5]
        )




class Enemy():

    def __init__(self,name,level,hp,dmg,race,res,xp):
        self.name = name
        self.level = level
        self.hp = hp
        self.dmg = dmg
        self.race = race
        self.res = res
        self.xp = xp


    def get_dmg(self,weapon_dmg):
        self.hp -= round(weapon_dmg * (1 - self.res / 100))
        print(f"HIT DMG:{weapon_dmg} | ENEMY HP: {round(self.hp)}")

    def dead(self):
            if self.hp <= 0:
                self.hp = 0
                print(f"{self.name} ha muerto, has ganado {self.xp} de experiencia!!")
                return self.xp
            return 0



  


def goblin_fight(arma,enemigo):
    while enemigo.hp > 0:
        contador = 0
        answer = input(f"Hay un {enemigo.name} en frente tuyo quieres lucharle? (y/n)").lower()
        if answer == "y":
            while enemigo.hp > 0:
                contador += 1
                if contador > 4:
                    print(f"Has perdido, el {enemigo.name} te apuñalo con veneno")
                    sys.exit()
                enemigo.get_dmg(arma.hit())
                if enemigo.hp > 0:
                    print(f"El {enemigo.name} se acerca, debes de matarlo rapido!!!") 
                    input("Presione Enter para volver a disparar...")
            
        elif answer == "n":
            print("\nHuiste del combate.")
            break
        else:
            print("Respuesta mal tipeada, vuelve a intentarlo")
            input("Presione Enter para continuar...")
            clean_cmd()
    if enemigo.hp <= 0:
        arma.gain_xp(enemigo.dead())
        input("Presione Enter para continuar...")
        clean_cmd()
    
   


    