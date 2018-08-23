import os
import time
import max7219.led as led

from pieza import Pieza

COLS = 8
FILS = 16

class Tablero:
  def __init__(self):
    self.cols = COLS
    self.fils = FILS
    self.tablero = []
    self.copia_tablero = []
    self.pieza = Pieza((4,0))
    self.display = led.matrix(cascaded=2)

  def iniciar_tablero(self):
    self.tablero = []
    for i in range(self.fils):
      self.tablero.append([0 for j in range(self.cols)])

  def nueva_pieza(self):
    self.pieza.random()

  def es_cuadro_vacio(self, x, y):
    return self.tablero[y][x] != 1

  def es_pieza_libre_bajar(self):
    forma = self.pieza.get_forma()
    results = []
    for celda in forma:
      x = celda[0] + self.pieza.get_x()
      y = celda[1] + self.pieza.get_y() + 1
      results.append(self.es_cuadro_vacio(x,y))
    return not (False in results)

  def bajar_pieza(self):
    y = self.pieza.get_y()
    if(y + 1 < self.fils):
      print self.es_pieza_libre_bajar()
      if (self.es_pieza_libre_bajar()):
        self.pieza.bajar()
        return True
      else:
        return False
    else:
      return False

  def unir_pieza_tablero(self):
    
    for celda in self.pieza.get_forma():



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

  def get_id(self, i):
    if (i<=8):
      return 0
    else:
      return 1

  def get_pos(self,i):
    if (i<=8):
      return i
    else:
      return i-8

  def get_byte(self, fil):
    return sum([self.copia_tablero[fil][i] * (2**(7-i)) for i in range(self.cols)])

  def imprimir_tablero(self):
    self.display.clear()
    self.tablero_temporal()
    self.colocar_pieza()
    for i in range(0, self.fils):
      self.display.set_byte(self.get_id(i+1), self.get_pos(i+1), self.get_byte(i))


if __name__=='__main__':
  duo = Tablero()
  duo.iniciar_tablero()
  duo.nueva_pieza()
  duo.tablero[7][4] = 1

  while True:
    duo.imprimir_tablero()
    baja = duo.bajar_pieza()
    if not baja{

    }
    time.sleep(0.5)
