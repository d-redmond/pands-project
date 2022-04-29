# GMIT PANDS 2022 Project
# Purpose: Analyze Fischer's Iris Data Set using Python

# iris.csv downloaded from https://datahub.io/machine-learning/iris
# iris.data downloaded from https://archive.ics.uci.edu/ml/datasets/iris

# Author: Denise Redmond                                   

# Importing Pandas, Numpy, Matplotlib, and Seaborn libraries 

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

# Assgning headings to columns
# Using open function, data converted csv format

filename = 'iris.data' 
columns = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Species'] 
with open (filename, "r") as f: 
    iris = pd.read_csv(filename, sep= ',', header=None, names=columns)

# Task 1: Outputing a summary of each variable to a single text file irisSummary.txt

    print("Summary Iris Dat Set", file=open("irisSummary.txt", "w"))
    print(" ", file=open("irisSummary.txt", "a"))
    print("Number of Samples available for each type: ", file=open("irisSummary.txt", "a"))
    print(" ", file=open("irisSummary.txt", "a"))

# Using value_counts and describe methods to find descriptive statistics of each column
# Using corr function to find pairwise correlation of columns
# Results output to irisSummary.txt  

    print(iris['Species'].value_counts(), file=open("irisSummary.txt", "a"))
    print(' ', file=open("irisSummary.txt", "a"))
    print(iris.describe, file=open("irisSummary.txt", "a"))
    print (' ', file=open("irisSummary.txt", "a")) 
    print(iris.groupby("Species").corr(), file=open("irisSummary.txt", "a"))

# Retrieving data values from the relevant locations with the .loc function
# Separating data according to species

iris_setosa = iris.loc[iris["Species"]=="Iris-setosa"] 

iris_virginica = iris.loc[iris["Species"]=="Iris-virginica"]

iris_versicolor = iris.loc[iris["Species"]=="Iris-versicolor"] 

# Task 2: Saving a histogram of each variable to png files

# Using FacetGrid class and histplot function to map and plot the data in order to illustrate distribution patterns
# Adding a simple legend to distinguish results by species
# Defining dpi

sns.FacetGrid(iris,hue="Species",height=6).map(sns.histplot,"Petal Length").add_legend()
plt.savefig('histogram_PL.png', dpi = 300)

sns.FacetGrid(iris,hue="Species",height=6).map(sns.histplot,"Petal Width").add_legend()
plt.savefig('histogram_PW.png', dpi = 300)

sns.FacetGrid(iris,hue="Species",height=6).map(sns.histplot,"Sepal Length").add_legend()
plt.savefig('histogram_SL.png', dpi = 300)

sns.FacetGrid(iris,hue="Species",height=6).map(sns.histplot,"Sepal Width").add_legend()
plt.savefig('histogram_SW.png', dpi = 300)

# Task 3: Outputing a scatter plot of each pair of variables

# Using scatterplot function to create and map scatter plots for each species
# Pulling data from specified species
# Adding legend and labels
# Using .clf to clear the current figure

sns.scatterplot(data = iris_setosa, x = "Sepal Length", y = "Sepal Width", legend = True)

sns.scatterplot(data = iris_virginica, x= "Sepal Length", y = "Sepal Width", legend = True)

sns.scatterplot(data = iris_versicolor, x= "Sepal Length", y = "Sepal Width", legend = True)

plt.legend(labels=["Iris Setosa", "Iris Virginica", "Iris Versicolor"])

plt.show()
plt.clf()

# Same process as above, but drawing data from the petal columns as appropriate

sns.scatterplot(data = iris_setosa, x= "Petal Length", y = "Petal Width", legend = True)

sns.scatterplot(data = iris_virginica, x= "Petal Length", y = "Petal Width", legend = True)

sns.scatterplot(data = iris_versicolor, x= "Petal Length", y = "Petal Width", legend = True)

plt.legend(labels=["Iris Setosa", "Iris Virginica", "Iris Versicolor"])

plt.suptitle("Iris Setosa, Virginica and Versicolour Petal Length/Petal Width")

plt.show()
plt.clf()