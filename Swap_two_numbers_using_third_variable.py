def main():
    first_num = int(input("Please enter the first number to swap"))
    second_num = int(input("PLease enter the second number to swap"))
    temp = first_num
    first_num = second_num
    second_num = temp
    print(f'After swapping first number is: {first_num} and second number is {second_num}')


if __name__ == "__main__":
    main()
