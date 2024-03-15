# генераторы:

from pprint import pprint

# numbers = ["f" for i in range(1, 11)]
# print(numbers)
# numbers_set = {"f" for i in range(1, 11)}
# print(numbers_set)
# numbers_dict = {i: "f" for i in range(1, 11)}
# print(numbers_dict)

# even_numbers = [i for i in range(1, 11) if i % 2 == 0]
# print(even_numbers)

# even_numbers_or_0 = [bool(i) for i in range(1, 11)]
# print(even_numbers_or_0)

# b = 4
# a = b if b % 2 == 0 else 0
# print(a)

# numbers = [i*j for i in range(1, 10) for j in range(10, 20)]
# print(numbers)

# for j in range(10, 20):
# for i in range(1, 10):
# print(i*j)


# методы в словарях:

numbers_dict = {i: "f" for i in range(1, 11)}
# print(numbers_dict[19])
# print(numbers_dict.items(), numbers_dict.values(), numbers_dict.keys())
print(numbers_dict.pop(1))
numbers_dict.update({19: "manmg", 18: "afugn", 2: "fajnfgn"})
pprint(numbers_dict)

g = [2, 5, 10, 3, 1]
print(set(g))