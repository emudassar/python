# a = int(input("value 1: "))
# b = int(input("value 2: "))
# c = int(input("value 3: "))

# result = (a*b)*c
# print(result)

# a = int(input("value 1: "))
# b = int(input("value 2: "))

# result = (a + b) / 2
# print(result)


# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

def runningSumArray():
  nums = [1,2,3,4]
  for i in range(1, len(nums)):
    nums[i] += nums[i-1]
  print(nums)
  return nums

runningSumArray()

