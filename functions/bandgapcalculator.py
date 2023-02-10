import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
def Egplotter(
    dataframe, 
    control_name, 
    sample_name, 
    upperlimit, 
    lowerlimit,
    title,
    xlabel

):  
    """
    Pepegasm
    """
    # TODO:
    # Transfer stuff to energy, 
    df = dataframe.set_index('energy')
    
    # Cull the values we are not interested in
    # df = dataframe[dataframe.index > lowerlimit]
    # df = df[df.index < upperlimit]
    # Energy values to list
    energy = df.index.tolist()
    # Square all the values in the dataframe 
    df = np.square(df)


    # Create a list of all names and then loop over elements in list 
    sample_name.append(control_name)
    # WE are using many figures
    plt.figure(3)
    for name in sample_name: 
        alpha =  df[name].values.tolist()
        plt.plot(energy, alpha, label  = name)
    
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel('alpha^2')
    plt.legend()
    # Return list to its orignal State
    sample_name = sample_name[:-1]
    return df

