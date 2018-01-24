# Control flow relies on comparing one value to another in order to make some decision.
# The following comparison signs are supported:
# == (equal to), != (not equal to),
# < (less than), > (greater than),
# <= (less than or equal to), >= (greater than or equal to)
# You can also add 'not' keyword before the comparison to negate it, for example: (not True) == False

# If-statement is the basic option of controlling the flow of a program
# It contains three keywords: if, elif (short for 'else if') and else.
# If-statement goes through all the cases starting at the top, checking each case
# one by one until it falls into the one covering it and then it stops further resolution.
# In the example below, there are three cases and only one is executed depending
# on the value of days_left_till_end_of_world. Try playing with it by changing the value!
days_left_till_end_of_world = 0
if days_left_till_end_of_world > 7:
    # Value has to be greater than 7.
    print("Whatever, it's party time!")  # double-quoted string
elif days_left_till_end_of_world > 1:
    # Value has to be greater than 1 and it will be less than or equal to 7
    # because the previous case caught numbers greater than 7.
    print("We've still get enough time for a party.")
else:
    # Any value outside the ranges provided before will get you here.
    print("Today we die so let's party like there's no tomorrow.")
