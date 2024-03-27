# Напишите функцию same_by(characteristic, objects), 
# которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

# def same_by(characteristic: callable,
#             elements: list) -> bool:
#     pass


# def is_odd(element: int) -> bool:
#     return element % 2 == 0


# elements1 = [2, 4, 6, 8, 10] # -> True
# elements2 = [1, 2, 3, 4, 5] # -> False




def same_by(charc, obj) -> bool:
    return len(set(map(charc, obj))) <= 1

values = [2,4,6,8]

print(same_by(lambda x: x % 2 == 0, values))


# print(list(map(lambda x: str(x), values)))



# /////////////////////////////////////////////////////////////////////////////////////////////

# реализация через all
def same_by(charc, obj) -> bool:
    obj = map(charc, obj)
    return all(obj) or not any(obj)


elements1 = [2, 4, 6, 8, 10] # -> True
elements2 = [1, 2, 3, 4, 5] # -> False
elements3 = [1, 3, 5, 7, 9] # -> True
print(elements1, same_by(lambda x: x % 2 == 0, elements1))
print(elements2, same_by(lambda x: x % 2 == 0, elements2))
print(elements3, same_by(lambda x: x % 2 == 0, elements3))