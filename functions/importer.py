from pylab import *
from matplotlib import pyplot as plt 
import numpy as np 
import pandas as pd 

"""
TODO:
    1. Import 
    2. Clean 
    3. Return dicts of cleaned and non cleaned

"""

def importer(
    sample_names, 
    sample_dates, 
    substrate_path, 
    substrate_name,
    rate,
    sam_thick 
):
    """
    Args:   
    
        sample_names,   list, sample names 
        sample_dates,   str, date + extra information
        substrate_path, str, path of the substrate
        substrate_name, str, name and index of substrate
    Returs:
        un_df;          pandas.Dataframe, raw imported transmission
        cl_df;          pandas.Dataframe, normalized imported transmission data 
    """
    # Create empty dataframes to store our data,  
    un_df = pd.DataFrame()
    cl_df = pd.DataFrame()
    al_df = pd.DataFrame()

    # Assume the data is in micrometers, 
    # Import  the sbstrate values using pylance, 
    sub_um, sub_t = loadtxt(substrate_path, unpack = True)
    un_df[substrate_name] = sub_t
    # Conversion from um to ev, 
    h = 4.1357e-15 #eV s
    c = 299792458 # ms-1
    sub_ev = [h * c/(m * 1e-6) for m in sub_um]
    un_df['eV'] = sub_ev
    cl_df['eV'] = sub_ev
    al_df['eV'] = sub_ev
    for name in sample_names:
        # Clear memory of previous lists, 
        sam_um = []
        sam_t = []
        alpha = []
        # Loop over all items in sample names dict,
        # Assuming the same convemtion has beenm used for 
        # All the str of data then we guccy!!!
        # DUMMY str: 'data\InGaAsSb091122_2\InGaAsSb_XAB1308_091122_64.0.txt',
        folder = 'data/'
        subfoler = 'InGaAsSb' + sample_dates + '/'
        file = 'InGaAsSb_' + name + '_'  + sample_dates + '_' + rate + '.txt'
        path  = folder + subfoler + file
        # Import Data
        sam_um, sam_t = loadtxt(path, unpack = True)
        print(path)
        print(sam_t)
        #Manual fix for rough side
        tarnishlist = ['XAB1308',
                        'XK1787',
                        'XK1786']
        if name in tarnishlist:
            sam_t = sam_t * 10
            print(name, ' Timesed by 10 to account for tarnishing')
        # Data to df 
        un_df[name] = sam_t
        # Clean Data, 
        sam_norm_t = [m/n for m,n in zip(sam_t, sub_t)]
        # Append to Cleaned DF
        cl_df[name] = sam_norm_t

        # We now calculate the absorption coefficient, 
        alpha = - np.log(sam_norm_t) / (sam_thick * 1e-7)
        al_df[name] = alpha
        
        
        
    # EXIT 
    # Switch dfs to ev: 
    un_df = un_df.set_index('eV')
    cl_df = cl_df.set_index('eV')
    al_df = al_df.set_index('eV') 


    return un_df, cl_df, al_df





