# Using the {**dict1, **dict2} syntax:

# You can merge two dictionaries using the {**dict1, **dict2} syntax.

my_dict = {'key0': 'value0'}
new_items = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
my_dict = {**my_dict, **new_items}
print(my_dict)