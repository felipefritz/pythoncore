# Immutable data types:
# Are those that can never change their value in place.

# Integers
# Floating-Point numbers
# Booleans
# Strings
# Tuples

# Mutable:
# Mutable data types are those whose values can be changed in place

# Lists
# Dictionaries
# Sets

# Example. The id object in memory will change:
# Strings:

string = "Hello world"
print(id(string))
string = "Hello world2"
print(id(string))
# but it is possible to change by slices
string = string[:2] + 'str' + string[2 + 1:]
print(string)
print(id(string))


l = [2, 1, 3]

print(sorted(l))


