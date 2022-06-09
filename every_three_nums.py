# Create a function called every_three_nums that has 
# one parameter named start.

# The function should return a list of every third 
# number between start and 100 (inclusive). 

def every_three_nums(start):
  return list(range(start, 101, 3))

print(every_three_nums(91))