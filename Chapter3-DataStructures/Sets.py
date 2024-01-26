'''
Collection of values. Used to store multiple unique values. 
Sets are Unordered
'''

# Define a Set
letters = {'a', 'b', 'c', 'a'}
numbers = set([1,2,3])

# Access items
print('Access items')
letters = {'a', 'b', 'c'}

print('Using in operator. Is a in letters -> ', 'a' in letters)
print('Using in operator. Is z in letters -> ', 'z' in letters)
print() # print for new line

# Add to Set
numbers = {1,2,3}
decimals = {1.5, 2.5, 3.5}

numbers.add(4)
numbers.add(5)
print('Set after adding items ->', numbers)

numbers.update(decimals)
print('numbers after update method ->', numbers)
print() # print for new line

# Remove from Set
print('Remove from Set')
letters = {'a', 'b', 'c', 'd'}
letters.remove('a')
print('After remove method ->', letters)

letters.discard('z')
letters.discard('b')
print('After discard method ->', letters)

letters.clear()
print('After clear method ->', letters)

# Uncomment the statement below to delete set
# del letters
print() # print for new line

# Join Sets
print('Join Sets')
odd = {1,3,5}
even = {2,4,6}

combined = odd.union(even)
print('Combined set after union ->', combined)

odd.update(even)
print('odd after update method ->',odd)
print('even after update method ->',even)
print() # print for new line

# Keep Duplicates only
numbers1 = {1,3,5,6,7}
numbers2 = {2,4,6,7}

numbers = numbers1.intersection(numbers2)
print('numbers after intersection ->',numbers)

numbers1.intersection_update(numbers2)
print('numbers1 after intersection_update ->',numbers1)
print() # print for new line

# Keep All, but not Duplicates
numbers1 = {1,3,5,6,7}
numbers2 = {2,4,6,7}

numbers = numbers1.symmetric_difference(numbers2)
print('numbers after symmetric_difference ->',numbers)

numbers1.symmetric_difference_update(numbers2)
print('numbers1 after symmetric_difference_update ->',numbers1)
print() # print for new line
