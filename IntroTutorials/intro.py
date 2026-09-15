print('Rashmi Dissasekara')
print('o----')
print(' ||||')
print('*' * 10) # Python expression
#%%
# Using Variables to store data
price = 10 # Numbers without a decimal point - integers
rating = 4.0 # Floats with decimal points
name = 'Rashmi' # Strings with alphabetical characters
is_published = True # use _ to separate words in python. Stores a boolean value here. True or False
print (price, rating, name, is_published)

#%%
# Exercise - create variables to store patient information such as name, age and whether they are a new patient

full_name = 'John Smith'
age = 20
is_new = True
#%%
# Receiving input from the user
name = input('What is your name? ')
print('Hi ' + name) # String concatenation - python expression

#%%
#Exercise
name = input('What is your name? ')
color = input('What is your favorite color? ')
print(name + ' likes ' + color)

#%%
# Type conversion
birth_year = input('What is your birth year? ')
age = 2026 - int(birth_year) # convert to integer. otherwise string is the default data type
print ('You are now ' + str(age) + ' years old') # int must be converted to str for concatenation

# Finding out the data type
print(type(birth_year))
print(type(age))

#%%
#Exercise - ask a user their weight in pounds and convert to kg

weight_lb = input("What is your weight in pounds? ")
weight_kg = float(weight_lb) * 0.45
print("Your weight is " + str(weight_kg) + " kgs")