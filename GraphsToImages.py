
# coding: utf-8

# In[ ]:


# Function for Univariate Graphs with only the given suggestions
def Graphs_univariate(df, var=[], direc=r''):
    #Importing required packages
    import pandas as pd
    import matplotlib.pyplot as plt
    from pandas.plotting import scatter_matrix
    import seaborn as sns

    x=df._get_numeric_data().columns   #List of numerical variables in dataframe
    
    if direc != r'': #If directory is given, we need to append one more slash to land into the folder for saving graphs.
        direc=direc+ "\\"
    
    if var: # If any column indexes are given
        for item in var:
            z = df.iloc[:,[item]].columns  # fetching column name via index
            column = z[0]
            if column in x: # If column is numerical
                plt.figure()
                #Boxplot
                df.boxplot([column],rot = 0,notch=False,grid=False,vert=False)
                plt.xlabel(column.capitalize(),fontsize=10)
                plt.title("Boxplot of "+column,fontsize=14)
                plt.savefig(direc+column.capitalize()+'_Boxplot.png')
                #Histogram
                df.hist([column],grid=False)
                plt.xlabel(column.capitalize(),fontsize=10)
                plt.ylabel('Frequency of '+column,fontsize=10)
                plt.title("Histogram of "+column,fontsize=14)
                plt.savefig(direc+column.capitalize()+'_Hist.png')
            else: # If column is categorical
                #Barplot
                df[column].value_counts().plot(kind='bar',fontsize=10)
                plt.xlabel(column.capitalize(),fontsize=10)
                plt.ylabel('Frequency of '+column,fontsize=10)
                plt.title("Barplot of "+column,fontsize=14)
                plt.savefig(direc+column.capitalize()+'_BarChart.png')

    else:
        for column in df:
            if column in x:
                plt.figure()
                #Boxplot
                df.boxplot([column],rot = 0,notch=False,grid=False,vert=False)
                plt.xlabel(column.capitalize(),fontsize=10)
                plt.title("Boxplot of "+column,fontsize=14)
                plt.savefig(direc+column.capitalize()+'_Boxplot.png')
                #Histogram
                df.hist([column], grid=False)
                plt.xlabel(column.capitalize(),fontsize=10)
                plt.ylabel('Frequency of '+column,fontsize=10)
                plt.title("Histogram of "+column,fontsize=14)
                plt.savefig(direc+column.capitalize()+'_Hist.png')

            else:
                #Barplot
                df[column].value_counts().plot(kind='bar',fontsize=10)
                plt.xlabel(column.capitalize(),fontsize=10)
                plt.ylabel('Frequency of '+column,fontsize=10)
                plt.title("Barplot of "+column,fontsize=14)
                plt.savefig(direc+column.capitalize()+'_BarChart.png')


# In[ ]:


# Function for Univariate and Bivariate Graphs with the given suggestions as well as improved suggestios
# Improved suggestions like asking the user for Figure size, color and edge colors as inputs for all the graphs.
# Also, if 
def Graphs(df,target_y='', var=[], direc=r'',figsize = (12,8),color = 'blue', edgecolor = 'black'):
    #Importing required packages
    import pandas as pd
    import matplotlib.pyplot as plt
    from pandas.plotting import scatter_matrix
    import seaborn as sns
    
    x=df._get_numeric_data().columns  #List of numerical variables in dataframe
    
    if direc != r'': #If directory is given, we need to append one more slash to land into the folder for saving graphs.
        direc=direc+ "\\"

    #If target variable y is not given input argument, this function is meant for Univariate analysis:
    if not(target_y):
        if var: # If any column indexes are given
            for item in var:
                z = df.iloc[:,[item]].columns  # fetching column name via index
                column = z[0]
                
                if column in x: # If column is numerical
                    plt.figure()
                    #Boxplot
                    df.boxplot([column],rot = 0,figsize=figsize,notch=False,grid=False,vert=False)
                    plt.xlabel(column.capitalize(),fontsize=10)
                    plt.title("Boxplot of "+column,fontsize=14)                     
                    plt.savefig(direc+column.capitalize()+'_Boxplot.png')                    
                    #Histogram
                    df.hist([column],figsize=figsize,grid=False,color = color, edgecolor=edgecolor)
                    plt.xlabel(column.capitalize(),fontsize=10)
                    plt.ylabel('Frequency of '+column,fontsize=10)
                    plt.title("Histogram of "+column,fontsize=14)
                    plt.savefig(direc+column.capitalize()+'_Hist.png')
                else: # If column is categorical
                    #Barplot
                    df[column].value_counts().plot(kind='bar',color=color,fontsize=10, figsize = figsize,edgecolor=edgecolor)
                    plt.xlabel(column.capitalize(),fontsize=10)
                    plt.ylabel('Frequency of '+column,fontsize=10)
                    plt.title("Barplot of "+column,fontsize=14)                     
                    plt.savefig(direc+column.capitalize()+'_BarChart.png')

        else: # If no variable indexes are given, save graphs of all
            for column in df:
                if column in x:
                    plt.figure()
                    #Boxplot
                    df.boxplot([column],rot = 0,figsize=figsize,notch=False,grid=False,vert=False)
                    plt.xlabel(column.capitalize(),fontsize=10)
                    plt.title("Boxplot of "+column,fontsize=14)                     
                    plt.savefig(direc+column.capitalize()+'_Boxplot.png')
                    #Histogram
                    df.hist([column],figsize=figsize, grid=False, color=color, edgecolor=edgecolor)
                    plt.xlabel(column.capitalize(),fontsize=10)
                    plt.ylabel('Frequency of '+column,fontsize=10)
                    plt.title("Histogram of "+column,fontsize=14)                     
                    plt.savefig(direc+column.capitalize()+'_Hist.png')

                else:
                    #Barplot
                    df[column].value_counts().plot(kind='bar',color=color,fontsize=10, figsize = figsize,edgecolor=edgecolor)
                    plt.xlabel(column.capitalize(),fontsize=10)
                    plt.ylabel('Frequency of '+column,fontsize=10)
                    plt.title("Barplot of "+column,fontsize=14)                     
                    plt.savefig(direc+column.capitalize()+'_BarChart.png')
    
    #If target variable y is given as attribute name as string into input  
    else:
        for column in df:
            if target_y!=column:
                if target_y in x:
                    if column in x:
                        #scatter plot for Y numerical and X numerical
                        df.plot(x = column, y = target_y, kind = 'scatter')
                        plt.title("Scatter Plot of %s and %s" %(column, target_y))                         
                        plt.savefig(direc+column+"_and_"+target_y+"_Scatter_Plot.png")
                    else:
                        #Boxplot for Y numerical and X Categorical
                        sns_plot1 = sns.boxplot(data=df, x=column, y = target_y).set_title('Box Plot of %s and %s' %(column, target_y), weight = 'bold')
                        sns_plot1.figure.savefig(direc+column+"_and_"+target_y+"_Box_Plot.png")
                else:
                    if column in x:
                        #Boxplot for Y categorical and X numerical
                        sns_plot1 = sns.boxplot(data=df, x=column, y = target_y).set_title('Box Plot of %s and %s' %(column, target_y), weight = 'bold')
                        sns_plot1.figure.savefig(direc+column+"_and_"+target_y+"_Box_Plot.png")
                    else:
                        #No graphs for both x and y are categorical
                        pass

