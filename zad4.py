import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set()
df = pd.read_csv('automobile.csv', header=0, sep=',', decimal='.')
print(df)

print(df.groupby(by='Car model').agg({'price': ['sum']}))
