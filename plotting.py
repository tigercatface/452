from matplotlib import pyplot as plt 
from processor import transmittancetoabsorbtioncoeff

df_2 =  transmittancetoabsorbtioncoeff(
     'InGaAsSb251022\GaAs_un0821_251022_64.0.txt',
     'InGaAsSb251022\InGaAsSb_XAB1308_251022_64.0.txt',
    1000)
df_1 =  transmittancetoabsorbtioncoeff(
    'InGaAsSb251022\GaAs_un0821_251022_64.0.txt',
    'InGaAsSb251022\InGaAsSb_XAB1309_251022_64.0.txt',
    1000)
df_1_lambda = df_1.index.values.tolist()
df_1_alpha = df_1['alpha'].values.tolist()

df_2_lambda = df_2.index.values.tolist()
df_2_alpha = df_2['alpha'].values.tolist()


plt.plot(df_1_lambda,df_1_alpha, label = 'XAB1309')
plt.plot(df_2_lambda,df_2_alpha, label = 'XAB1308')
plt.title("XAB1308 absorbtion coefficient")
plt.yscale("log")
plt.xlabel('wavelength (nm)')
plt.ylabel('absorption coefficient (cm-1)')
plt.legend()
plt.show()

