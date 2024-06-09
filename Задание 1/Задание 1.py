
def is_palindrome(data):
    if data == data[::-1]:
        return True
    else:
        return False


def test_is_palindrome():
    # Тестовые случаи
    test_cases = [
        ("Abba", True),
        ("qwerq", False),
        ("raDaR", True),
        ("hello", False),
        ("A", True),
        ("", True),
        ("abcba", True),
        ("abcd", False),
        ("madaM", True),
        ("python", False),
    ]

    # Тестирование функции
    for test_case in test_cases:
        s, expected_result = test_case
        result = is_palindrome(s)
        if result == expected_result:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    test_is_palindrome()

