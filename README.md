# project_2019

Project
“Fisher”
Iris Data Set.


Programming and Scripting
GMIT
April 2019
Autor: Alexander Pepe


This project is investigative. Research has been done on several sources, all of which have been related at work, to understand how to use programming in data extraction and compilation of data, thus helping everyone to understand.
For the visualization of the project it is necessary to have installed into a computer Python and its libraries, Visual Studio Code and cmder. This Project is avaible to see and to download in the following link:
https://github.com/PepeAlex

Who is Fisher?

Ronald Aylmer Fisher was born into a wealthy family in London, England, UK on February 17, 1890. He was the second born of twins.
Even at school, Fisher viewed himself as a scientist who was especially interested in biology. He did not, however, enjoy learning the names and details of biological structures. He decided to study mathematics, believing it was through mathematics he could make the greatest contributions to biology.
After graduating, Fisher spent a further year at Cambridge studying postgraduate level physics, including the theory of errors, a topic which heightened his interest in statistics. https://www.famousscientists.or/ronald-fisher/

He has been described as "a genius who almost single-handedly created the foundations for modern statistical science" and "the single most important figure in 20th century statistics". In genetics, his work used mathematics to combine Mendelian genetics and natural selection; this contributed to the revival of Darwinism in the early 20th-century revision of the theory of evolution known as the modern synthesis. For his contributions to biology, Fisher has been called "the greatest of Darwin’s successors".
From 1919 onward, he worked at the Rothamsted Experimental Station for 14 years;  here, he analysed its immense data from crop experiments since the 1840s, and developed the analysis of variance (ANOVA). He established his reputation there in the following years as a biostatistician. https://en.wikipedia.org/wiki/Ronald_Fisher

Iris Data Set

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.
The data set consists of 50 samples from each of three species of Iris as:
Iris setosa (also known as bristle-pointed iris), is a species in the genus Iris, it is also in the subgenus of Limniris and in the Iris series Tripetalae.
Iris virginica, with the common name Virginia iris, is a perennial species of flowering plant, native to eastern North America.
Iris versicolor is also commonly known as the blue flag, harlequin blueflag, larger blue flag, northern blue flag, and poison flag, plus other variations of these names, and in Britain and Ireland as purple iris. 
Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.
https://en.wikipedia.org/wiki/Iris_flower_data_set
http://www.lac.inpe.br/~rafael.santos/Docs/R/CAP394?WholeStory-Iris.html

fig iris_dataset

Description

In order to complete my work, some programs and their libraries were used. Below is described a little of each of them. If you need more information click on the link. You can go deep into them and even lower them.

  Python
Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together.
https://www.python.org/doc/essays/blurb/
	
  Matplotlib
Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.
https://matplotlib.org/
	
  Pandas
pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.
pandas is a NumFOCUS sponsored project. This will help ensure the success of development of pandas as a world-class open-source project, and makes it possible to donate to the project.
https://pandas.pydata.org/

  Numpy
NumPy is the fundamental package for scientific computing with Python. It contains among other things:
o	a powerful N-dimensional array object
o	sophisticated (broadcasting) functions
o	tools for integrating C/C++ and Fortran code
o	useful linear algebra, Fourier transform, and random number capabilities
Besides its obvious scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. 
https://www.numpy.org/

  Seaborn
Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
https://seaborn.pydata.org/

  Scikit-learn (formerly scikits.learn)
Is a free software machine learning library for the Python programming language. It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.
https://en.wikipedia.org/wiki/Scikit-learn
https://scikit-learn.org/stable/

  cmder
Cmder is a software package created out of pure frustration over the absence of nice console emulators on Windows. It is based on amazing software, and spiced up with the Monokai color scheme and a custom prompt layout, looking sexy from the start.
https://cmder.net/

  Visual Studio Code – VSCode
