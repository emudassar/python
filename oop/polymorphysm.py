# class Animal:
#     def speak(self):
#         print("Animal cannot speak")


# class Human:
#     def speak(self):
#         print("Human can speak")

# obj1 = Animal()
# obj2 = Human()

# obj1.speak() 
# obj2.speak()


# Method Overriding

class Animal:
   def __init__(self, name):
      self.name = name
      
   def details(self):
      print(f"This is your {self.name}")
      
class Human(Animal):
   def __init__(self, name):
      super().__init__(name)
      
   def details(self):
      print(f"Your info is {self.name}, and this is all we have")
      
obj = Human("Mudassar")
obj.details()

