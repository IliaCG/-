
def is_palindrome(data):
    if data == data[::-1]:
        return "Yes"
    else:
        return "No"


if __name__ == "__main__":
    str = input("Введите строку: ").strip()
    print(is_palindrome(str))
