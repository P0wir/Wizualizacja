import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Zadanie 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
# print(df.to_string())
print(df)
print()

dff = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')

# grupa = df.groupby('Rok').agg({'Liczba' : ['sum']})
# print(grupa)
# grupa.plot(kind='line')
# plt.show()

#zadanie 2
# grupa = df.groupby('Plec').agg({'Liczba' : ['sum']})
# print(grupa)
# grupa.plot(kind='bar', title='urodzenia w mln')
# plt.legend(loc='upper left')
# plt.show()

#zadanie 3
# grupa = df[df['Rok'] > 2012].groupby('Rok').agg({'Liczba' : ['sum']})
# print(grupa)
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%')
# plt.show()

#zadanie 4
# grupa = dff.groupby('Sprzedawca').agg(
#         {'idZamowienia': ['count']})
# print(grupa)
# grupa.plot(kind='bar')
# plt.show()
