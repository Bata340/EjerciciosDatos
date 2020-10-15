import pandas as pd

datos = pd.read_csv('csv/Entrenamieto_ECI_2020.csv')
region_EMEA = datos['Region']=='EMEA'
datos_EMEA = datos[region_EMEA]
top_10 = datos_EMEA.nlargest(10, 'Total_Amount')
top_10_columnas = top_10[['ID', 'Territory', 'Delivery_Quarter', 'Delivery_Year']]
print(top_10_columnas.head(10))