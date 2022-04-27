import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
#
# ts.plot()
# plt.show()

# dane = {'Kraj': ['Belgia','Indie','Brazylia','Polska'],
#         'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         'Populacja': [11190846, 1303171035, 207847528, 38675467],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Poludniowa', 'Europa']}
#
# df = pd.DataFrame(dane)
#
# grupa = df.groupby('Kontynent').agg({'Populacja' : ['sum']})
# print(grupa)
# grupa.plot(kind='bar', xlabel = 'Kontynent', ylabel = 'Populacja w mln', rot=0, title = 'populacja')
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Kontynent')
# wykres.set_ylabel('Populacja w mld')
# wykres.tick_params(axis='x', labelrotation=0)
# plt.savefig('plot.png')
#
df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
print(df)

grupa = df.groupby('Imię i nazwisko').agg(
        {'Wartość zamówienia': ['sum']})

grupa.plot(kind='pie', subplots=True, autopct='%.2f %%',
           fontsize=20, figsize=(8, 8), colors=['red', 'green'])
plt.legend(loc='upper left')
plt.show()
