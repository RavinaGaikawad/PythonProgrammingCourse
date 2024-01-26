'''
Collection of values. Used to store multiple values. 
Ordered and immutable/unchangeable
'''

# Define a Tuple
# variable_name = (value1, value2, value3)
letters = ('a', 'b', 'c')
numbers = (1,2,3)

# Access Tuple values
print('Access Tuple values')
letters = ('a', 'b', 'c')
uppercase = ('A', 'B')

print('First element ->', letters[0])
print('Slicing ->', letters[:2])
print('Concatenate 2 tuples ->',letters + uppercase)
print() # print for new line

print('Packing and unpacking')
weights = (5,3,8)
print('Packed ->', weights)

x, y, z = weights
print('Unpacked ->',x,y,z)
print() # print for new line



# Sort Tuple
print('Sort Tuple')
numbers = (1,6,7,8,9, 2, 3)
print('Sorted tuple', tuple(sorted(numbers)))

print('Reversed tuple', numbers[::-1])
print() # print for new line

# Delete Tuple
numbers = (1,3,4,5)

# Comment the statement below to delete the tuple.
# del numbers
