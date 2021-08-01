import random

def aventar_agujas(numero_de_agujas):
    dentro_del_circulo=0
    for _ in range(numero_de_agujas):
        x=random.random()*random.choice([-1,1])
        y=random.random()*random.choice([-1,1])
        