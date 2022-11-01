import pandas as pd

"""
This file contains a function that reads the data in txt form 
outputted from the FTIR machine and transforms it into a df 
panda dataframe
"""

def importtxt(
    path  
):
    """
    importtxt = importing and processing a txt file
    ARGS:
        path:   str, relative path string to file we want to import
    RETURS:
        df:     DataFrame, dataframe contains transmittance and the 
                        index is the wavelength in nm 
    """
    # Pre-allocate memory for list
    column_name =  ['nm','t']
    # Import the df using pd.read_csv
    df =  pd.read_csv(path, delimiter = "\t0" , header = None)
    # Rename the columns 
    df.columns = column_name
    # Convert from cm-1 to nm
    # TODO check this it is wrong cuttof should be around 2000nm
    # Set the index 
    df = df.set_index('nm') 
    
    return df




