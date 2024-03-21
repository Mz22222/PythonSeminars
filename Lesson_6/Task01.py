# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива

def add_in_the_end(array1: list[int], array2: list[int]) -> list[int]:
    result = []
    for i in array1:
        if i not in array2:
          result.append(i)
    return result


array1 = [1, 2, 3, 4, 5]
array2 = [6, 2, 8, 5, 0]
print(add_in_the_end(array1, array2))