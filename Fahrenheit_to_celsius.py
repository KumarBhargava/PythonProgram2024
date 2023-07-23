def convert_fahrenheit_to_celsius(t):
    temperature = ((t - 32) * 5) / 9
    print("Temperature in celsius is " + str(temperature))


def main():
    temp = float(input("Please provide the temperature in fahrenheit: "))
    convert_fahrenheit_to_celsius(temp)


if __name__ == "__main__":
    main()
