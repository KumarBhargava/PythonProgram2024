def take_different_input_from_user():
    num = input("Please provide a integer value as input: ")
    print('Provided integer input is: ' + num)
    float = input("Please provide a floating point number: ")
    print('provided floating point number is: ' + float)
    str = input("Please provide a string value as input: ")
    print('Provided String input is: ' + str)


def main():
    take_different_input_from_user()


if __name__ == "__main__":
    main()
