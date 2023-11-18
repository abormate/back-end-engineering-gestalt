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

# -------------------------- #
# Guild Permissions
# -------------------------- #

"""
It sometimes is the case that applications store user permissions as binary values. 
Think about it, if I have 4 different permissions a user can have, then I can 
store that as a 4-digit binary number, and if a certain bit is present, I know 
the permission is enabled. This can be a lot more efficient than storing entire 
strings.

Let's think we have 4 permissions related to "guilds" in Fantasy Quest ("guild" 
is just a fancy videogame word for "team"):

can_create_guild - Leftmost bit (0b1000)
can_review_guild - Second to leftmost bit (0b0100)
can_delete_guild - Second to rightmost bit (0b0010)
can_edit_guild - Rightmost bit (0b0001)

If a user has no permissions, their binary permissions would be 0b0000.

If a user only has the can_create_guild permission, their binary permissions 
would be 0b1000, but a user with can_review_guild and can_edit_guild permissions 
would be 0b0101.

To check for, say, the can_review_guild permission, we can perform a bitwise AND 
operation on the user's permissions and the enabled can_review_guild bit (0b0100).

If the result is 0b0100 again, we know they have that specific permission!


"""



