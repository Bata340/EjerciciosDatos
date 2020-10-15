import pandas as pd
import numpy as np

datos = pd.read_csv('csv/Entrenamieto_ECI_2020.csv')
filtro = datos['Territory'] == 'Germany'
datos_germany = datos[filtro]
pd.to_numeric(datos_germany['Price'], errors='coerce')
(datos_germany['Price']).replace(['None', 'Other'], np.nan, inplace=True)
datos_germany.dropna(subset=['Price'],inplace=True)
datos_germany['Price']=pd.to_numeric(datos_germany['Price'], errors='coerce')
precio_promedio = datos_germany['Price'].mean()
print ("El precio promedio en Germany es: " + str(precio_promedio))