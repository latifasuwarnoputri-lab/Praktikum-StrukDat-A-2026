class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # Private property

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

p1 = Person("Michelle", 22)
print(p1.get_age())

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

p1 = Person("Bubu", 23)
print(p1.get_age())

p1.set_age(30)
print(p1.get_age())

class Person:
  def __init__(self, name, salary):
    self.name = name
    self._salary = salary  # Protected property

p1 = Person("Linus", 50000)
print(p1.name)
print(p1._salary)  # Can access, but shouldn't

class Calculator:
  def __init__(self):
    self.result = 0

  def __validate(self, num):
    if not isinstance(num, (int, float)):
      return False
    return True

  def add(self, num):
    if self.__validate(num):
      self.result += num
    else:
      print("Invalid number")

calc = Calculator()
calc.add(13)
calc.add(7)
print(calc.result)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age

p1 = Person("Emil", 30)

# This is how Python mangles the name:
print(p1._Person__age) # Not recommended!