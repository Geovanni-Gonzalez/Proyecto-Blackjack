"""
Clase Jugadorde Blackjack
"""
class Jugador:

    def __init__(self, nombre,fichas=1000, ia=False):
        self.nombre = nombre
        self.ia = ia
        self.mano = []
        self.puntos = 0
        self.fichas=fichas
        self.apuestaActual=0

    """
    Nombre: getNombre
    Descripción: Obtiene el nombre del jugador
    """
    def getNombre(self):
        return self.nombre
    

    """
    Nombre: getIA
    Descripción: Obtiene si el jugador es una IA
    """
    def getIA(self):
        return self.ia
    
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
    Nombre: getApuesta
    Descripcion: Obtiene la apuesta actual del jugador
    """
    def getApuesta(self):
        return self.apuestaActual

    """
    Nombre: getFichas
    Descricion: Obtiene las fichas del jugador
    """
    def getFichas(self):
        return self.fichas
    


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
    Nombre: setApuesta
    Descripción: Establece la apuesta del jugador
    """
    def setApuesta(self, apuesta):
        self.apuestaActual = apuesta
    
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
        """Apuesta una cantidad de fichas, valida si tiene suficientes."""
        if cantidad > self.fichas:
            raise ValueError("No tienes suficientes fichas para apostar esa cantidad.")
        else:
            self.fichas -= cantidad
            self.apuestaActual = cantidad
    

    """
    Nombre: doblar
    Entradas: ninguna
    """
    def doblar(self):
        if self.apuestaActual*2>self.fichas:
            raise ValueError("No tienes suficientes fichas para doblar la apuesta.")
        self.fichas-=self.apuestaActual
        self.apuestaActual*=2
    

    def apostarTodo(self):
        self.apuestaActual=self.fichas
        self.fichas=0
    """
    Nombre: decisionIA
    Entradas: mazo
    Salidas: string
    Descripción: Toma una decisión de pedir otra carta o plantarse.
    """
    def decisionIA(self, mazo):
        pass
