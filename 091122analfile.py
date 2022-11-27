from functions.processor import alphaplot
from functions.bandgapcalculator import Egplotter
from functions.linearfit import linearfit
from matplotlib import pyplot as plt
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


# s_name_list = [
#     'XAB1308',
#     'XAB1309',
#     'XAB1315',
#     'XK1786',
#     'XK1787'
# ]

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
thickness_list = [
    1000,
    1000,
    1000,
    1000,
    1000
]
control_path = 'data\InGaAsSb091122_2\GaAs_un_091122_64.1.txt'
control_thickness = 350000
control_name = 'GaAs Control'
plt_title = 'TITLE'

sample_limits = {
    'XAB1308':[0.5,0.7],
    'XAB1309':[0.55,0.7],
    'XAB1315':[0.450, 0.575],
    'XK1786':[0.575, 0.750],
    'XK1787':[0.650, 0.750],
}

df = alphaplot(
    control_path,
    s_path_list,
    s_name_list,
    thickness_list,
    control_thickness,
    control_name,
    '09-11-22 Attempt 2',
    5,
    1, 
    True,
    1)
    
Egplotter(df,
        control_name,
        s_name_list,
        1,    
        'EGG',
        'Energy (eV)',
        'eV'
        )

# TODO need to use different list, no idea why. 

sampleregression, sampledfs = linearfit(
    df,
    s_name_list_2,
    sample_limits
)
plt.show()

