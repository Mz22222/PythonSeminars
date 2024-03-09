# Деление шоколадки
# Определите, можно ли от шоколадки размером a × b долек отломить c долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# Выведите yes или no соответственно.

# Пример:
# a, b, c = 3, 2, 4 -> yes
# a, b, c = 3, 2, 1 -> no


a = 3
b = 2
c = 1


chockolate = a * b 
if c <= chockolate and (c%a == 0 or c%b == 0):
    print('yes')
else:
    print('no')

# или другой вариант решения: 
if c % a == 0 or c % b == 0:
    print('yes')
else:
    print('no')