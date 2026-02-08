def greet():
    print("Hello, I am learning Python functions!")

greet()

def greet(name):
  print("Hello", name)

greet("Mudasaar")

def add(a, b):
  return a + b

result = add(5, 3)
print(result)

def describe_pet(pet_name, animal_type="dog"):
    print("I have a", animal_type, "named", pet_name)

describe_pet("Buddy")
describe_pet("Whiskers", "cat")