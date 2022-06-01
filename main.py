import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#zadanie 1

# x = np.arange(1,11,0.14)
# def f(x):
#     return (np.tan(x)+np.cos(x))/x**2
#
# plt.plot(x,f(x))
# plt.title("wykres dla 70 liczb")
# plt.xlabel("liczby")
# plt.ylabel("wartosci")
# plt.show()

#zadanie 2

# x1 = np.arange(1,10.1,0.05)
# x2 = np.arange(1,10.1,0.1)
#
# y1 = (np.sin(x1)+np.tan(x1))/(2*x1)
# y2 = (np.sin(x2)*(3*x2))/2
#
# plt.plot(x1,y1,'r')
# plt.plot(x2,y2,'g')
# plt.legend(['sin(x)+tan(x))/2x', 'sin(x)*3x/2'], loc ="upper left")
# plt.title("wykres liniowy dwoch funkcji")
#
# plt.savefig("powirski.png")
# plt.show()

#zadanie 3
# df=pd.read_csv('flags.csv',sep=';',decimal='.')
# print(df)
# filt = df[['Country']].where(df['Landmass']=='Asia')
# filt2 = df[['Country']].where(df['Landmass']=='Africa')
# print(filt2)
# print(filt)
#
# x = df['Country'].where(df['Landmass']=="Asia").count()
# x2 = df['Country'].where(df['Landmass']=="Africa").count()
#
# plt.bar(1, df['Country'].where(df['Landmass']=="Asia").count())
# plt.bar(2, df['Country'].where(df['Landmass']=="Africa").count())
# plt.axis([1,2,0,45])
# plt.xlabel=('kraje')
# plt.ylabel=('liczba krai')
# plt.title('Kraje')
# plt.show()

#zadanie 4
# df=pd.read_csv('flags.csv',sep=';',decimal='.')
# x = df['Religion'].groupby(df['Religion']).count()
# wykres = x.plot.pie(autopct=lambda pct: "{:.2f}%".format(pct), fontsize=14)
# plt.title("religie w krajach")
# plt.legend(loc="lower left")
# plt.show()
# print(x)
