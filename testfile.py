from concurrent.futures import process
from processor2electricboogietowntime import processor

sample_path_list = [
    'InGaAsSb251022\InGaAsSb_XAB1308_251022_64.0.txt',
    'InGaAsSb251022\InGaAsSb_XAB1309_251022_64.0.txt',
    'InGaAsSb251022\InGaAsSb_XK1786_251022_64.0.txt',
    'InGaAsSb251022\InGaAsSb_XK1787_251022_64.0.txt'
    ]
sample_name_list = [
    'XAB1308',
    'XAB1309',
    'XK1786',
    'XK1787'
]
thickness_list = [
    1000,
    1000,
    1000,
    1000
]
control_path = 'InGaAsSb251022\GaAs_un0821_251022_64_NIR.0.txt'
control_thickness = 350000

processor(control_path, 
    sample_path_list, 
    sample_name_list,
    thickness_list,
    control_thickness)


