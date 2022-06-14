# Write a function named count_multi_char_x that takes a 
# string named word and a string named x.  
# Make sure your function works when x is 
# multiple characters long.

def count_multi_char_x(word, x):
  splits = word.split(x)
  return (len(splits)-1)

print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1