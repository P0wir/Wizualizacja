import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

A = np.linspace(-2,2, num=100)

a = np.tan(A)
b = np.sin(A)

d = a+b
print(a+b)
plt.plot(A, d, label="tan(x)+sin(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(loc='upper left')
plt.show()


