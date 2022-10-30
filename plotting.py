from matplotlib import pyplot as plt 
from processor import transmittancetoabsorbtioncoeff

df_1 =  transmittancetoabsorbtioncoeff(
    'InGaAsSb251022\GaAs_un0821_251022_64.0.txt',
    'InGaAsSb251022\InGaAsSb_XAB1308_251022_64.0.txt',
    1500)
df_1_lambda = df_1.index.values.tolist()
df_1_alpha = df_1['alpha'].values.tolist()

print(df_1)

plt.plot(df_1_alpha,df_1_lambda)
plt.title("XAB1308 absorbtion coefficient")
plt.yscale("log", nonposy='clip')
plt.xlabel('wavelength (nm)')
plt.ylabel('absorption coefficient (cm-1)')
plt.show()

