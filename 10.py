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
