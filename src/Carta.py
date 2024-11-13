"""
Clase Carta
Representa una carta, para Blackjack.
"""    
class Carta:
    
    """
    Constructor de la clase Carta.
    """
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor
        self.valorNumerico = self.calcularValorNumerico()
        self.visible=False

    """
    Nombre: getPalo
    Descripción: Obtiene el palo de la carta
    """
    def getPalo(self):
        return self.palo
    
    """
    Nombre: getValor
    Descripción: Obtiene el valor de la carta
    """
    def getValor(self): 
        return self.valor
    
    """
    Nombre: getValorNumerico
    Descripción: Obtiene el valor numérico de la carta
    """
    def getValorNumerico(self):
        return self.valorNumerico
    
    """
    Nombre: setValor
    Descripción: Establece el valor de la carta
    """
    def setValor(self, valor):
        self.valor = valor


    """
    Nombre: setPalo
    Descripción: Establece el palo de la carta
    """
    def setPalo(self, palo):
        self.palo = palo

    """
    Nombre: setValorNumerico
    Descripción: Establece el valor numérico de la carta
    """
    def setValorNumerico(self, valorNumerico):
        self.valorNumerico = valorNumerico

    """
    Nombre: calcularValorNumerico
    Descripción: Calcula el valor numérico de la carta
    """
    def calcularValorNumerico(self):
        if self.valor in ['J', 'Q', 'K']:
            self.valorNumerico = 10
        elif self.valor == 'A':
            self.valorNumerico = 11
        else:
            self.valorNumerico = int(self.valor)

    """
    Nombre: mostrar
    Descripción: Muestra la carta
    """
    def mostrar(self):
        self.visible=True

    """
    Nombre: ocultar
    Descripción: Oculta la carta
    """
    def ocultar(self):
        self.visible=False

    