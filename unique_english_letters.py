# Write a function called unique_english_letters that 
# takes the string word as a parameter. The function 
# should return the total number of unique letters 
# in the string. Uppercase and lowercase letters should 
# be counted as different letters.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  count = 0
  for letter in letters:
    if letter in word:
      count += 1
  return count

print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
