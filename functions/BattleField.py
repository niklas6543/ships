# coding=UTF-8
from .Ship import *

# https://docs.python.org/3/library/enum.html
from enum import Enum

class Field(Enum):
    """
    1 if not hited and empty
    2 if hited and empty
    3 if filled and not hited
    4 if filled and hited
    """
    EMPTY_NO_HIT = 1
    EMPTY_HIT = 2
    FILLED_NO_HIT = 3
    FILLED_HIT = 4

# https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
class FieldNotFoundException(Exception):
    """docstring for EieldNotFoundException."""
    def __init__(self):
        super(FieldNotFoundException, self).__init__()

class BattleField(object):

  """
  :version: 1.0
  """

  """ ATTRIBUTES



  width  (private)



  height  (private)
  height of the field


  ships  (private)



  field  (private)
  1 if not hited and empty
  2 if hited and empty
  3 if filled and not hited
  4 if filled and hited

  """
  def __init__(self, width = 10, height = 10):
    """
    @param int width : for the field.
    @param int height : for the field.
    @return  : a instance of BattleField.
    @author Christian Boseck
    """
    self.width = width
    self.height = height
    # https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array-in-python
    self.field = [[0 for x in range(self.width)] for y in range(self.height)]
    self.clearField()
    self.ships = []


  def shoot(self, x, y):
    """
    @param int x : the position to shoot at
    @param int y : the position to shoot at
    @return bool : True if you hit a ship, else retuns False
    @author Christian
    """
    if x > self.width or x < 0:
        raise FieldNotFoundException()
    elif y > self.height or y < 0:
        raise FieldNotFoundException()

    for ship in self.ships:
        if ship.isHorizontal:
            if ( x <= (ship.x + ship.lenght)) and (x >= ship.x) and ship.y is y:
                ship.hit(x - ship.x)
                self.field[x][y] = Field.FILLED_HIT
                return True
            else:
                self.field[x][y] = Field.EMPTY_HIT
                return False
        else:
            if (y <= ship.y + ship.lenght ) and (ship.y >= y) and ship.x is x:
                ship.hitAt(y - ship.y)
                self.field[x][y] = Field.FILLED_HIT
                return True
            else:
                self.field[x][y] = Field.EMPTY_HIT
                return False

    # if no ships are set
    return False

  def clearField(self):
    """
    makes all Fields empty with no hits

    @author Christian
    """
    for x in self.field:
        for fieled in x:
            fieled = Field.EMPTY_NO_HIT

  def setShip(self, s):
    """
     the ships starts at x, y, and goes x + ship.lenght or y + ship.lenght if
     horizontal is false.

    @param Ship s :

    @return  :
    @author
    """
    self.ships.append(s)
    pass
