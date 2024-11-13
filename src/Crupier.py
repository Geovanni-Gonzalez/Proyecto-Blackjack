import Jugador

class Crupier(Jugador):

    def __init__(self, nombre):
        super().__init__(nombre)
        self.mano = []
        self.puntos = 0

    """
    Nombre: calcularPuntaje
    Entradas: ninguna
    Salidas: entero
    Descripción: Calcula el puntaje de la mano del crupier.
    """
    def calcularPuntaje(self):
        puntaje = 0
        ases = 0
        for carta in self.mano:
            if carta.getValor() == 1:
                ases += 1
            puntaje += carta.getValor()
        while puntaje < 12 and ases > 0:
            puntaje += 10
            ases -= 1
        return puntaje

