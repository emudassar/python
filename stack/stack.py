class Stack:
  def __init__(self):
    self.stack = []

  def push(self, value):
    self.stack.append(value)

  def pop(self):
    if len(self.stack) == 0:
      return "Stack is empty"
    else:
      return self.stack.pop()
    
  def peek(self):
    if len(self.stack) == 0:
      return "Stack is empty"
    else:
      return self.stack[-1]
    
  def display(self):
    print(self.stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

print("Pop: ", s.pop())

s.display()
