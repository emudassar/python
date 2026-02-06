userAge = int(input("Write your age: "))

if userAge < 13:
  print("Child")
elif userAge < 20:
  print("Teenager")
elif userAge < 59:
  print("Adult")
else:
  print("Senior")
  
