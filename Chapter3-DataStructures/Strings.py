'''
Strings are collection of characters
'''

'''How to define strings
    variable_name = 'Pseudocoder Ravina'
'''
name = 'Pseudocoder Ravina Python Programming Course'
print('String ->',name)
print('' * 10) # used for spacing in terminal


# Length of a string
print('Length of string ->', len(name))

print('' * 10) # used for spacing in terminal


# Access characters in a string
name = 'Pseudocoder Ravina Python Programming Course'
print("First char in the string", name[0])
print("Last char in the string", name[-1])

print('' * 10) # used for spacing in terminal

''' String Slicing
    string_name[start : end] (end is exclusive)
'''
name = 'Pseudocoder Ravina Python Programming Course'

# Specify both start and end indices
print('Slicing using start 0 and end 12 ->', name[0:12])

#Only end index
print('Slicing using only end 12 ->', name[:12])

# Only start index
print('Slicing using only start 0 ->', name[12:])

print('' * 10) # used for spacing in terminal


# Reverse a string in place
print('Reversed string ->', name[::-1])

print('' * 10) # used for spacing in terminal


# Concatenate two strings
str1 = 'Hello '
str2 = '2024'
print('String concatenation ->', str1 + str2)


str1 = 'Hello '
year = 2024
print('String concatenation with int ->', str1 + str(year))

print('' * 10) # used for spacing in terminal


#String methods

# 1. lower()
name = 'Pseudocoder Ravina Python Programming Course'
print('Lowercase string ->', name.lower())

print('' * 10) # used for spacing in terminal


# 2. upper()
name = 'Pseudocoder Ravina Python Programming Course'
print('Uppercase string ->', name.upper())

print('' * 10) # used for spacing in terminal


# 3. strip(), lstrip(), rstrip()
name = ' Ravina '

print('Strip -> [' + name.strip() + ']')
print('Strip left -> [' + name.lstrip() + ']')
print('Strip right -> [' + name.rstrip() + ']')

print('' * 10) # used for spacing in terminal


# 4. isalpha()
name='Ravina'
print('Is alphabet ->',name.isalpha())

print('' * 10) # used for spacing in terminal


# 5. isdigit()
year = '2024'
print('Is digit -> ',year.isdigit())

print('' * 10) # used for spacing in terminal


# 6. isspace()
name = '  '
print('Is space ->',name.isspace())

print('' * 10) # used for spacing in terminal


# 7. format()
# Output we want -> Hello 2024. Bye 2023
oldyear = 2023
newyear = 2024
output = 'Hello {0}. Bye {1}'
print(output.format(oldyear, newyear))

print('' * 10) # used for spacing in terminal


# 8. find()
name = 'Pseudocoder Ravina Python Programming Course'
print('Ravina starts from index -> ',name.find('Ravina'))

print('' * 10) # used for spacing in terminal


# 9. replace()
message = 'This one is the one with two or one sentence'
print('Replacing one 2 times', message.replace('one', 'ten', 2))

print('' * 10) # used for spacing in terminal


# 10. startswith()
name = 'Pseudocoder Ravina'
print('String starts with Pseudo? ->',name.startswith('Pseudo'))

print('' * 10) # used for spacing in terminal