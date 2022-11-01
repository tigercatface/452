import pandas as pd 
import numpy as np 
from importing import importtxt

def transmittancetoabsorbtioncoeff(
    control,
    sample,
    thickness
    ):
    """
    ARGS: 
        control:    str; relative path of substrate layer it is built on
        sample:     str; relative path of sample data 
        thickness:  str; thickness of the substrate in nm 
    RETURNS: 
        test_df;    DataFrame; processed data!
    """

    # Import both dataframes
    control_df = importtxt(
        control
    )
    sample_df = importtxt(
        sample
    )
    # Divide sample / control to obtain a better spectrum
    test_df =  sample_df/control_df
    # Convertion from nm to cm 
    thicknesscm = thickness * 1e-7

    # I = I_0exp(-alpha*thicknesscm) 
    # -ln(I/I_0)/thicknesscm = alpha
    test_df['alpha'] = -np.log(test_df['t']) / thicknesscm

    
    return test_df






