from processor2electricboogietowntime import processor
from plotter import plottter

s_path_list = [
    'InGaAsSb091122\InGaAsSb_XAB1308_091122_64.0.txt',
    'InGaAsSb091122\InGaAsSb_XAB1309_091122_64.0.txt',
    'InGaAsSb091122\InGaAsSb_XAB1315_091122_64.0.txt',
     'InGaAsSb091122\InGaAsSb_XK1786_091122_64.0.txt',
     'InGaAsSb091122\InGaAsSb_XK1787_091122_64.0.txt'
]
s_name_list = [
    'XAB1308',
    'XAB1309',
    'XAB1315',
    'XK1786',
    'XK1787'
]
thickness_list = [
    1000,
    1000,
    1000,
    1000,
    1000
]
control_path = 'InGaAsSb091122\GaAs_un_091122_64.1.txt'
control_thickness = 350000
control_name = 'GaAs Control'
plt_title = 'TITLE'
processor(
    control_path,
    s_path_list,
    s_name_list,
    thickness_list,
    control_thickness,
    control_name,
    '09-11-22 Attempt 2',
    9,
    1)
plottter(
    control_path,
    s_path_list,
    s_name_list,    
    thickness_list,
    control_thickness,
    control_name,
    )