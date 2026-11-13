class queue:
  def __init__(self):
    self.values = []

  def enqueue(self, x):
    self.values.append(x)

  def dequeue(self):
    front = self.values[0]
    self.values = self.values[1:]
    return front

q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q.values)
q.dequeue()
print(q.values)