# Alexander Pepe
# 21/04/2019
# Project 2019 - GMIT

# Features of Iris Data Set

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

print(iris['feature_names'])