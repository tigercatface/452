import pandas as pd 
import numpy as np 
import statsmodels.api as sm 
from matplotlib import pyplot as plt 

def linearfit(
    dataframe, 
    sample_name_list, 
    sample_limits,
):  
    """
    args:
        dataframe,          DataFram: df of alpha^2 , eV index, 
        sample_name_list,   List: Names of the samples, 
        sample_limits,      Dict: Key: Sample name, value: [lowerlim,upperlim]
    returns:
        sampleregression_dict, Dict, Sample: Regression Fit Results 
        sample_df_dict,     Dict, Sample: DF with limits applied to it
    """
    sample_df_dict = {}
    sampleregression_dict = {}
    dataframe = dataframe.set_index('energy')
    for sample in sample_name_list:
        df = pd.DataFrame() # Empty the dataframe,
        y = 0
        x = 0
        lowlim = 0
        upplim = 0
        lowlim = sample_limits[sample][0] # 1st element of list, 
        upplim = sample_limits[sample][1] # 2nd element of list, 
        # Only select sample dataframe, 
        df = dataframe[[sample]].copy()
        # New special limits
        df = df[df.index > lowlim]
        df = df[df.index < upplim]
        # Dict of Dataframes, 
        sample_df_dict[sample] = df
        # Perform our linear regression, 
        
        y = df[sample].tolist()
        x = df.index.tolist()
        model = sm.OLS(y, sm.add_constant(x))
        results = model.fit()
        sampleregression_dict[sample] = results.summary()
        plt.figure(4)
        plt.plot(x,y, label = sample)
        fit_m = results.params[1]
        fit_b = results.params[0]
        # TODO, find a way to make is go from x = 0, 
        # np.arrange for fit y using lower and upper limits
        # using equation for y = mx + b
        lowy = 0
        highy = upplim * fit_m + fit_b
        fit_y = np.arange(lowy, highy, 0.01)
        fit_x = (fit_y - fit_b)/ fit_m

        plt.plot(fit_x,fit_y, label = sample + " FIT")
        plt.legend()
        plt.title('Absorption Coefficient Squared Linear Fit')
        plt.xlabel('Energy (eV)')
        plt.ylabel('Absorption Coefficient Squared')
    return sampleregression_dict, sample_df_dict






