# import os
# import sys


# def add_new_user(name: str, phone: str, filename: str):
#     """
#     Добавление нового пользователя.
#     """
#     pass


# def read_all(filename: str) -> str:
#     """
#     Возвращает все содержимое телефонной книги.
#     """
#     with open("Number.txt", "r", encoding="utf-8") as file:
#         return file.read()


# def search_user(data: str) -> str:
#     """
#     Поиск записи по критерию data.
#     """
#     pass


# INFO_STRING = """
# Выберите режим работы:
# 1 - вывести все данные
# 2 - добавление нового пользователя
# 3 - поиск
# """

# file = "Number.txt"

# if file not in os.listdir():
#     print("указанное имя файла отсутсвует")
#     sys.exit()


# while True:
#     mode = int(input(INFO_STRING))
#     if mode == 1:
#         print(read_all(file))
#         pass
#     elif mode == 2:
#         pass
#     elif mode == 3:
#         pass


import os
import sys


def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''

    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line}{name} - {phone}")





def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    pass


INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
"""

file = "Number.txt"

if file not in os.listdir():
    print("указанное имя файла отсутсвует")
    sys.exit()



while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))
        pass
    elif mode == 2:
        name = input("Введите Ваше имя: ")
        phone = input("Введите Ваш телефон: ")
        add_new_user(name, phone, file)
        pass
    elif mode == 3:
        pass