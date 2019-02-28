# Python-Interactive-package-for-exploratory-data-analysis

Problem Statement: To develop a package in Python which will do the EDA of any dataset.

Approach: Created functions inside the package named "GraphsToImages.py" (a local package) to identify categorical
and numerical variables, plot visualization graphs for each of the
variables, identify and provide suggestions for outlier treatment and
missing value imputation method to the user.

Here, there are 2 functions in side this package:
1. Graphs_univariate:
 - This one does the univariate analysis for each of the variables/attributes. 
 - If it is numerical, it will plot box plot and histogram.  If it is categorical, it will plot barplot. 
 - The directory in which the graphs need to be exported and saved as image can also be given by user, otherwise it will be stored in the same working diretory.

2. Graphs:
 - This one does the bi-variate analysis between target variable and other independent variables.
 - 

