from abc import abstractproperty
import random
from statistics import mean

def random_walk_2(steps):
    """
    Regresa las coordenadas despues de caminar "steps" 

    """
    x,y=0,0
    for i in range(steps):
        (dx,dy)=random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y += dy
    return (x,y)


def main(simulations):
    mean_walked=[0]
    steps=1
    while mean(mean_walked)<=4:
        steps+=1
        for i in range (simulations):
            walk=random_walk_2(steps)
            distance_from_home=abs(walk[0])+abs(walk[0])
            #print(walk,f"Distancia caminada desde tu casa {distance_from_home}")
            mean_walked.append(distance_from_home)

    return mean(mean_walked),steps

if __name__ == "__main__":
    simulations=int(input("Ingrese el numero de veces que se hara la simulacion"))
    promedio, pasos= main(simulations)
    print(promedio,f'El maximo numero de pasos en el que el promedio de distancia es 4 o menor es de {pasos}')



     
