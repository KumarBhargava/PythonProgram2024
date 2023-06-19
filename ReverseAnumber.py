num = int(input("Enter a number to be reversed ")) # input funstion helps to take input from the user
rev = 0                                            # Initialize the rev variable
while num > 0:
    digit = num % 10           # take out the last digit from the number as "%" provide the last digit
    rev = rev * 10 + digit  # multiply the reverse by 10 and add the digit
    num = num // 10         # Remove the last digit from the number


print("Reversed number is: ",rev) # Print the reverse number

