
class BattleField {
  constructor (width, height)
  {
    this.m_height = height;
    this.m_width = width;

    this.m_field = new Array(this.m_height);
    for (var i = 0; i < this.m_height; i++) {
      this.m_field[i] = new Array(this.m_width);
      for (var j = 0; j < this.m_height.length; j++) {
        this.m_field[i][j].value = Field.NO_HIT;
      }
    }
    this.m_ships = [];
  }


  /**
  * @param s : Ship object
  */
  setShip(s)
  {
    this.m_ships.push(s);
    this.m_field[s.y][s.x].ship = s;
  }

  /**
  * this is the method to show te BattleField object at the website
  */
  show(parentId) {
    var gamefield = document.getElementById(parentId);
    var parent = gamefield;
    for (var i = 0; i < this.m_height; i++) {
      for (var j = 0; j < this.m_width; j++) {
        //this.m_filed[i][j]
        var showShip = document.createElement('button');
        showShip.innerHTML = "<|>";
        showShip.y = i;
        showShip.x = j;
        showShip.addEventListener('click', function (event) {
          // TODO shoot(this.x, this.y);
          // and then wait for the move of the openent
          this.innerHTML = '>|<';
        });
        this.m_filed[i][j].btn = showShip;
        parent.appendChild(showShip);
      }
      var newLine = document.createElement('br');
      gamefield.appendChild(newLine);

    }
  }

  /**
  * remove all buttons.
  */
  clearField() {
    var gamefield = document.getElementById('gamefield');
    while (gamefield.firstChild) {
      gamefield.removeChild(gamefield.firstChild);
    }
  }
}
