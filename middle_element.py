# Create a function called middle_element that has one parameter 
# named lst.

# If there are an odd number of elements in lst, 
# the function should return the middle element. 
# If there are an even number of elements, the 
# function should return the average of the middle two elements.

def middle_element(lst):
  if len(lst) % 2 == 0:
    half = int(len(lst) / 2)
    average = lst[half-1] + lst[half]
    average = average / 2
    return average
  else:
    half = int(len(lst) / 2)
    return lst[half]

print(middle_element([5, 2, -10, -4, 4, 5]))