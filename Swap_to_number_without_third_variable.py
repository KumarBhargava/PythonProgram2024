def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    print("Number after swapping are "+str(a)+" and "+str(b))


def main():
    x = int(input("Enter the first number to swap"))
    y = int(input("Enter the second number to swap"))
    swap(x, y)


if __name__ == "__main__":
    main()
