import random

PALOS=['⚔️','💘','💎','🍀']
VALORES=['A','1','2','3','4','5','6','7','8','9','JOTA','REINA','REY']


def crear_baraja():
    """
    Esta funcion crea la baraja
    """
    barajas=[]
    for palo in PALOS:
        for valor in VALORES:
            barajas.append((palo,valor))
    return barajas

def obtener_mano(barajas,tamano_mano):
    """
    docstring
    """
    mano=random.sample(barajas,tamano_mano)

    return mano

def main(tamano_mano,intentos):
    """
    docstring
    """
    for _ in range(intentos):
        barajas=crear_baraja()
        mano=obtener_mano(barajas,tamano_mano)
        print(mano)


if __name__ == "__main__":
    tamano_mano=int(input("¿De cuantas cartas sera la mano? "))
    numero_de_intentos=int(input("¿Cuantas veces se correra la simulacion? "))
    main(tamano_mano,numero_de_intentos)