# Create a function named odd_indices() that has 
# one parameter named lst.

# The function should create a new empty list 
# and add every element from lst that has an odd index. 
# The function should then return this new list.

def odd_indices(lst):
  new_lst = []
  for num in lst:
    if lst.index(num) % 2 == 0:
      continue
    else:
      new_lst.append(num)
  return new_lst

print(odd_indices([4, 3, 7, 10, 11, -2]))