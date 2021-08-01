class Campo:
    """
    Esta clase define el campo por el cual se movera el borracho
    """
    def __init__(self):
        """
        docstring
        """
        self.coordenadas_de_borrachos = {}

    def anadir_borracho(self,borracho,coordenada):
        self.coordenadas_de_borrachos[borracho] = coordenada

    def mover_borracho(self,borracho):
        delta_x, delta_y = borracho.camina()

        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada=coordenada_actual.mover(delta_x,delta_y)

        self.coordenadas_de_borrachos[borracho] = nueva_coordenada
    

    def obtener_coordenada(self,borracho):
        return self.coordenadas_de_borrachos[borracho]