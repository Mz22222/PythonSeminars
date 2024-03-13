# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# Input: aaabcaadcdd
# Output: aa_1a_2bca_3a_4dc_1d_1d_2


a = 'aaabcaadcdd'
b = ''
slovar = {}

for i in a:
    if i not in slovar:
        slovar[i] = 0
        b += i
    else:
        slovar[i] += 1
        b += f'{i}_{slovar[i]}' # {i} - ключ, slovar[i] - значение ключа
print(b)