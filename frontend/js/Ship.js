/**
  * class Ship
  * coding=UTF-8
  */

class Ship {
  constructor(lenght, horizontal) {
    this.m_lenght = lenght;
    this.m_lifes = lenght;
    this.m_horizontal = horizontal;
    this.m_hurt = [];
    this.x = 0;
    this.y = 0;
  }

  /**
   * @param x value of x
   */
  setX(x)
  {
    this.x=x;
  }

  /**
   * @param y
   */
  setY(y)
  {
    this.y = y;
  }


  /**
   * @return : true if ship is horizontal.
   */
  isHorizontal ()
  {
    return this.horizontal;
  }

  /**
   * @return : true is ship is dead.
   */
  isDead()
  {
    return this.m_.lifes < 0;
  }

  /**
   *     get's called from Battelship object
   *     @param int hitAt : the relative hit position of the ship
   *     @return  : False if ship is aready hitten at this position
   *     @author Christian
   *     @param hitAt
   */
  hit(hitAt) {
    //assert hitAt < this.m_.lenght,'unable to hit ship there max lenght '+str(this.m_.lenght)
    if (hitAt in this.hurt) {
      return false;
    } else {
      this.m_lifes--;
      return true;
    }
  }
}
