# Create a function named max_num() that takes a list 
# of numbers named nums as a parameter.

# The function should return the largest number in nums.

def max_num(nums):
  def_max = nums[0]
  for num in nums:
    if num > def_max:
      def_max = num
  return def_max

print(max_num([50, -10, 0, 75, 20]))