number = int(input("Write number: "))
sum_even_number = 0

for i in range(1, number+1):
  if i%2 == 0:
    sum_even_number += i

print(sum_even_number)
