Rangeforce: developer-friendly range checks with user-friendly error messages
===============================================================================


Ever had to write the same old `if value < 0` bit of Python code to validate
a user input? Tired of unuseful error messages like _"Illegal value"_?
 
_Rangeforce_ is a very simple module offering multiple functions checking
the range of values, either integers or floats, or theirs lengths. It does
so in one line of code while providing an understandable error message that
can be displayed directly to the user as well.

```python
def classic_approach():
    value = int(input('Type a hex value: '), 16)
    if value < 0:
        raise ValueError('Value must be positive')
    elif value > 350:
        raise ValueError('Value must be <= 350')
    else:
        return value

# Same code, but simplified using Rangeforce
import rangeforce as rf

def with_rangeforce():
    value = int(input('Type a hex value: '), 16)
    return rf.limited(value, 0, 350)  # Here's the magic
```


Features
----------------------------------------


Installation
----------------------------------------


Example usage
----------------------------------------

```python
import rangeforce as rf

value = rf.limited(8000, 20, 5000, dtype=int)
# If successful, value will held 8000, otherwise (as it would happen in this
# example) raises a rangeforce.RangeError with a useful message:
# "Value must be in range [20, 5000]. 8000 found instead."
# Can be also shown directly to the user:

try:
    value = rf.limited(8000, 20, 5000, dtype=int)
except rf.RangeError as error:
    print(str(error))

# A missing bound (min or max) means unbounded
value = rf.limited(2000.0, None, 5000.0, dtype=float)
# Value must be <= 5000 but can be as small as it gets, including negative


# Especially useful in setters to validate the input in one line
class FullHdPicturesPixel(object):
    def __init__(self, x, y):
        self._x = None
        self._y = None
        self.x = x
        self.y = y
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, new_x):
        self._x = rf.limited(new_x, 0, 1920, 'The X pixel coordinate', int)
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, new_y):
        self._y = rf.limited(new_y, 0, 1080, 'The Y pixel coordinate', int)
        
pixel = FullHdPicturesPixel(10, 2000)
# This raises
# rangeforce.RangeError: The Y pixel coordinate must be in range [0, 1080]. 2000 found instead.


# Operating with C-like data structures and binary data?
# These functions might come in handy!
value = rf.int8(20) 
value = rf.int16(20) 
value = rf.int32(20) 
value = rf.int64(20)
value = rf.uint8(20) 
value = rf.uint16(20) 
value = rf.uint32(20) 
value = rf.uint64(20)

# Customize the name of the variable:
distance = rf.uint8(-3, 'Distance')
# This raises and error with the message:
# "Distance must be in range [0, 255]. -3 found instead."

# To check the length range of anything (e.g. a list or bytes):
value = rf.limited_len([1, 2, 3], 2, 7) # 'value' will hold [1, 2, 3]

# If you need an exact length, do it like this
pair = rf.exact_len([10, 20, 30], 2, name='pair of values')
# This raises and error with the message:
# "Length of pair of values must be exactly 2. 3 found instead.
```
