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
    Thisn function imports the processed dataframe and calculates the band gap energies
    of the samples , 
    it then uses lower and upper bounds to calculate a theoretical bound for the egap
    args:
        dataframe,          DataFram: df of alpha^2 , eV index, 
        sample_name_list,   List: Names of the samples, 
        sample_limits,      Dict: Key: Sample name, value: 
                            [[lowerlim,upperlim],[maximizing ev],[minimizingev]]
    returns:
        sampleregression_dict, Dict, Sample: Regression Fit Results 
        sample_df_dict,     Dict, Sample: DF with limits applied to it
        egap_dict,          Dict, Sample: Egap,Higerbound,Lowerbound
    """
    egap_dict = {}
    sample_df_dict = {}
    sampleregression_dict = {}
    #dataframe = dataframe.set_index('energy')
    dataframe = np.square(dataframe)
    
    # Initialize the return dict 
    e_error = {}
    for sample in sample_name_list:
        y1 = 0 # Fit
        y2 = 0 # Upper
        y3 = 0 # Lower
        x1 = 0 # Fit 
        x2 = 0 # Upper
        x3 = 0 # Lower
        # Create and empty the dataframes:
        df1 = pd.DataFrame()
        df2 = pd.DataFrame()
        df3 = pd.DataFrame()
        df4 = pd.DataFrame() # Used to plot more of the absorption Coeff
        # Load the Dataframes
        df1 = dataframe[[sample]].copy()
        df2 = dataframe[[sample]].copy()
        df3 = dataframe[[sample]].copy()
        df4 = dataframe[[sample]].copy()
        # Limit the dataframes
        df1 = df1[df1.index <
            sample_limits[sample][0][1]]
        df1 = df1[df1.index >
            sample_limits[sample][0][0]]
        df2 = df2[df2.index <
            sample_limits[sample][1][1]]
        df2 = df2[df2.index >
            sample_limits[sample][1][0]]
        df3 = df3[df3.index <
            sample_limits[sample][2][1]]
        df3 = df3[df3.index >
            sample_limits[sample][2][0]]
        print(sample_limits[sample][0][0])
        print(sample_limits[sample][0][1])
        # Need to do the fittings for the samples now: 
        y1 = df1[sample].tolist()
        x1 = df1.index.tolist()
        y2 = df2[sample].tolist()
        x2 = df2.index.tolist()
        y3 = df3[sample].tolist()
        x3 = df3.index.tolist()

        model1 = sm.OLS(y1, sm.add_constant(x1))
        model2 = sm.OLS(y2, sm.add_constant(x2))
        model3 = sm.OLS(y3, sm.add_constant(x3))

        results1 = model1.fit()
        results2 = model2.fit()
        results3 = model3.fit()

        fitm1 = results1.params[1]
        fitb1 = results1.params[0]
        fitm2 = results2.params[1]
        fitb2 = results2.params[0]
        fitm3 = results3.params[1]
        fitb3 = results3.params[0]

        egap1 = -fitb1/fitm1
        egap2 = -fitb2/fitm2
        egap3 = -fitb3/fitm3

        # Diff between egaps: 
        egap_errmax = egap2 - egap1
        egap_errmin = egap1 - egap3
        print("Egap is ", egap1,"Range (", egap2," - ",egap3,")" )
        e_error[sample] = [egap_errmax, egap_errmin]

        df4 = df4[df4.index > sample_limits[sample][0][0] - 0.05]
        df4 = df4[df4.index < 0.7]

        # Linear Fit Equation
        lowy = 0 
        highy1 = sample_limits[sample][0][1] * fitm1 + fitb1 + 5e7
        highy2 = sample_limits[sample][1][1] * fitm2 + fitb2 + 5e7
        highy3 = sample_limits[sample][2][1] * fitm3 + fitb3 + 5e7
        
        fit_y1 = np.arange(lowy, highy1, 10)
        fit_y2 = np.arange(lowy, highy2, 10)
        fit_y3 = np.arange(lowy, highy3, 10)

        fit_x1 = (fit_y1 - fitb1)/fitm1
        fit_x2 = (fit_y2 - fitb2)/fitm2
        fit_x3 = (fit_y3 - fitb3)/fitm3

        y1 =  df4[sample].tolist()
        x1 = df4.index.tolist()

        plt.figure(6)
        plt.plot(x1,y1, label = sample)
        plt.plot(fit_x1, fit_y1, label = '')
        plt.plot(fit_x2, fit_y2, label = '')
        plt.plot(fit_x3, fit_y3, label = '')
        plt.title('Absorption Coefficient Squared Linear Fit')
        plt.xlabel('Energy (eV)')
        plt.ylabel('Absorption Coefficient Squared')
        plt.legend()
    return (e_error)

