# Create a function named exponents() 
# that takes two lists as parameters named bases and powers. 
# Return a new list containing every number in bases raised 
# to every number in powers.

def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for exponent in powers:
      new_lst.append(base ** exponent)
  return new_lst

print(exponents([2, 3, 4], [1, 2, 3]))