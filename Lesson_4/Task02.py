# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

stroka = 'abc bcd abc bcd wwe \n qwe wwe qwe eeq'

stroka = stroka.split()

print(len(set(stroka)))



# решение с помощью генераторных выражений

stroka = 'abc bcd abc bcd wwe qwe wwe qwe eeq'

print({i:ord(i) for i in stroka})