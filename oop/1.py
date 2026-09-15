class Bags:
  def __init__(self,name,zip,pockets):
    self.name = name
    self.zip = zip
    self.pockets = pockets

rebook = Bags("Leather", 3, 2)
campus = Bags("polyster", 2, 4)

print(rebook.name)
print(campus.name)