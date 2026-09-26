# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

# Example 1:

# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.

def maximumWealth():

  accounts = [[1,2,3],[3,2,5]]
  acc1 = accounts[0]
  acc2 = accounts[1]
  count1 = 0
  count2 = 0

  for i in acc1:
     count1 += i
  for j in acc2:
     count2 += j
  if count1 > count2:
     print(count1)
  else:
     print(count2)

maximumWealth()