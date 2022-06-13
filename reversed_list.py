# Create a function named reversed_list() that takes 
# two lists of the same size as parameters named lst1 and lst2.

# The function should return True if lst1 is the same as lst2 reversed. 
# The function should return False otherwise.

def reversed_list(lst1, lst2):
  count = 0
  reverse_index = -1
  for index in range(len(lst1)):
    if lst1[index] == lst2[reverse_index]:
      count += 1
      reverse_index -= 1
    else:
      continue
  if count == len(lst1):
    return True
  else:
    return False

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))