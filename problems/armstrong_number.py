def checkArmstrong(n):
  num = n
  result = 0
  while num > 0:
    ld = num % 10
    result = ld**3 + result
    num = num // 10
  if (result == n):
    return True
  else:
    return False
  
print(checkArmstrong(153))