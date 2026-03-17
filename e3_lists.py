'''
IndexOf: you should be able to determine the location of an item in a list
Example:
data = [1,2,3,5,6]
calling the function like
index_of(data, 3) should return the index 2
'''
def index_of(data, item):
    return data.index(item)

'''
Sum: you should be able to sum the items of a list
Example: data = [1,2,3]   =>  6
'''
def sum_list(data):
    return sum(data)

'''
Filter: Should filter out all instances of a value from a list
Example: filtering 2 out of [1,2,3,5,6,2,4,2] should return [1,3,5,6,4]
'''
def filter_out(data, item):
    return [x for x in data if x != item]

# Append: you should be able to add an item to the end of a list
def append(data, item):
    return data + [item]

'''
Truncate: you should be able to remove the last item of a list
hint: Use pop or slice to remove the last element of the list
'''
def truncate(data):
    return data[:-1]

'''
Concat: you should be able to join together two lists
'''
def concat(data1, data2):
    return data1 + data2

'''
Insert: you should be able to add an item at the specified index of a list
hint: Use the insert() method
'''
def insert(data, item, index):
    result = data.copy()
