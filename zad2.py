import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

x_lista = []
for x in range(1,21):
    x_lista.append((x*x)+4*x)
print(x_lista)

d = np.sin(x_lista)
print(d)



x=x_lista
y=x/d
sns.lineplot(x, y, label='linia nr 1', color='red', marker='o', linestyle=':')
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(loc='upper left')
plt.title("wykres funkcji f(x) dla x [1,20]")
plt.show()
