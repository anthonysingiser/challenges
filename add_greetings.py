# Create a function named add_greetings() which takes a list 
# of strings named names as a parameter.

# In the function, create an empty list that will contain 
# each greeting. Add the string 'Hello, ' in front of each 
# name in names and append the greeting to the list.

def add_greetings(names):
  lst_appended_greetings = []
  for name in names:
    lst_appended_greetings.append("Hello, " + name)
  return lst_appended_greetings

print(add_greetings(["Owen", "Max", "Sophie"]))