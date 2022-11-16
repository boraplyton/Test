import pandas as pd

df = pd.read_excel('zdr2-4.xls') # ЗАБОЛЕВАЕМОСТЬ НАСЕЛЕНИЯ НАРКОМАНИЕЙ

#df = df.dropna() # удолили отсутствующие значения

print("\n\n\t\t\tDataFrame\n\n", df)

print("\n\n\t\t\tDataFrame  Без нулевых значений\n\n", df.fillna(method='bfill'))




print("\n\n\t\t\tАнализ полей DataFrame\n\n", df.describe()) # Рассчитали основные статистические показатели


print('\n\n\t\t\tСводная таблица\n\n', df.pivot_table( columns='Год'))    # Анаиз показателей заболеваемости по годам