import numpy as np
import pandas as pd

# s1 = pd.Series([10,12,8,14], index=['a','b','c','d'])
# print(s1)
#
# dane = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
#         'Populacja' : [11190846, 1303171035, 207847528]}
#
# df = pd.DataFrame(dane)
# # print(df)
# #
# # daty = pd.date_range('20220420', periods=5)
# # df = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
# # print(df)
# #
# iris_df = pd.read_csv('iris.csv', header=0, sep=',', decimal='.')
# print(iris_df)
# # iris_df.to_csv('nowy.csv', index=False)
#
# # print(s1['a'])
# # print(s1.a)
# #
# # print(df['Populacja'])
# # print(df.Populacja)
# #
# # print(df.iloc[0], [1])
# # print(df.loc[[0], ['Kraj']])
# # print(df.at[0, 'Kraj'])
#
# print(df.sample(1))
# print(df.sample(frac=0.5))
#
# print('')
# print(df.sample(2, replace=True))
#
# print(iris_df.head(10))
# print(iris_df.tail(10))
#
# print(s1[s1 > 10])
# print(s1.where(s1 > 10))
#
# seria=s1.copy()
# print(seria)
# seria.where(s1 >10, 'element nie spelnia warunku', inplace=True)
# print(seria)
#
# print(s1[~(s1 >10)])
# print(s1[(s1 <13) & (s1 >8)])
#
# print(df[df['Populacja'] > 120000000000])
# print(df[(df.Populacja > 1000000) & (df.index.isin([0,2]))])
#
# szukaj = ['Belgia', 'Brasilia']
# print(df.isin(szukaj))
#
# s1['e'] = 15
# print(s1)
#
# df.loc[3] = 'nowy element'
# df.loc[4] = ['Polska', 'Warszawa', 38675467]
#
# print(df)
#
# df.drop(3, inplace=True)
# print(df)
# df.drop('Kraj', axis=1 inplace=True)
# print(df)
# df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa']
# print(df)
# print(df.sort_values(by='Kraj'))
# grupa = df.groupby(by='Kontynent')
# print
# print(grupa.get_group('Europa'))
#
# print(df.groupby(by='Kontynent').agg({'Populacja': ['sum']}))

# Zadanie 1
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
# print(df.to_string())
print(df)
print()

#zadanie 2
#1
print(df[(df['Liczba'] > 1000 ) & (df['Rok'] == 2002)])
#2
print(df[df['Imie']=='MATEUSZ'])
#3
print(df.agg({'Liczba': ['sum']}))
#4
print(df.agg({'Liczba': ['sum']})df.where['Rok'] == 2000)
