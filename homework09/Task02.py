# Максимальная households

# Дан файл california_housing_train.csv.
# Найти максимальное значение переменной "households" в зоне минимального значения переменной min_population 
# и сохраните это значение в переменную max_households_in_min_population.
# Используйте модуль pandas.

import pandas 

df = pandas.read_csv('california_housing_train.csv')

max_households_in_min_population = df[df['population'] == df['population'].min()]['households'].max()
