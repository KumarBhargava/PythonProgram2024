import re

# In this Python code, we use the re module to work with regular expressions. Here's how the code works:
#
# We define the product cost as "$1234" and the number of products as 10.
# The regular expression pattern r'\d+' is used to match one or more digits in the string. Here's a breakdown of the pattern:
# \d: This represents any digit from 0 to 9.
# +: This quantifier means "one or more occurrences".
# The re.findall() function is used to find all occurrences of the pattern in the product cost string.
# If there is at least one match found, we extract the matched substring (which is the numeric value without the "$" symbol) and store it in the cost_string variable.
# We convert cost_string to an integer using int() and assign it to the cost variable.
# Finally, we calculate the total price by multiplying the cost by the number of products and print it to the console.
# Note: This code assumes that the product cost format is always in the format "$<numeric_value>". If the format varies, you may need to adjust the regular expression pattern accordingly.

product_cost = "$120"
number_of_product = 10

cost_pattern = re.compile(r'\d+')
matches = re.findall(cost_pattern, product_cost)

if matches:
    cost_string = matches[0]
    cost = int(cost_string)

    # calculate the total Price
    total_price = cost * number_of_product
    print(f"Total price of {number_of_product} number of product is {total_price}")
else:
    print("Invalid Price format.")
