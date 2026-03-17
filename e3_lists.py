'''
index_of: should return the index of the first occurrence of the value in the list.
Should raise ValueError if the value is not found.
'''
def index_of(lst, value):
    if value not in lst:
        raise ValueError(f"{value} is not in list")
    return lst.index(value)

'''
sum_list: should return the sum of all numbers in the list.
'''
def sum_list(lst):
    return sum(lst)

'''
filter_out: should return a new list with all occurrences of the value removed.
'''
def filter_out(lst, value):
    return [x for x in lst if x != value]

'''
append: should return a new list with the value added to the end.
'''
def append(lst, value):
    return lst + [value]

'''
truncate: should return a new list with the last element removed.
'''
def truncate(lst):
    return lst[:-1]

'''
concat: should return a new list combining both lists.
'''
def concat(lst1, lst2):
    return lst1 + lst2

'''
insert: should return a new list with the value inserted at the given index.
'''
def insert(lst, value, index):
    return lst[:index] + [value] + lst[index:]

'''
square: should return a new list with each value squared.
'''
def square(lst):
    return [x ** 2 for x in lst]