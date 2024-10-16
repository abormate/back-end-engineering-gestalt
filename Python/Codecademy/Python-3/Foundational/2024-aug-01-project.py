# ------------------------------------------- #
#
# -- Python LearnSpace -- Loveseats Receipts -- 
#
# ------------------------------------------- #

"""

Weve decided to pursue the dream of small-business ownership and 
open up a furniture store called Lovely Loveseats for Neat Suites 
on Fleet Street. With our newfound knowledge of Python programming, 
were going to build a system to help speed up the process of 
creating receipts for your customers.

In this project, we will be storing the names and prices of a 
furniture stores catalog in variables. You will then process 
the total price and item list of customers, printing them to 
the output terminal.

"""

# ----------------- #
# -- Task 00 --
# ----------------- #

"""
Lets add in our first item, the Lovely Loveseat that is the 
stores namesake. Create a variable called 
lovely_loveseat_description and assign to it the following 
string:

"""

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."

# ---------------- #
# -- Task 01 --
# ---------------- #

"""
Great, now lets create a price for the loveseat. Create a variable lovely_loveseat_price and set it equal to 254.00.

"""

lovely_loveseat_price = 254.00

# ---------------- #
# -- Task 02 --
# ---------------- #

"""
Lets extend our inventory with another characteristic 
piece of furniture! Create a variable called 
stylish_settee_description and assign to it the following 
string:

"""

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

# ---------------- #
# -- Task 03 --
# ---------------- #

"""
Now lets set the price for our Stylish Settee. Create a 
variable stylish_settee_price and assign it the value of 
180.50.

"""

stylish_settee_price = 180.50


# --------------- #
# -- Task 04 --
# --------------- #

"""
Fantastic, we just need one more item before were ready for 
business. Create a new variable called 
luxurious_lamp_description and assign it the following:

"""

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

# -------------- #
# -- Task 05 --
# -------------- #

"""
Lets set the price for this item. Create a variable called 
luxurious_lamp_price and set it equal to 52.15.

"""

luxurious_lamp_price = 52.15

# --------------- #
# -- Task 06 --
# --------------- #

"""
In order to be a business, we should also be calculating 
sales tax. Lets store that in a variable as well.

Define the variable sales_tax and set it equal to .088. 
Thats 8.8%.

"""

sales_tax = 0.088

# --------------- #
# -- Task 07 --
# --------------- #

"""
Our first customer is making their purchase! Lets keep a 
running tally of their expenses by defining a variable called
customer_one_total. Since they havent purchased anything yet, 
lets set that variable equal to 0 for now.

"""

customer_one_total = 0

# --------------- #
# -- Task 08 --
# --------------- #

"""
We should also keep a list of the descriptions of things 
theyre purchasing. Create a variable called 
customer_one_itemization and set that equal to the empty 
string "". Well tack on the descriptions to this as they 
make their purchases.

"""

customer_one_itemization = ""

# -------------- #
# -- Task 09 --
# -------------- #

"""
Our customer has decided they are going to purchase our 
Lovely Loveseat! Add the price to customer_one_total.

"""

customer_one_total = 254.00

# ------------- #
# -- Task 10 --
# ------------- #

"""
Lets start keeping track of the items our customer purchased. 
Add the description of the Lovely Loveseat to 
customer_one_itemization.

"""

customer_one_itemization = lovely_loveseat_description

# ------------ #
# -- Task 11 --
# ------------ #

"""
Our customer has also decided to purchase the Luxurious Lamp! 
Lets add the price to the customers total.

"""

customer_one_total = luxurious_lamp_price

customer_one_itemization += luxurious_lamp_description

# ----------- #
# -- Task 12 --
# ----------- #

"""
Theyre ready to check out! Lets begin by calculating sales 
tax. Create a variable called customer_one_tax and set it 
equal to customer_one_total times sales_tax

"""

customer_one_tax = customer_one_total * sales_tax

# ---------- #
# -- Task 13 --
# ---------- #

"""
Add the sales tax to the customers total cost.

"""

customer_one_total += customer_one_tax

# -------------- #
# -- Task 014 --
# -------------- #

"""
Lets start printing up their receipt! Begin by printing out 
the heading for their itemization. Print the phrase 
"Customer One Items:".

"""

print("Customer One Items: ")

# ----------------- #
# -- Task 015 --
# ----------------- #

"""
Print customer_one_itemization.

"""

print(customer_one_itemization)

# ------------------ #
# -- Task 016 --
# ------------------ #

"""
Now add a heading for their total cost: Print out 
"Customer One Total:"

"""

print("Customer One Total: ")

# ------------------ #
# -- Task 017 --
# ------------------ #

"""
Now print out their total! Our first customer now has a 
receipt for the things they purchased.

"""

print(customer_one_total)

print("thank you... keep well.")


