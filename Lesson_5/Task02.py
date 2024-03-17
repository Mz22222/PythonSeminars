# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Пример: 
# [1, 3, 4, 1, 5, 1, 5] -> [1, 3, 4, 1, 1, 1 , 1]

import copy

def zamena(array:list[int]) -> list[int]:
    max_value = max(array)
    min_value = min(array)
    new_marks = copy.copy(array)

    for i in range(len(array)):
        if new_marks[i] == max_value:
           new_marks[i] = min_value
    return new_marks

marks = [1, 3, 4, 1, 5, 1, 5]
zamena(marks)
print(zamena(marks))