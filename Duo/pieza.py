from def_piezas import PIEZAS
import random as rnd

class Pieza:
  # pos es un tupla (x,y) indica la posicion de la pieza en el tablero
  def __init__(self, pos):
    self._n = rnd.randint(0, 2)
    self._rotacion = rnd.randint(0, 3)
    self._pos = pos
    self._x = pos[0]
    self._y = pos[1]

  def bajar(self):
    self._y+=1

  def derecha(self):
    self._x +=1

  def izquierda(self):
    self._x -=1

  def subir(self):
    self._y-=1

  def get_x(self):
    return self._x
  
  def get_y(self):
    return self._y

  def get_forma(self):
    return PIEZAS[self._n][self._rotacion]

  def random(self):
    self._n = rnd.randint(0, 3)
    self._rotacion = rnd.randint(0, 3)
