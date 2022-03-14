class jugador():
    def __init__(self):
        print('jugador iniciado')
    def seleccionaTiro(self, tablero):
        print(tablero)
class tablero():
    posiciones=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    def getTablero(self):
        return self.posiciones
    def elige(self, posicion, jugador):
        for item, value in enumerate(self.posiciones):
            if value==posicion:
                self.posiciones[item]=jugador
    def show(self):
        print(self.posiciones)
pcGamer=jugador()
mytablero=tablero()
mytablero.elige(3, 'A')
mytablero.show()
tablero=mytablero.getTablero()
pcGamer.seleccionaTiro(tablero)
