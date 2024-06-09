def is_correct_mobile_phone_number(number):
    # Удаление пробелов, дефисов, скобок
    number = number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

    # Проверка, начинается ли номер с 8 или +7
    if not (number.startswith("8") or number.startswith("+7")):
        return False

    # Удаление + перед 7, если он есть
    if number.startswith("+7"):
        number = number[1:]

    # Проверяем, является ли код оператора трехзначным числом
    if not number[1:4].isdigit():
        return False

    # Проверка, является ли остальная часть номера семизначной
    if not number[4:].isdigit() or len(number[4:]) != 7:
        return False

    return True


def test_is_correct_mobile_phone_number():
    test_cases = [
        ("6324652195", False),
        ("8901234567", True),
        ("+79901234567", True),
        ("+7(900)1234567", True),
        ("+7 999 123-45-67", True),
        ("890123456", False),
        ("+7990123456", False),
        ("+7(900)123456", False),
        ("+7 999 123-45-6", False),
    ]

    tests_failed = False
    for test_case in test_cases:
        number, expected_result = test_case
        result = is_correct_mobile_phone_number(number)
        if result == expected_result:
            print(f"Тест номера '{number}' пройден.")
        else:
            print(f"Тест номера '{number}' не пройден.")
            tests_failed = True

    if not tests_failed:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    test_is_correct_mobile_phone_number()