Visual Studio Code is a source-code editor developed by Microsoft for Windows, Linux and macOS. It includes support for debugging, embedded Git control, syntax highlighting, intelligent code completion, snippets, and code refactoring.
https://en.wikipedia.org/wiki/Visual_Studio_Code
https://code.visualstudio.com/

  K-nearest neighbors algorithm - KNN
In pattern recognition, the k-nearest neighbors algorithm (k-NN) is a non-parametric method used for classification and regression. In both cases, the input consists of the k closest training examples in the feature space.
https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm

  Jupyter Notebook
The Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.
https://jupyter.org/

  CSV File
Data set “iris” 
https://gist.github.com/curran/a08a1080b88344b0c8a7


Data Analyse

First of all, I need to download the CSV File and save it in my computer. I save it as the same name of reference.
fig Data_analyse

Open the CSV File in Python.
fig open_file and open_file2

Getting information about the data:

iris_1 – This program shows the number of samples, features and species.
fig iris_1

iris_2 – Four features were measured from each sample in centimeters.
fig iris_2

iris_3 – Describe the Iris Data Set statistic as features, samples, mean, minimum, maximum and values between the minimum and maximum.
fig iris_3

iris_4 – This program shows the shape.
fig iris_4

iris_5 – Then I display the keys - or columns - present in the file.
fig iris_5

iris_6 – Characteristics of Data Set
fig iris_6

iris-7 – Species
fig iris_7

iris_8 – Graphics of each species by the number of samples vs its size.
fig iris_8

iris_9 – The best way to inspect the data is to visualize it. To do this, we will use the Matplotlib library to generate a scatter plot. This will allow us to verify that the measurement data of the petals and sepals are well distributed.
As we can see in the chart, the data seems to be very well distributed. This will allow a greater accuracy of the model, since the information is very varied for each type of Iris. Imagine, for example, if the flowers of the Setosa species had the same measurements as the Versicolor. This would make it difficult for our model to predict new flowers inserted later.
fig iris_9

iris_10 – A violin plot plays a similar role as a box and whisker plot. It shows the distribution of quantitative data across several levels of one (or more) categorical variables such that those distributions can be compared.
fig iris_10 - species vs sepal_length
fig iris_11 - species vs sepal_wdth
fig iris_12 - species vs petal_length
fig iris_13 - species vs petal_width

 	 
Conclusion

This project was very challenging to gather subjects focused on my training of Biologist, inspired by Fisher with the data collection of flowers and my new goal in Hight Diploma in Data Analytics, creating a computational environment for visualization and analysis of the data.The data search for this project was great and very learning. It is surprising how the database was created and even more intriguing as Fisher can describe this with formulas.
I collected the suggested database in class on the GitHub site and began to manipulate the data to know the number of species, characteristics, keywords and total samples. And finally print graphs related to the study that caught my attention.
My project is available in GitHub and in annex follows the programs used for my manipulation of the data.


References

https://www.famousscientists.or/ronald-fisher/
https://en.wikipedia.org/wiki/Ronald_Fisher
https://cmder.net/
https://www.python.org/doc/essays/blurb/
http://www.lac.inpe.br/~rafael.santos/Docs/R/CAP394?WholeStory-Iris.html
https://en.wikipedia.org/wiki/Visual_Studio_Code
https://code.visualstudio.com/
https://en.wikipedia.org/wiki/Iris_flower_data_set
https://seaborn.pydata.org/
https://www.python.org/doc/essays/blurb/
https://www.numpy.org/
https://pandas.pydata.org/
https://matplotlib.org/
https://en.wikipedia.org/wiki/Scikit-learn
https://scikit-learn.org/stable/
https://matplotlib.org/
https://gist.github.com/curran/a08a1080b88344b0c8a7
https://paulovasconcellos.com.br/como-criar-seu-primeiro-aplicativo-de-machine-learning-7b6af291ba11
https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset
https://seaborn.pydata.org/generated/seaborn.violinplot.html?highlight=violinplots%20observations
https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm
https://jupyter.org/
