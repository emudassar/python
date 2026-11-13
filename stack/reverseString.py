class stack:
  def __init__(self):
    self.stack = []
    self.values = ""

  def reverseString(self, x):
    for i in range(len(x)):
      self.stack.append(x[i])

    for i in range(len(x)):
      result = self.stack.pop()
      self.values += result

    return self.values

ans = stack()
reverse = ans.reverseString("crane")
print(reverse)
