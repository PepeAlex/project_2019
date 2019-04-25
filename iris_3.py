# Alexander Pepe
# 21/04/2019
# Project 2019 - GMIT

# Describe the statistic of Iris Data Set

import pandas as pd

iris = pd.read_csv("iris.csv")

i = iris.describe()
print(i)