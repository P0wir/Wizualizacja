import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(1,21,1)
# print(x)
#
# def f(x):
#     return (x**2+4*x)/np.sin(x)
#
# plt.plot(x,f(x),'g^:')
# plt.axis([1,20,0,650])
# plt.title("zadanie 1 - wykres")
# plt.show()

x1 = np.arange(-2,2.1,0.1)
x2 = np.arange(-3,3.1,0.1)
y1 = np.tan(x1)*np.sin(x1)
y2 = np.tan(x2)+np.sin(x2)

fig,axs = plt.subplots(2,2)
axs[0,1].plot(x1,y1,'g:')
# (’-’, ’–’, ’-.’, ’:’, 'None’, ’ ’, ”, 'solid’, 'dashed’, 'dashdot’, 'dotted’)
axs[0,1].set_title("wykres x1")
axs[0,1].set_xlabel("x1")
axs[0,1].set_ylabel("y1")
axs[0,1].legend("wykres funckji f(x1)")

axs[1,0].plot(x2,y2)
axs[1,0].set_title("wykres x2")
axs[1,0].set_xlabel("x2")
axs[1,0].set_ylabel("y2")
axs[1,0].legend("wykres funkcji f(x2)")
axs[1,0].axis([-3,3,-40,40])
plt.savefig("powir.png")
plt.show()

# sns.set()
# df=pd.read_csv('iris.data',header=0,sep=',',decimal='.')
# print(df)
# x = df['petal length'].where(df['class']=="Iris-versicolor")
# y = df['petal width'].where(df['class']=="Iris-versicolor")
#
# wykres=sns.relplot(data=df, x=x, y=y, hue='class', palette='dark')
# plt.show()

sns.set()
df=pd.read_csv('automobile.csv',header=0,sep=';',decimal='.')
y2 = df.groupby(['Car model'])['Price'].agg(sum)
filt = df[['Car model','Price']].where(df['Fuel-type']=='gas').groupby(['Car model']).count()
print(filt)
plot = sns.catplot(data=df, x = 'Car model', y = 'Price', kind='bar', ci=None, hue = 'Car model', estimator = np.sum, dodge = False)
plt.title("ceny samochodow")
plot.fig.set_size_inches(10,10)
plt.xticks(rotation = "vertical")
plt.show()

# x1 = np.random.randint(0,20,100)
# y1 = np.random.randint(0,20,100)
# print(x1)
# plt.axis([1,20,1,20])
# sns.set()
# sns.relplot(data = x1, x=x1, y=y1)
# plt.show()
