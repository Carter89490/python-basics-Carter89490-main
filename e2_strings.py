'''
reverse_string: you should be able to reverse a string
  Example: "abc" => "cba"
'''
def reverse_string(str):
    return str[::-1]

'''
capitalize: should return the input in all-caps
  Example: "this is a string" => "THIS IS A STRING"
'''
def capitalize(str):
    return str.upper()

'''
split_string: should divide a string into substrings and return a list
  Example: "Jane,Doe,21"  =>  [ "Jane", "Doe", "21" ]
'''
def split_string(str, splitAt=','):
    return str.split(splitAt)