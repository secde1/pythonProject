# import re
# def user_name(name):
#     pattern = r'^[A-Z][a-zA-Z\s]*$'
#     result = re.match(pattern, name)
#     return result
#
# name = input("Введите ваше имя: ")
# if user_name(name):
#     print("имя актуально!")
# else:
#     print("Неверный формат имени! Пожалуйста, введите верное имя.")

import re


def number(phone_number):
    # pattern = r'^\+9989[0-5|7-9]\d{7}$'
    pattern = r'^\+998-(99|97|95|93|91|90|88|77|55)-\d{3}-\d{4}$'
    return re.match(pattern, phone_number) is not None

phone_numbers = ["+998-90-997-9548",]

for i in phone_numbers:
    if number(i):
        print(f"{i} - Telefon raqami to'g'ri formatda.")
    else:
        print(f"{i} - Telefon raqami noto'g'ri formatda.")












# name = name.capitalize()  # Birinchi harfni katta harf bilan boshlash uchun capitalize() metodi qo'llaniladi