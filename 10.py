#zadanie 1
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/x


x=np.setdiff1d(np.linspace(0,1,20),[0]) #to remove the zero
y=f(x)
plt.plot(y, x, label="1/x")
plt.axis([0,20,0,1])
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(loc='upper left')
plt.show()


#zadanie 2
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 1/x


x=np.setdiff1d(np.linspace(0,1,21),[0]) #to remove the zero
y=f(x)
plt.plot(x, y, 'g:^', label="1/x")
plt.axis([0,1,0,20])
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(loc='upper right')
plt.title("wykres funkcji f(x) dla x [1,20]")
plt.show()

#zadanie 3
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0, 30, 0.1)
s = np.sin(x)
d = np.cos(x)
plt.plot(x, s, label="sin(x)")
plt.plot(x, d, label="cos(x)")
plt.legend(loc='upper right')
plt.xlabel("x")
plt.ylabel("sin(x), cos(x)")
plt.title("wykres funkcji sin(x) i cos(x) x [1,30]")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = []
y = []

col_list = ["sepal length", "sepal width"]
df = pd.read_csv('iris.csv', skipinitialspace=True, usecols=col_list)


x = df["sepal length"]
y = df["sepal width"]
d=np.abs(x-y)
plt.scatter(x,y, c= np.random.randint(0,180,150), s=d)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

a = df['Liczba'][ df['Plec'] == "M" ].sum()
b = df['Liczba'][ df['Plec'] == "K" ].sum()
print(a)
print(b)

c = df.groupby(["Rok", "Plec"])["Liczba"].sum()
a_list = [a,b]
plec = ["chlopcy","dziewczynki"]

plt.bar(x = plec , height=a_list)
plt.xlabel('Plec')
plt.ylabel('Urodzenia w mln')
plt.show()

print(c)
