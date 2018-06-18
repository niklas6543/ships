# coding=UTF-8

class Ship(object):

  """

  :version: 1.0
  :author: Christian
  """

  """ ATTRIBUTES



  lenght  (private)



  lives  (private)


  horizontal (private)

  """

  def __init__(self, lenght, horizontal):
      self.lenght = lenght
      self.lifes = self.lenght
      self.horizontal = horizontal
      self.hurt = []

  def setX(self, x):
      self.x = x

  def setY(self, y):
      self.y = y

  def hit(self, hitAt):
    assert hitAt < self.lenght, 'unable to hit ship there max lenght ' + str(self.lenght)
    """
    get's called from Battelship object

    @param int hitAt : the relative hit position of the ship
    @return  : False if ship is aready hitten at this position
    @author Christian
    """

    if hitAt in self.hurt:
        return False
    else:
        self.lifes -= 1
        return False

  def isHorizontal(self):
      """
      @return : true if ship is horizontal
      """
      return self.horizontal

  def isDead(self):
      return self.lifes < 0
