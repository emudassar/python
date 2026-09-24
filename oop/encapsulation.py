class Factory:
  name = "Kia"
  __secName = "Alto"
  def __init__(self, type, tyre, color):
    self.type = type
    self.tyre = tyre
    self.__color = color

  def getName(self):
    return self.__color

obj = Factory("sedan", "MRF", "black")
print(obj.name)
obj.__color = "Blue"
print(obj.getName())