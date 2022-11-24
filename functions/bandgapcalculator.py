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
    print(df)
    # Energy values to list
    energy = df.index.tolist()
    # Square all the values in the dataframe 
    df = np.square(df)
    print(df)

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
    plt.show()
    return df

