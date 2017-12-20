## Functions

# function with required arguments
def status(user, mood="happy"):
    """ Print a user's mood

    Args:
        user: [str] a user's name
        mood: [str] the mood
    Returns: 
        [str] the user's mood
    """
    return ("{} is {} now.".format(user, mood))


default_me = status("Suo Tan")
print(default_me)

sad_me = status("Suo Tan", "sad")
print(sad_me)

# print(status()) # This will raise error. At lest pass a value for 'user'. 

# help(status) # help function to tell you how to use the function.


# function with keyword arguments
def convert_imperial_to_metric(feet=0.0, inches=0.0):
    """ Convert U.S./Imperial units to SI/Metric units

    Args:
        feet: [float] value in feet (default 0.0)
        inches: [float] value in inch (default 0.0)
    Return:
        [float] the converted value in centimeters
    """
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm

length_2_cm = convert_imperial_to_metric(inches=3, feet=2.6) # keyword arguments, spelt out when calling
print (length_2_cm)


## SUMMARY
# 1. There are three types of arguments for a function in Python: required arguments, keyword arguments and variable-length arguments.
# 2. Required arguments do not have default values. Required arguments must be passed a value following the correct positional order, and the parameter number must match exactly, when the function is called.
# 3. Keyword arguments must be spelt out when calling the function. You do not need to pass a value for an argument with default value provided in function definition. Keyword arguments help you write flexable functions and clean code. 
# 4. All arguments in the Python are passed by reference.