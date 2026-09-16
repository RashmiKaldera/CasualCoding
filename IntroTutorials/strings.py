# Difference between "" and ''
course = "Rashmi's course for refreshing" # Start with the double quotes to have a single quote as apostrophe
print(course)

# Triple quotes to span multiple lines

email = '''
Hi Rashmi,
This is our first email to you.

Thank you.

'''

print(email)

#%%
# Getting the character at a given index

course = "Rashmi's course for refreshing"
print(course[0])
print(course[-1]) # last character
print(course[-2]) # second to last
print(course[0:3]) # starting from 0 until the 3rd character. Doesn't return the 3rd character
print(course[0:]) # not supplying the end will print until the end
print(course[1:]) # excludes 0th index
print(course[:3]) # will assume 0 at the start

another = course[:] # copies the characters of course
print(another)

#%%
# Formatted strings
first = 'Rashmi'
last = 'Dissasekara'
message = f'{first} [{last}] is a PhD student' # {} are placeholders for variables that are going to be dynamically updated. Better visualization than string concatenation
print(message)

#%% String methods
course = "Rashmi's course for refreshing"
print(len(course)) # len is a general purpose function
# String specific functions can be accessed by . operator
print(course.upper()) # function specific to string object - method
print(course.lower())
print(course.find('for')) # returns the index of the first occurrence of that character/sequence of characters
print(course.replace('Rashmi', 'Dissasekara'))
print('Rashmi' in course)  # in operator produces a boolean value

