# Write a function named append_sum that has one parameter 
# — a list named named lst.

# The function should add the last two elements 
# of lst together and append the result to lst. 
# It should do this process three times and then return lst.


def append_sum(lst):
  i = 0
  while i < 3:
    lst.append(lst[-1] + lst[-2])
    i += 1
  return lst

print(append_sum([1, 1, 2]))