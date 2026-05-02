def checkPalindrome():
  n = 1234
  num = n
  result = 0

  while num > 0:
    last_digit = num % 10
    result = result * 10 + last_digit
    num = num // 10

  if (result == n):
    print("Palindrome")
  else:
    print("Not palindrome")
checkPalindrome()