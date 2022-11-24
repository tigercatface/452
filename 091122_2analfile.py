from functions.processor import processor
from plotter import plottter

s_path_list = [
    'XAB1315T\GaAs_111122_T_77_64.0..txt',
    'XAB1315T\GaAs_111122_T_90_64.0..txt',
    'XAB1315T\GaAs_111122_T_100_64.0..txt',
    'XAB1315T\GaAs_111122_T_120_64.0..txt',
    'XAB1315T\GaAs_111122_T_140_64.0..txt',
    'XAB1315T\GaAs_111122_T_160_64.0..txt',
    'XAB1315T\GaAs_111122_T_180_64.0..txt',
    'XAB1315T\GaAs_111122_T_200_64.0..txt',
]
s_name_list = [
    '77',
    '90',
    '100',
    '120',
    '140',
    '160',
    '180',
    '200'
]
thickness_list = [
    1000,
    1000,
    1000,
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
df1 = processor(
    control_path,
    s_path_list,
    s_name_list,
    thickness_list,
    control_thickness,
    control_name,
    '09-11-22 Attempt 2',
    9,
    1)

print(df1
)
plottter(
    control_path,
    s_path_list,
    s_name_list,    
    thickness_list,
    control_thickness,
    control_name,
    )