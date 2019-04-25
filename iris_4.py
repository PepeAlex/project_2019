# Alexander Pepe
# 21/04/2019
# Project 2019 - GMIT

# Shape of Iris Data Set

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()

print(iris['data'].shape)