from functions.processor import alphaplot
from functions.bandgapcalculator import Egplotter
from functions.linearfit import linearfit
from functions.bowing_plot import bowing_plotter 
from functions.linearfitfurther import linearfit as coolinearfit
import numpy as np 
from matplotlib import pyplot as plt
import matplotlib
#matplotlib.rcParams.update(matplotlib.rcParamsDefault)


# Control /  block comment
# s_path_list = [
#     'data\InGaAsSb091122_2\InGaAsSb_XAB1308_091122_64.0.txt',
#     'data\InGaAsSb091122_2\InGaAsSb_XAB1309_091122_64.0.txt',
#     'data\InGaAsSb091122_2\InGaAsSb_XAB1315_091122_64.0.txt',
#      'data\InGaAsSb091122_2\InGaAsSb_XK1786_091122_64.0.txt',
#      'data\InGaAsSb091122_2\InGaAsSb_XK1787_091122_64.0.txt'
# ]
s_path_list = [
    'data\InGaAsSb091122_2\InGaAsSb_XAB1308_091122_64.0.txt',
    'data\InGaAsSb091122_2\InGaAsSb_XK1786_091122_64.0.txt',
    'data\InGaAsSb091122_2\InGaAsSb_XK1787_091122_64.0.txt',
    'data\InGaAsSb091122_2\InGaAsSb_XAB1309_091122_64.0.txt',
    'data\InGaAsSb091122_2\InGaAsSb_XAB1315_091122_64.0.txt'
]


s_name_list = [
    'XAB1308',
    'XK1786',
    'XK1787',
    'XAB1309',
    'XAB1315'
]
s_name_list_2 = [
    'XAB1308',
    'XK1786',
    'XK1787',
    'XAB1309',
    'XAB1315'
]
# UNCERTAINTY in this 

thickness_list = [
    1000,
    1000,
    1000,
    1000,
    1000
]
alloy_frac = {
    "XAB1308":0.20,
    "XK1786":0.1,
    "XK1787":0.05,
    "XAB1309":0.14,
    "XAB1315":0.25
}


control_path = 'data\InGaAsSb091122_2\GaAs_un_091122_64.1.txt'
control_thickness = 350000
control_name = 'GaAs Control'
plt_title = 'TITLE'

# NOTE these are in eV
sample_limits = {
    'XAB1308':[0.501,0.5237],
    'XAB1309':[0.57,0.589],
    'XAB1315':[0.48, 0.506],
    'XK1786':[0.585, 0.611],
    'XK1787':[0.65, 0.678],
}
# [[GoodLimit],[Upperlimit],[Lowerlimit]]
sample_extended_limits = {   
    'XAB1308':[[0.51,0.52],[0.515,0.52],[0.51,0.53]],
    'XAB1309':[[0.57, 0.585],[0.570,0.585],[0.570,0.59] ],
    'XAB1315':[[0.48, 0.506],[0.48,0.49],[0.48,0.51]],
    'XK1786':[[0.585, 0.600],[0.585,0.600],[0.585,0.610]],
    'XK1787':[[0.65, 0.66],[0.65, 0.66],[0.65,0.7]],
}

df = alphaplot(
    control_path,
    s_path_list,
    s_name_list,
    thickness_list,
    control_thickness,
    control_name,
    '09-11-22 Transmission Raw Data',
    5,
    1, 
    True,
    1)

#Egplotter(df,
 #       control_name,
  #      s_name_list,
   #     1,    
    #    'EGG',
     #   'Energy (eV)',
      #  'eV'
       # )

# TODO need to use different list, no idea why. 
# TODO df does not have eV in the index yet so if you square it the emnergy is too large
# NOTE the size issue was when we squared the coefficient, python wanted to do an np.arange
# that was too big for storage, 1e14 values ish     
df = df.set_index('energy')
df2 = df.copy()
sampleregression, sampledfs, e_list = linearfit(
    df,
    s_name_list_2,
    sample_limits
)
print(e_list)


e_err = coolinearfit(df2, s_name_list_2, sample_extended_limits)

bowing_plotter(
    e_list, 
    e_err,
    alloy_frac,
    s_name_list)

plt.show()  