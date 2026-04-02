class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.data = value

def insert(root, value):
  if (root == None):
    return Node(value)
  if (root.data == value):
    return root
  if (root.data > value):
    root.left = insert(root.left, value)
  else:
    root.right = insert(root.right, value)
  return root

def search(root, value):
  if (root == None):
    print("Element not found", end="\n")
    return
  if (root.data == value):
    print("Element found", end="\n")
    return
  if (root.data > value):
    search(root.left, value)
  else:
    search(root.right, value)
  
def inOrder(root):
  if (root != None):
    inOrder(root.left)
    print(root.data, end = " ")
    inOrder(root.right)

root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 25)
root = insert(root, 50)
inOrder(root)
search(root, 25)
search(root, 100)

# root = Node(20)
# root.left = Node(15)
# root.right = Node(30)
# root.left.left = Node(12)
# root.left.right = Node(18)
# root.right.right = Node(40)
# inOrder(root)