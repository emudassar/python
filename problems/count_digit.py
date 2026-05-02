def countDigit(n):
  num = n
  count = 0
  while num > 0:
    count = count + 1
    num = num//10
  return count

print(countDigit(6755578))