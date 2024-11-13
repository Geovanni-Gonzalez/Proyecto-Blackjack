"""
Clase Jugadorde Blackjack
"""
class Jugador:

    def __init__(self, nombre,dinero=1000, ia=False):
        self.nombre = nombre
        self.ia = ia
        self.mano = []
        self.puntos = 0
        self.dinero = dinero

    """
    Nombre: getNombre
    Descripción: Obtiene el nombre del jugador
    """
    def getNombre(self):
        return self.nombre
    """
    Nombre: getMano
    Descripción: Obtiene la mano del jugador
    """
    def getMano(self):
        return self.mano
    
    """
    Nombre: getPuntos
    Descripción: Obtiene los puntos del jugador
    """
    def getPuntos(self):
        return self.puntos
    
    """
    Nombre: getDinero
    Descripción: Obtiene el dinero del jugador
    """
    def getDinero(self):
        return self.dinero

    """
    Nombre: setNombre
    Descripción: Establece el nombre del jugador
    """
    def setNombre(self, nombre):
        self.nombre = nombre

    """
    Nombre: setMano
    Descripción: Establece la mano del jugador
    """
    def setMano(self, mano):
        self.mano = mano

    """
    Nombre: setPuntos
    Descripción: Establece los puntos del jugador
    """

    def setPuntos(self, puntos):
        self.puntos = puntos

    """
    Nombre: setDinero
    """
    def setDinero(self, dinero):
        self.dinero = dinero

    """
    Nombre: calcularPuntaje
    Entradas: ninguna
    Salidas: entero
    Descripción: Calcula el puntaje de la mano del jugador.
    """
    def calcularPuntaje(self):
        puntaje = sum([carta.getValor() for carta in self.mano])
        ases = len([carta for carta in self.mano if carta.valor == 'A'])
        while puntaje > 21 and ases > 0:
            puntaje -= 10
            ases -= 1
        return puntaje
    
    """
    Nombre: hit
    Entradas: Carta
    Salidas: ninguna
    Descripción: Recibe una carta y la agrega a la mano del jugador.
    """
    def hit(self, carta):
        self.mano.append(carta)
        self.puntos = self.calcularPuntaje()

    """
    Nombre: stand
    Entradas: ninguna
    Salidas: ninguna
    Descripción: El jugador se planta.
    """
    def stand(self):
        pass

    """
    Nombre: apostar
    Entradas: entero
    Salidas: ninguna
    Descripción: El jugador apuesta una cantidad de dinero.
    """
    def apostar(self, cantidad):
        self.dinero -= cantidad
    

    """
    Nombre: doblar
    Entradas: entero
    """
    def doblar(self, cantidad):
        pass
    
    
    """
    Nombre: decisionIA
    Entradas: mazo
    Salidas: string
    Descripción: Toma una decisión de pedir otra carta o plantarse.
    """
    def decisionIA(self, mazo):
        pass
