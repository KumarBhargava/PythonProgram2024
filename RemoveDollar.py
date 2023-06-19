import re

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
