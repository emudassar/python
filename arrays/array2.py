from array import *

val = array("i", [1, 2, 3, 4, 5])

# print(val)
# for i in range(0, len(val)):
#   print(val[i], end=" ")

for x in val:
  print(x, end=" ")

# print(val.typecode)

# val.reverse()
# print(val)

print("\n")

# val.insert(1, 10)
# print(val)

# val[1] = 8
# print(val)

# newArray = array(val.typecode, (x for x in val))
# print(newArray)

# val.pop(2)
# print(val)

# val.remove(3)
# print(val)

# newArray = val[::-1]
# print(newArray)

arr = array("i", [])

num = int(input("Enter a number: "))

for x in range(0, num):
  arr.append(int(input("Enter next number: ")))

for x in arr:
  print(x, end=" ")

# i = val.index(3)
# print(i)

