# Напишите программу для печати всех уникальных значений в словаре

# 1-й вариант
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

data1 = []
for dictn in data:
    for val in dictn:
        data1.append(dictn.get(val))
    dict_set = set(data1)
print(dict_set)


# 2-й вариант
dict_ = {
    "V": 1,
    "R": 1,
    "T": 2,
    "А": 2
}
# for i in dict_:
#     print (i)
print(set(dict_.values()))


# 3-й вариант
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

res = set ()
for d in data:
    for element in d.values():
        res.add (element),
print(res)


# 4-й вариант
data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

res = set ()
for d in data:
   res = res.union(set(d.values()))
print(res)

