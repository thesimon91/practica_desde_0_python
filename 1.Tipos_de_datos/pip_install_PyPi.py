import POO



arco_de_madera = POO.wood_bow()

goblin = POO.Enemy(name="Goblin",level=1,hp=10,dmg=[0,2],race=1,res=5,xp = 5)
goblin2 = POO.Enemy(name="Goblin",level=1,hp=10,dmg=[0,2],race=1,res=5,xp = 5)
goblin3 = POO.Enemy(name="Goblin",level=2,hp=13,dmg=[1,3],race=1,res=8,xp = 7)
goblin4 = POO.Enemy(name="Goblin",level=2,hp=15,dmg=[1,4],race=1,res=10,xp = 10)
goblin5 = POO.Enemy(name="Goblin",level=3,hp=22,dmg=[2,5],race=1,res=11,xp = 15)
goblin_elite = POO.Enemy(name="Goblin Elite",level=5,hp=30,dmg=[4,9],race=1,res=15,xp = 25)

POO.goblin_fight(arco_de_madera,goblin)
POO.goblin_fight(arco_de_madera,goblin2)
POO.goblin_fight(arco_de_madera,goblin3)
POO.goblin_fight(arco_de_madera,goblin4)
POO.goblin_fight(arco_de_madera,goblin5)
POO.goblin_fight(arco_de_madera,goblin_elite)

