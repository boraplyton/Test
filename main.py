import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_excel('zdr2-4.xls') # ЗАБОЛЕВАЕМОСТЬ НАСЕЛЕНИЯ НАРКОМАНИЕЙ

#df = df.dropna() # удaлили отсутствующие значения

print("\n\n\t\t\tDataFrame\n\n", df)

print("\n\n\t\t\tDataFrame  Без нулевых значений\n\n", df.fillna(method='bfill'))
df = df.fillna(method='bfill')
print("\n\n\t\t\tАнализ полей DataFrame\n\n", df.describe()) # Рассчитали основные статистические показатели


#print('\n\n\t\t\tСводная таблица\n\n', df.pivot_table(columns='Год'))    # Анаиз показателей заболеваемости по годам

print("Сумма 2003 = ", df[2003].sum())
print("Сумма 2004 = ", df[2004].sum())
print("Сумма 2005 = ", df[2005].sum())


names = ['Сумма 2003', 'Сумма 2004', 'Сумма 2005']
values = [df[2003].sum(),df[2004].sum(),df[2005].sum()]

plt.figure(figsize=(12,5))

plt.bar(names, values)
plt.savefig('task.png')
plt.show()
