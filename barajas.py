import collections
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
    barajas=crear_baraja()

    manos=[]
    for _ in range(intentos):
        mano=obtener_mano(barajas,tamano_mano)
        manos.append(mano)
    pares=0
    tercia=0
    poker=0
    corrida=0
    corrida_color=0
    for mano in manos:
        valores=[]
        for carta in mano:
            valores.append(carta[1])
        counter = dict(collections.Counter(valores))
        for val in counter.values():
            if val ==2:
                pares+=1
                break
            elif val == 3:
                tercia+=1
                break
            elif val == 4:
                poker+=1
                break
        lista_corrida=[]
        for keys in counter.keys():
            lista_corrida.append( VALORES.index(keys))
        lista_corrida.sort()
        if len(lista_corrida)==5:
            
            if (lista_corrida[0]+1)== lista_corrida[1] and (lista_corrida[0]+2)== lista_corrida[2] and (lista_corrida[0]+3)== lista_corrida[3] and (lista_corrida[0]+4)== lista_corrida[4]:
                corrida+=1
                if mano[0][0] == mano[1][0] and mano[1][0] == mano[2][0] and mano[2][0] == mano[3][0]  and mano[3][0] == mano[4][0]:
                    print(mano)
                    print(mano[0][0])
                    corrida_color+=1

    probabilidad_pares= pares/intentos
    probabilidad_tercias=tercia/intentos
    probabilidad_poker=poker/intentos
    probabilidad_corrida=corrida/intentos
    probabilidad_corrida_color=corrida_color/intentos

    print(f'La probabilidad de obtener un par en una mano de {tamano_mano} cartas es {probabilidad_pares},Pares en la simulacion {pares} en {intentos} intentos')
    print(f'La probabilidad de obtener una tercia en una mano de {tamano_mano} cartas es {probabilidad_tercias},tercias en la simulacion {tercia} en {intentos} intentos')
    print(f'La probabilidad de obtener un poker en una mano de {tamano_mano} cartas es {probabilidad_poker},full house en la simulacion {poker} en {intentos} intentos')
    print(f'La probabilidad de obtener un corrida de numeros en una mano de {tamano_mano} cartas es {probabilidad_corrida},corridas en la simulacion {corrida} en {intentos} intentos')
    print(f'La probabilidad de obtener un corrida de color de numeros en una mano de {tamano_mano} cartas es {probabilidad_corrida_color},corridas en la simulacion {corrida_color} en {intentos} intentos')



if __name__ == "__main__":
    tamano_mano=int(input("¿De cuantas cartas sera la mano? "))
    numero_de_intentos=int(input("¿Cuantas veces se correra la simulacion? "))
    main(tamano_mano,numero_de_intentos)