import random

def random_walk(steps):
    """
    return coordinates after "Steps " block random wals
    """
    x=0
    y=0 
    for i in range (steps):
        step = random.choice(['N','S','W','E'])
        if step == 'N':
            y+=1
        elif step == 'S':
            y-=1
        elif step == 'E':
            x+=1
        elif step == 'W':
            x-=1
    return x,y

    
if __name__ == "__main__":
    steps=int(input("Ingrese el numero de pasos que dara" ))
    n_simulations=int(input("Ingrese el numero de simulaciones que se haran" ))
    for i in range(n_simulations):
        distance=random_walk(steps)
        print(distance,f"La distancia caminada desde tu casa es de {abs(distance[0])+ abs(distance[1])} ")

    
    