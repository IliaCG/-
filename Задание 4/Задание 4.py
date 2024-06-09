def is_correct_mobile_phone_number(number):
    # Удаление пробелов, дефисов, скобок
    number = number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

    # Проверка, начинается ли номер с 8 или +7
    if not (number.startswith("8") or number.startswith("+7")):
        return "No"

    # Удаление + перед 7, если он есть
    if number.startswith("+7"):
        number = number[1:]

    # Проверяем, является ли код оператора трехзначным числом
    if not number[1:4].isdigit():
        return "No"

    # Проверка, является ли остальная часть номера семизначной
    if not number[4:].isdigit() or len(number[4:]) != 7:
        return "No"

    return "Yes"


if __name__ == "__main__":
    phone_number = input("Введите номер телефона: ")
    print(is_correct_mobile_phone_number(phone_number))
