# Write a function named substring_between_letters that takes 
# a string named word, a single character named start, and 
# another character named end. This function should return 
# the substring between the first occurrence of start and 
# end in word. If start or end are not in word, the function 
# should return word.

def substring_between_letters(word, start, end):
  start_index = word.find(start)
  end_index = word.find(end)
  if start_index > -1 and end_index > -1:
    return word[start_index+1:end_index]
  else:
    return word 

print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"