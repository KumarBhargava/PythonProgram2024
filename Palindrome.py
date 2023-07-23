# Check if a string is palindrome or not , if not make it palindrome.

def is_palindrome(s):
    return s == s[::-1]


def make_palindrome(s):
    return s + s[::-1]


def main():
    string = input("Enter a string :")
    if is_palindrome(string):
        print("string is palindrome")
    else:
        palindrome = make_palindrome(string)
        print(f"New Palindrome string is {palindrome}")


if __name__ == "__main__":
    main()
