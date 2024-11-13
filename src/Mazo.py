import random
from Carta import *

"""
Representa un mazo de cartas para un juego de blackjack.
"""
class Mazo:
    
    # Palos y valores de las cartas
    palos = ['Corazones', 'Diamantes', 'Tréboles', 'Picas']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    """
    Constructor de la clase Mazo.
    """
    def __init__(self):
        self.cartas = [Carta(valor, palo) for palo in self.palos for valor in self.valores]
        random.shuffle(self.cartas)
        self.conteo=0

    """
    Nombre: getCartas
    Descripción: Obtiene las cartas del mazo
    """
    def getCartas(self):
        return self.cartas
    """
    Nombre: getConteo
    Descripción: Obtiene el conteo de cartas del mazo
    """
    def getConteo(self):
        return self.conteo
    
    """
    Nombre: robarCarta
    Entradas: ninguna
    Salidas: Carta
    Descripción: Roba una carta del mazo.
    """
    def robarCarta(self):
        carta=self.cartas.pop()
        self.actualizarConteo(carta)
        return carta
    
    """
    Nombre: actualizarConteo
    Entradas: Carta
    Salidas: ninguna
    Descripción: Actualiza el conteo de cartas del mazo.
    """
    def actualizarConteo(self,carta):
        valor=carta.getValor()
        if valor in ['2','3','4','5','6']:
            self.conteo+=1
        elif valor in ['10','J','Q','K','A']:
            self.conteo-=1

