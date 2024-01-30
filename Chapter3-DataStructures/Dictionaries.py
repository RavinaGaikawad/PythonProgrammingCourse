'''
Collection of values. Used to store key value pairs.
'''

#Define 
data = {}
data = dict()
data = {'name': 'Pseudocoder',
        'course': 'Python'}

# Access items in a dict
print('Access items in a dict')
data = {'name': 'Pseudocoder',
        'course': 'Python'}

print('Access using key name inside square brackets ->', data['name'])
print('Access using get method ->', data.get('name', 0))

print('Access all keys in the dict ->', data.keys())
print('Access all values in the dict ->', data.values())
print('Access all items in the dict ->', data.items())
print() # print for new line


# Add & Update dict values
print('Add & Update dict values')
data = {'name': 'Pseudocoder',
        'course': 'Python'}

data['name'] = 'Ravina'
data['age'] = 21
print('Upsert using square brackets ->', data)

data.update({'age': 25, 'title': 'SDE'})
print('Upsert using update method ->', data)
print() # print for new line


# Remove items from dict
print('Remove items from dict')
data = {'name': 'Pseudocoder',
        'course': 'Python',
        'age': 21,
        'title': 'SDE'}

data.pop('age')
print('Remove using pop method ->', data)

del data['title']
print('Remove using del keyword ->', data)

data.popitem()
print('Remove using popitem method ->', data)

data.clear()
print('Remove all items using clear method ->', data)

# Uncomment line below to delete the dictionary
# del data 

print() # print for new line


# Copy dict
print('Copy dict')
data = {'name': 'Pseudocoder',
        'course': 'Python'}

data2 = data.copy()

data2['name'] = 'Ravina'

print('Old dict after Copy method ->',data)
print('New dict after Copy method ->',data2)

print() # print for new line


# Nested Dict
print('Nested Dict')
data1 = {'name': 'Pseudocoder',
        'course': 'Python'}

data2 = {'name': 'Pseudocoder',
        'course': 'DBMS'}

records = {}

records['data1'] = data1
records['data2'] = data2

print('Nested dict ->',records)
