import string


def strip_punctuation_ru(data):
    # Удаляем знаки препинания
    translator = str.maketrans('', '', string.punctuation)
    data_no_punct = data.translate(translator)

    # Разделяем строку на слова
    words = data_no_punct.split()

    # Возвращаем слова, разделенные одним пробелом
    return ' '.join(words)


if __name__ == "__main__":
    entered_string = input("Введите строку: ")
    print(strip_punctuation_ru(entered_string))
