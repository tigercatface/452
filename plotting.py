from matplotlib import pyplot as plt 
from processor import transmittancetoabsorbtioncoeff, alphacontrol

# Impport and process 4 sets of data 
df_2 =  transmittancetoabsorbtioncoeff(
     'InGaAsSb251022\GaAs_un0821_251022_64.0.txt',
     'InGaAsSb251022\InGaAsSb_XAB1308_251022_64.0.txt',
    1000
)
df_1 =  transmittancetoabsorbtioncoeff(
    'InGaAsSb251022\GaAs_un0821_251022_64.0.txt',
    'InGaAsSb251022\InGaAsSb_XAB1309_251022_64.0.txt',
    1000
)

df_3 = transmittancetoabsorbtioncoeff(
    'InGaAsSb251022\GaAs_un0821_251022_64.0.txt',
    'InGaAsSb251022\InGaAsSb_XK1786_251022_64.0.txt',
    1000
)

df_4 = transmittancetoabsorbtioncoeff(
    'InGaAsSb251022\GaAs_un0821_251022_64.0.txt',
    'InGaAsSb251022\InGaAsSb_XK1787_251022_64.0.txt',
    1000

)
#Import the substrate constrol 
df_control = alphacontrol(
    'InGaAsSb251022\GaAs_un0821_251022_64.0.txt',
    1500 # This is an estimate 
)

df_1_lambda = df_1.index.values.tolist()
df_1_alpha = df_1['alpha'].values.tolist()

df_2_lambda = df_2.index.values.tolist()
df_2_alpha = df_2['alpha'].values.tolist()

df_3_lambda = df_3.index.values.tolist()
df_3_alpha = df_3['alpha'].values.tolist()

df_4_lambda = df_4.index.values.tolist()
df_4_alpha = df_4['alpha'].values.tolist()

df_c_lambda = df_control.index.values.tolist()
df_c_alpha = df_control['alpha'].values.tolist()


plt.plot(df_1_lambda,df_1_alpha, label = 'XAB1309')
plt.plot(df_2_lambda,df_2_alpha, label = 'XAB1308')
plt.plot(df_3_lambda,df_3_alpha, label = 'XK1786')
plt.plot(df_4_lambda,df_4_alpha, label = 'XK1787')
plt.plot(df_c_lambda,df_c_alpha, label = 'GaAs')
plt.title("InGaAsSb Absorption against Wavelength")
plt.yscale("log")
plt.xlabel('wavelength (nm)')
plt.ylabel('absorption coefficient (cm-1)')
plt.legend()
plt.show()

