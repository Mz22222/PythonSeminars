# Элементы из заданного диапазона
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементамиlist_1 и границы диапазона в виде чисел min_number, max_number.
# Пример
# На входе:
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# На выходе:
# 1
# 2
# 3
# 6
# 7
# 9
# 10
# 11
# 13
# 14
# 16
# 19



list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

# Введите ваше решение ниже

def elements_from_diap(list_1, min_number, max_number):

    result = []
    for i in range(len(list_1)):
        if min_number <= list_1[i] <= max_number:
            result.append(i)
    return result
    

result_i = elements_from_diap(list_1, min_number, max_number)
for index in result_i:
    print(index)
