# ЗДЕСЬ НЕ РУБИТ!!
# ЭТО ДЛЯ КОЛАБА, НО СОХРАНЮ ЗДЕСЬ, ЧТОБЫ БЫЛО 


# Определить среднюю стоимость дома

# Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
# Используйте модуль pandas.




import pandas 

df = pandas.read_csv('california_housing_train.csv')

avg = df[(df['population'] >= 0) & (df['population'] <= 500)]['median_house_value'].mean()