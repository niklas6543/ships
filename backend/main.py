import BattleField
import Ship

b = BattleField.BattleField()
ship = Ship.Ship(lenght=5, horizontal= True)
ship.setX(0)
ship.setY(0)
b.setShip(ship)

print(b.shoot(x=0, y=0))
print(b.shoot(x=1, y=1))
print(b.shoot(x=2, y=0))
print(b.shoot(x=4, y=4))
print(b.shoot(x=5, y=4))
