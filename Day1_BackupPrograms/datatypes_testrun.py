"""

Program to testrun different datatypes.

i = 1 # Integer. Stores integers
r = 5.78 # Floats. Stores numbers with decimal parts.
c = 'h' # Characters. Stores single characters. It is a string in python.
s = 'Strings' # Strings. Stores a series of characters
l = True/False # Logical. Stores binary values
cm = 6.0+5.6j  # Complex. Stores complex values

* ``id()`` : returns the memory location ID of the variable.
* ``type()`` - returns the datatype of the variable.
* ``ord()`` - returns the ASCII/Unicode value of the symbol.
* ``chr()`` - returns the symbol of the ASCII/Unicode value.

"""

a = 1.5     # Float/Real
print(a, id(a), type(a))
a = "hello" # String/Character
print(a, id(a), type(a))
a = 5       # Integer
print(a, id(a), type(a))
a = True    # Logical
print(a, id(a), type(a))
a = 6.0+7.8j    # Complex
print(a, id(a), type(a))
a = [7, 8.9, 10] # List
print(a, id(a), type(a))
a = (5.2, 4, 12) # Tuple
print(a, id(a), type(a))
a = {'v1': 6, 'v2' : 10} # Dictionary
print(a, id(a), type(a))
# Get the ASCII/unicode value of a character
print(ord('z'))
# Get the character for the ASCII/unicode
print(chr(98))
print(chr(32250))
