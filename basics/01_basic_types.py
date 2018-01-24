# coding=utf-8
# This line will be explained in a moment :)

# Lines starting with a hash sign are considered comments.
# If hash sign is added after something else, everything up to the end of line is considered a comment.

# Initialization (definition) of a variable is done by assigning a value to some name:
one = 1  # Variable 'one' is assigned a value 1 of type int (as in integer).
two_and_a_half = 2.5  # floating-point variable (real number).
abs_five = 3+4j  # complex number (imaginary number).
is_this_the_real_life = True  # boolean variable which allows only True or False as its values
is_this_just_fantasy = False  # counter-part of True :)

# We can be explicit about the type by calling it directly before assignment:
integer_value = int(1)
floating_point_value = float(2.3)
complex_value = complex(1, 2)
# This is not that useful for declaration but we can benefit from this
# when we convert the value of one type into a value of some other type.
four = int(4.6)  # Converting float to int cuts the part after the dot
three_point_zero = float(3)  # Converting int to float adds .0 to the int value
# Be careful about converting very big integers! Ints can be infinitely long while floats don't.
# This means that if you convert a huge integer to float, the results might be different than you expected!
# very_long_int = 2345678912347636498
# very_long_int_converted_to_float = float(very_long_int)
# If you compare these two variables, you will see what I mean:
# print(int(very_long_int_converted_to_float) - very_long_int)

# Strings are a bit complicated due to differences between major Python versions but to make it short
# everything surrounded with single-quotes, double-quotes or triple-quotes (used for docstrings)
# and is understood as some representation of text.
# There is a major difference how text (strings) are handled in Python between its major versions.
# Python 2.7: 'str' type is used for ASCII encoded strings (basically latin alphabet without special characters),
#             while 'unicode' is used for extended notation, for example: chinese and/or polish characters
# Python 3+:  'str' is the same as old 'unicode' type, old 'unicode' type is removed (!)
#             and old 'str' type definition is changed to 'bytes'
# Let's see an example:
question = 'How do the Polish people call jam?'  # Python 2.7: str type / Python 3+: bytes type

# Declaring answer variable with value 'Dżem' will crash the program as 'ż' is a non-ASCII character.
# This will raise a SyntaxError exception which can be avoided by adding 'coding=utf-8' line
# at the beginning of the file. This lets us use non-ASCII characters both for str and unicode types
# as Python will take care of converting non-ASCII characters to their proper representation for given type:
unicode_jam_in_polish = u'Dżem'  # answer's value: u'D\u017cem'
ascii_jam_in_polish = 'Dżem'  # assigned value: 'D\xc5\xbcem'

# If this gives you a headache, don't worry, it's normal.
# For now, keep in mind that it's better to use english until you get a better grasp of Python's syntax.
