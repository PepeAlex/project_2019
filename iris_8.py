import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
sns.set(color_codes=True)

df = pd.read_csv('iris.csv')

df.hist(figsize=(10,5))

plt.show()