# <p align="center"> PANDS Project - Analysis of Fischer's Iris Data Set using Python
# <p align="center"> Author: D. Redmond
    
    
    
    
**<p align="center"> Data Set Summary**
  
The Iris flower data set or Fisher’s Iris data set is one of the most famous multivariate data sets. It was introduced by the British statistician and biologist Ronald Fisher in his 1936 paper 'The use of multiple measurements in taxonomic problems' as an example of linear discriminant analysis. The data set consists of 50 samples from three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals, and the length and width of the petals. 
  
**<p align="center"> Project Tasks**
  
1. Research the data set online and write a summary about it in README.
2. Download the data set and add it to your repository.
3. Write a program called analysis.py that:
            3.1. outputs a summary of each variable to a single text file,
            3.2. saves a histogram of each variable to png files,
            3.3. outputs a scatter plot of each pair of variables, and
            3.4. performs other appropriate analysis.
  
**<p align="center"> Investigations**
  
Having downloaded the dataset and importing it into Python, I then import pandas, nimpy, seaborn, and matplotlib libraries to aid in analyzing the dataset. I convert the dataset into a csv format and assign relevant headings for the species columns. I organise the data by checking for duplicates, and removing empty cells. 
    
Task 1 involved outpitting a summary of each variable to a single text file titled irisSummary.txt. I do this by using value_counts and describe methods to find descriptive statistics of each column. I then use the corr function to find pairwise correlation of the columns. The data results of these three methods are retrieved with the loc function, and then output to the text file. 
    
Task 2 involved saving a histogram of each variable to png files. I began this task by using the facet grid class and histplot functions to map and plot the data. This illustrated distribution patterns in the data. I added a legend to distinguish the results by their species. 
    
Task 3 involced outputting a scatter plot of each pair of variables. To do this I used the scatterplot function to create and map a scatter plot for each of the three species in the dataset. I added a simple legend and labelled the columns appropriately. I also made use of the matplotlib pyplot module to clear the current data with the clf method. Finally I repeated the process for the petal columns.
  
**<p align="center"> Python Libraries Used**
  
Pandas - The pandas library is a useful package for importing labelled data such as the iris data set.
    
NumPy - The NumPy package is useful as a container for multidimensional data which makes NumPy arrays easier to work with, manipulate and analyse.
    
eaborn - Seaborn is a Python visualization library that provides a high-level interface for drawinge statistical graphics.
    
Matplotlib - The Matplotlib python library is used to make charts such as histograms, plots and bar charts.
  
**<p align="center"> Summary of Repository**
  
    analysis.py
    
    histogram_PL.png

    histogram_PW.png

    histogram_SL.png

    histogram_SW.png

    iris.data

    irisSummary.txt

    README.md

**<p align="center"> References**

https://en.wikipedia.org/wiki/Iris_flower_data_set
  
https://archive.ics.uci.edu/ml/datasets/iris
  
https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
  
https://www.geeksforgeeks.org/matplotlib-tutorial/
  
https://www.geeksforgeeks.org/python-seaborn-tutorial/
  
https://www.geeksforgeeks.org/matplotlib-pyplot-clf-in-python/
  
https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/
  
https://www.angela1c.com/projects/iris_project/investigating-the-iris-dataset/
  
https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d

