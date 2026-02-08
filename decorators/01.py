
def my_decorator(func):
  def wrapper():
    print("Before")
    func()
    print("After")
  return wrapper

def say_hello():
  print("Hello!")

decorated_function = my_decorator(say_hello)
decorated_function()
