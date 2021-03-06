# Write a function named count_char_x that takes a string 
# named word and a single character named x as parameters. 
# The function should return the number of times x appears in word.

def count_char_x(word, x):
  count = 0 
  for character in word:
    if character == x:
      count += 1
  return count

print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1