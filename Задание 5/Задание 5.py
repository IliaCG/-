import string

def strip_punctuation_ru(data):
    # Удаляем знаки препинания
    translator = str.maketrans('', '', string.punctuation)
    data_no_punct = data.translate(translator)

    # Разделяем строку на слова
    words = data_no_punct.split()

    # Возвращаем слова, разделенные одним пробелом
    return ' '.join(words)

def test_strip_punctuation_ru():
    test_cases = [
        ("Привет, мир!", "Привет мир"),
        ("Тестовая строка...", "Тестовая строка"),
        ("(Удалить скобки)!", "Удалить скобки"),
        ("Восклицательный знак!", "Восклицательный знак"),
        ("Запятая, и точки, и т.д.", "Запятая и точки и т д"),
        ("Привет,   мир!", "Привет мир"),
    ]

    tests_failed = False
    for test_case in test_cases:
        data, expected_result = test_case
        result = strip_punctuation_ru(data)
        if result == expected_result:
            print(f"Test passed for '{data}': {result}")
        else:
            print(f"Test failed for '{data}': expected {expected_result}, got {result}")
            fail = True

    if not tests_failed:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    test_strip_punctuation_ru()