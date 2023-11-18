# ---------------------------------------- #
#
# -- Bitwise and Ampersand (&) --
#
# ---------------------------------------- #

"""
Bitwise operators are similar to logical operators, but instead of operating on 
boolean values, they apply the same logic to all the bits in a value. For example, 
say you had the numbers 5 and 7 represented in binary. You could perform a 
bitwise AND operation and the result would be 5.

Example --
0101 = 5
&
0111 = 7
=
0101 = 5


A 1 in binary is the same as True, while 0 is False. So really a bitwise operation 
is just a bunch of logical operations that are completed in tandem.

& is the bitwise AND operator in Python. 5 & 7 = 5, while 5 & 2 = 0.


Example

0101 = 5
&
0010 = 2
=
0000 = 0

"""