# class Animal:
#   def __init__(self, name):
#     self.name = name

#   def details(self):
#     print(f"Hello, your name is {self.name}")

# class Human(Animal):
#   pass

# obj1 = Animal("Lion")
# obj2 = Human("Mudassar")

# obj1.details()
# obj2.details()

# print(obj1.name)
# print(obj2.name)

# class BagFactory:
#   def __init__(self, material, zips, pockets):
#     self.material = material
#     self.zips = zips
#     self.pockets = pockets

#   def details(self):
#     print("Here are your bag details: ")
#     print(self.material)
#     print(self.zips)
#     print(self.pockets)

# class Rebook(BagFactory):
#   def __init__(self, material, zips, pockets, color):
#     super().__init__(material, zips, pockets)
#     self.color = color

#   def details(self):
#     print(self.color)
#     return super().details()


# bag1 = BagFactory("Leather", 3, 2)
# bag2 = Rebook("Leather", 3, 2, "Blue")

# bag1.details()
# bag2.details()

# print(bag1.material)
# print(bag2.color)


# Multple Inheritance


# class Animal:
#   def __init__(self, name):
#     self.name = name

# class Human:
#   def __init__(self, id):
#     self.id = id

# class Robot(Human, Animal):
#   def __init__(self, id, name):
#     Human.__init__(self, id)
#     Animal.__init__(self, name)

#   def details(self):
#     print(self.id)
#     print(self.name)

# robo = Robot(1, "Emkay")
# robo.details()



# single inheritance

# class A:
#   def __init__(self, name):
#     self.name = name
    
# class B(A):
#   def __init__(self, name):
#     super().__init__(name)
    
# obj = B("Mudassar")
# print(obj.name)

# # multiple inheritance

# class A:
#   def __init__(self, name):
#     self.name = name
    
# class B:
#   def __init__(self, id):
#     self.id = id
    
# class C(A, B):
#   def __init__(self, name, id):
#     A.__init__(self, name)
#     B.__init__(self, id)
  
  
# obj = C("Mudassar", 2)

# print(obj.name)
# print(obj.id)


class Animal:
  def speak(self):
    print("Dog can speak")

class Dog(Animal):
  def speak(self):
    return super().speak()

obj = Dog()
obj.speak()