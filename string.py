# Strings can be concatenated (glued together) with the + operator, 
# and repeated with * operator
myFirstVar = "My name is Suo Tan"
mySecondVar = "I just graduated from Concordia University"
print(3 * myFirstVar + ", " + mySecondVar)
print("----------------------")

# string place holder %s, %d, %f, etc. 
animal = "cat"
print("%s can miao~" % animal)
print("----------------------")

# use raw strings by adding an 'r' before the first quote
print('C:\some\name')
print(r'C:\some\name')
print("----------------------")

# using triple-quotes: """...""" or '''...''' for multiple lines
print ("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print("----------------------")

# index in strings
word = "Python"
print(word[0])
print(word[-1])     # last character
print(word[-2])     # second-last character
print(word[2:5])    # characters from position 2 (included) to 5 (excluded)
print(word[-2:])    # characters from the second-last (included) to the end
print(len(word))    # the length of a string


# Single Quote v.s. Double Quote
## double quotes around strings that are used for interpolation or that are natural language messages
## single quotes for small symbol-like strings, but will break the rules if the strings contain quotes
## triple double quotes for docstrings and raw string literals for regular expressions

# LIGHT_MESSAGES = {
#     'English': "There are %(number_of_lights)s lights.",
#     'Pirate':  "Arr! Thar be %(number_of_lights)s lights."
# }

# def lights_message(language, number_of_lights):
#     """Return a language-appropriate string reporting the light count."""
#     return LIGHT_MESSAGES[language] % locals()

# def is_pirate(message):
#     """Return True if the given message sounds piratical."""
#     return re.search(r"(?i)(arr|avast|yohoho)!", message)