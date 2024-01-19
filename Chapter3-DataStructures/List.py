'''
Collection of values. Used to store multiple values.
'''

# Define a List
# variable_name = [value1, value2, value3]
print("Define List")
letters = ['a', 'b', 'c']
numbers = [1,2,3]
floats = [1.5, 4.5]
zeros = [0] * 50
print(zeros)
print() # print for new line

# Access List items
print("Access List Items")
letters = ['a', 'b', 'c']
print('First element', letters[0])
print('Last element', letters[-1])
print('Slicing 1', letters[0:2])
print('Slicing 2', letters[0:])
print('Slicing 3', letters[1:])

print('In operator -> z in letters -> ', 'z' in letters)
print() # print for new line


# Add to List
print("Add to List")
letters = ['a', 'b', 'c']
uppercase_letters = ['A', 'B']

letters.extend(uppercase_letters)
print('letters', letters)
print('uppercase_letters', uppercase_letters)
print() # print for new line


# Update List
print("Modify List Items")
letters = ['a', 'b', 'c']

letters[0] = 'x'
letters[1:3] = 'y', 'z'

print('Modified list ->', letters)
print() # print for new line


# Remove from List
print('Remove from List')
letters = ['a', 'b', 'c']
letters.remove('a')
print('a removed', letters)

letters.pop(1)
print('1st index popped', letters)

del letters[0]
print('1st index deleted', letters)

letters.clear()
print('clear all items', letters)

# del letters -> used to delete the list
print() # print for new line


# Sort List
print("Sort List")
letters = ['a','z', 'x', 'b', 'c']
numbers = [7,8,3,4,2,1]

# sort in ascending order
letters.sort()
numbers.sort()
print('sorted letters', letters)
print('sorted numbers', numbers)

#sort in descending order
numbers.sort(reverse=True)
print('sort numbers in desc order', numbers)

sorted_numbers = sorted(numbers)
print('sorted_numbers', sorted_numbers)
print() # print for new line


# Copy List
letters = ['a', 'b', 'c']
copy_letters = letters.copy()

copy_letters[0] = 'z'

print('Original list', letters)
print('Copied list and updated', copy_letters)
print() # print for new line

# Applications

# Stack
print('Stack')
stack = []

stack.append('a')
stack.append('b')
stack.append('c')
print('Initial Stack', stack)

stack.pop()
print('Stack after 1st pop', stack)
stack.pop()
print('Stack after 2nd pop', stack)
stack.pop()
print('Stack after 3rd pop', stack)

print() # print for new line


#Queue
print('Queue')
queue = []

queue.append(1)
queue.append(2)
queue.append(3)
print('Initial Queue', queue)

queue.pop(0)
print('Queue after 1st pop', queue)
queue.pop(0)
print('Queue after 2nd pop', queue)
queue.pop(0)
print('Queue after 3rd pop', queue)
