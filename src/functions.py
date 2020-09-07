import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def ratio(data,columna,categoria):
    """This function is used to calculate a ratio based in three parameters data frame, column and the attribute of the column, the columna and categoria parameters should be a string"""
    a=data[data[columna]==categoria]
    b=data[columna]

    p1=len(a)
    p2=len(b)
    ratio=(p1/p2)*100
    return ratio


def group(data, columna1, columna2):
    """Simple group by function, that received three parameters dataframe and two columns"""
    gp=data.groupby(columna1)[columna2]
    return gp



def ccountplot (column,data,title=' ', pal="Set2"):
    """Create a seaborn count plot, 4 parameters, colum, dataframe, title of the plot (optional) and palette set (optional, default 2)"""
    ax = sns.countplot(x=column, data=data, palette=pal)
    plt.title(title)
    plt.show()