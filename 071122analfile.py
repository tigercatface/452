from functions.processor import processor
from plotter import plottter

s_path_list = [
    'InGaAsSb071122\InGaAsSb_XAB1308_071122_backroundall_64.0.txt',
    'InGaAsSb071122\InGaAsSb_XAB1309_071122_backroundall_64.0.txt',
    'InGaAsSb071122\InGaAsSb_XAB1315_071122_backroundall_64.0.txt',
     'InGaAsSb071122\InGaAsSb_XK1786_071122_backroundall_64.0.txt',
     'InGaAsSb071122\InGaAsSb_XK1787_071122_backroundall_64.0.txt'
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
control_path = 'InGaAsSb071122\GaAs_undoped_071122_backroundall_64.0.txt'
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
    '07-11-22',
    9,
    1)
plottter(
    control_path,
    s_path_list,
    s_name_list,    
    thickness_list,
    control_name,
    '071122 Raw data'
    )