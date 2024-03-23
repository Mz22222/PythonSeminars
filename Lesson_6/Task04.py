# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) 
# равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел,
# каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. 
# Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. 
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

def del_sum(num: int) -> int:
    count = 0
    for i in range(1, num//2 + 1):
        if num % i == 0:
            count += i
    return count

def friendly_num (k: int) -> set:
    set_num = set()
    for i in range(220, k):
        for j in range(i+1, k):
            if del_sum(i) == j and del_sum(j) == i:
                set_num.add((i,j))
    return set_num

print(friendly_num(1000))

# или более оптимизированная версия (более быстрая)
def del_sum(num: int) -> int:
    count = 0
    for i in range(1, num//2 + 1):
        if num % i == 0:
            count += i
    return count

def friendly_num (k: int) -> set:
    set_num = {}
    for i in range(220, k):
        del_num = del_sum(i)
        if (i == del_num) or (i in set_num or del_num in set_num):
            continue
        if del_sum(del_num) == i:
            set_num.update({i: del_num})
    return set_num

print(friendly_num(1000))



# окончательный вариант 


def del_sum(num: int) -> int:
    count = 1
    for i in range(2, int(num**0.5)):
        if num % i == 0:
            count += (i + num//i)
    return count


def friendly_num(k: int) -> set:
    set_num = {}
    for i in range(220, k):
        del_num = del_sum(i)
        if (i == del_num) or (i in set_num or del_num in set_num):
            continue
        if del_sum(del_num) == i:
            set_num.update({i: del_num})
    return set_num

print(friendly_num(1000))
