# Collections are used to store many values under the same name.
# There are three major collections that everyone should know:
# Lists, tuples and dictionaries.

# Definition of a list for different types:
empty_list = []  # This can also be achieved by using: empty_list = list()
list_of_ints = [1, 2, 3]  # list of ints (integers)
list_of_floats = [1.2, 4.3]  # list of floats
list_of_complex_values = [1+2j]  # list of complex's

# Definition of a tuple for different types:
empty_tuple = ()  # This can also be achieved by using: empty_tuple = tuple()
tuple_of_ints = (1, 2, 3)
tuple_of_floats = (1.2, 3.4)
tuple_of_complex_values = (1+2j,)

# Definition of a tuple with only one value is tricky. Be careful!
tuple_with_one_value = (1,)  # Notice the comma after the value. It's mandatory!
# If we forget the comma, Python interpreter will drop the parentheses and assign 1 (int) to the name.
not_a_tuple = (1)  # not_a_tuple is now an int type variable equal to 1
# This applies to other types as well:
tuple_with_one_complex_value = (1+2j,)
tuple_with_one_float = (2.3,)

# In Python, one collection can stored multiple values of different types:
list_of_different_types = [1, 2, 3, 1.2, 4.3, 'Cheers', (1,), [3, 4]]
tuple_of_different_types = (2, 3, 4.1, 'Cheers', [4, 3], (2,))
# This is possible but creates problems which will be discussed later in the course.

# Items in the list can be accessed through subscript notation, like this:
# some_list[index] - where index is an int not greater than the total amount of items in the list
assert list_of_ints[0] == 1  # First item, index: zero
assert list_of_ints[1] == 2  # Second item, index: one
assert list_of_ints[2] == 3  # Third item, index: two
# We need to stop here or else we'll try to access an item that is out of bounds.
# This will cause the program to crash with this message: "IndexError: list index out of range".
# You can try it out by uncommenting the line below:
# list_of_ints[3]  # uncomment me, I dear you!

# Ok, so we now know how to access the items in the collection and we are aware that this is a little bit dangerous
# if we don't know the size of the collection which items we are trying to access.
# We can check the size of the collection by calling len function on it:
len(list_of_ints)
len(tuple_of_ints)
# We just need to remember that we can access all of the items for indexes equal or greater than 0
# but at the same time the index needs to be less than len(some_collection) where some_collection is the collection
# which items we are trying to access.
