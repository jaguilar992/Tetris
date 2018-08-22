import os
import time
from max

from pieza import Pieza

COLS = 8
FILS = 16

class Tablero:
  def __init__(self):
    self.cols = COLS
    self.fils = FILS
    self.tablero = []
    self.copia_tablero = []
    self.pieza = Pieza((4,5))

  def iniciar_tablero(self):
    self.tablero = []
    for i in range(self.fils):
      self.tablero.append([0 for j in range(self.cols)])

  def nueva_pieza(self):
    self.pieza.random()

  def bajar_pieza(self):
    posicion_vertical = self.pieza.get_y()
    if(posicion_vertical + 1 < self.fils):
      celda_baja = self.pieza.get_forma()[0][0]
      if (self.tablero[celda_baja + posicion_vertical + 1]!=1):
        self.pieza.bajar()
        return True
      else:
        return False
    else:
      return False




##################################### Funciones de impresion
  def colocar_pieza(self):
    for celda in self.pieza.get_forma():
      try:
        self.copia_tablero[self.pieza.get_y()+celda[1]][self.pieza.get_x()+celda[0]] = 1
      except Exception:
        pass

  def tablero_temporal(self):
    self.copia_tablero = []
    for i in range(self.fils):
      self.copia_tablero.append(self.tablero[i][:])
    return self.copia_tablero

  def imprimir_tablero(self):
    self.tablero_temporal()
    self.colocar_pieza()
    
    for i in range(0, self.fils):
      for j in range(self.cols):
        if self.copia_tablero[i][j] == 0:
          print "_",
        else:
          print "*",
      print


if __name__=='__main__':
  duo = Tablero()
  duo.iniciar_tablero()
  duo.nueva_pieza()

  while True:
    os.system("cls")
    duo.imprimir_tablero()
    duo.bajar_pieza()
    time.sleep(1)

  print duo.tablero
