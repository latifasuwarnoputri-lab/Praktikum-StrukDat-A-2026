x = "Selamat datang"

print(len(x))

mytuple = ("strawberry", "mangga", "apel")

print(len(mytuple))

celana = {
  "brand": "uniqlo",
  "jenis": "jeans",
  "ukuran": 35
}

print(len(celana))

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #membuat objek car
boat1 = Boat("Ibiza", "Touring 20") #membuat objek boat
plane1 = Plane("Boeing", "747")     #membuat objek plane

for x in (car1, boat1, plane1):
  x.move()

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()