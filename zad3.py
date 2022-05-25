import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set()
df = pd.read_csv('iris.data', header=0, sep=',', decimal='.')

a = df['sepal length'][ df['class'] == "Iris-versicolor" ]

g = sns.relplot(
    data=df,
    x="petal length", )
