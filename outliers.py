import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv('ventas_totales_sinnulos.csv', index_col=0)
#print(df.head()) 

valores_nulos = df.isnull().sum()
#print(valores_nulos)

#fig = plt.figure(figsize =(7, 3))
#plt.hist(x=df["ventas_precios_corrientes"], color='red', rwidth=0.50)
#plt.title('Histograma de ventas_precios_corrientes con outliers')
#plt.xlabel('ventas_precios_corrientes')
#plt.ylabel('Frecuencia')
#plt.show()

#fig = plt.figure(figsize =(5, 3))
#plt.boxplot(df["ventas_precios_corrientes"]) 
#plt.title("Outliers de ventas_precios_corriente")
#plt.show() 

# ======== ======== ======== ========= ========= ======== 
# Método aplicando Cuartiles. - Columna #1 "ventas_precios_corrientes"
y=df["ventas_precios_corrientes"]
percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
#print(percentile25)
#print(percentile75)
iqr= percentile75 - percentile25
#print(iqr)

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
#print("Limite superior permitido usando Cuartiles", Limite_Superior_iqr)
#print("Limite inferior permitido usando Cuartiles", Limite_Inferior_iqr)

#Obtenemos datos limpios
data_clean_iqr_cuartiles= df[(y<Limite_Superior_iqr)&(y>Limite_Inferior_iqr)]
#print(data_clean_iqr)

#fig = plt.figure(figsize =(5, 3))
#plt.boxplot(data_clean_iqr_cuartiles["ventas_precios_corrientes"]) 
#plt.title("ventas_precios_corriente sin outliers (cuartiles)")
#plt.show() 

#fig = plt.figure(figsize =(7, 3))
#plt.hist(x=data_clean_iqr_cuartiles["ventas_precios_corrientes"], color='blue', rwidth=0.50)
#plt.title('Histograma de ventas_precios_corrientes sin outliers (cuartiles)')
#plt.xlabel('ventas_precios_corrientes')
#plt.ylabel('Frecuencia')
#plt.show()
data_clean_iqr_cuartiles["ventas_precios_corrientes"].to_csv('ventas_precios_corrientes_cuartiles.csv')


#Método desviación estándar - Columna #1 "ventas_precios_corrientes"
y=df["ventas_precios_corrientes"]
Limite_Superior_dev_std = y.mean() + 3 * y.std()
Limite_Inferior_dev_std = y.mean() - 3 * y.std()

#print('Limite superior permitido usando desv. estandar ', Limite_Superior_dev_std)
#print('Limite inferior permitido usando desv. estandar ', Limite_Inferior_dev_std)

data_clean_iqr_std_dev = df[(y<Limite_Superior_dev_std)&(y>Limite_Inferior_dev_std)]

#fig = plt.figure(figsize =(7, 3))
#plt.hist(x=data_clean_iqr_std_dev["ventas_precios_corrientes"], color='purple', rwidth=0.50)
#plt.title('Histograma de ventas_precios_corrientes sin outliers (dev. std.)')
#plt.xlabel('ventas_precios_corrientes')
#plt.ylabel('Frecuencia')
#plt.show()

#fig = plt.figure(figsize =(5, 3))
#plt.boxplot(data_clean_iqr_std_dev["ventas_precios_corrientes"]) 
#plt.title("ventas_precios_corriente sin outliers (dev. std.)")
#plt.show() 

data_clean_iqr_std_dev["ventas_precios_corrientes"].to_csv('ventas_precios_corrientes__dev_std.csv')

# ================ ================ ================ ================ ================

# COlUMNA # 2: "ventas_totales_canal_venta"
#fig = plt.figure(figsize =(7, 3))
#plt.hist(x=df["ventas_totales_canal_venta"], color='red', rwidth=0.50)
#plt.title('Histograma de ventas_totales_canal_venta con outliers')
#plt.xlabel('ventas_totales_canal_venta')
#plt.ylabel('Frecuencia')
#plt.show()

#fig = plt.figure(figsize =(5, 3))
#plt.boxplot(df["ventas_totales_canal_venta"]) 
#plt.title("Outliers de ventas_totales_canal_venta")
#plt.show() 

# Método aplicando Cuartiles. - COlUMNA # 2: "ventas_totales_canal_venta"
y=df["ventas_totales_canal_venta"]
percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
iqr = percentile75 - percentile25

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
#print("Limite superior permitido usando Cuartiles", Limite_Superior_iqr)
#print("Limite inferior permitido usando Cuartiles", Limite_Inferior_iqr)

#Obtenemos datos limpios
data_clean_iqr_cuartiles = df[(y<Limite_Superior_iqr)&(y>Limite_Inferior_iqr)]
#print(data_clean_iqr_cuartiles)

#fig = plt.figure(figsize =(5, 3))
#plt.boxplot(data_clean_iqr_cuartiles["ventas_totales_canal_venta"]) 
#plt.title("ventas_totales_canal_venta sin outliers (cuartiles)")
#plt.show() 

#fig = plt.figure(figsize =(7, 3))
#plt.hist(x=data_clean_iqr_cuartiles["ventas_totales_canal_venta"], color='blue', rwidth=0.50)
#plt.title('Histograma de ventas_totales_canal_venta sin outliers (cuartiles)')
#plt.xlabel('ventas_totales_canal_venta')
#plt.ylabel('Frecuencia')
#plt.show()

data_clean_iqr_cuartiles["ventas_totales_canal_venta"].to_csv('ventas_totales_canal_venta_cuartiles.csv')

#Método desviación estándar - COlUMNA # 2: "ventas_totales_canal_venta"
y=df["ventas_totales_canal_venta"]
Limite_Superior_dev_std = y.mean() + 3 * y.std()
Limite_Inferior_dev_std = y.mean() - 3 * y.std()

#print('Limite superior permitido usando desv. estandar ', Limite_Superior_dev_std)
#print('Limite inferior permitido usando desv. estandar ', Limite_Inferior_dev_std)

data_clean_iqr_std_dev = df[(y<Limite_Superior_dev_std)&(y>Limite_Inferior_dev_std)]

#fig = plt.figure(figsize =(7, 3))
#plt.hist(x=data_clean_iqr_std_dev["ventas_totales_canal_venta"], color='purple', rwidth=0.50)
#plt.title('Histograma de ventas_totales_canal_venta sin outliers (dev. std.)')
#plt.xlabel('ventas_totales_canal_venta')
#plt.ylabel('Frecuencia')
#plt.show()

#fig = plt.figure(figsize =(5, 3))
#plt.boxplot(data_clean_iqr_std_dev["ventas_totales_canal_venta"]) 
#plt.title("ventas_totales_canal_venta sin outliers (dev. std.)")
#plt.show() 

data_clean_iqr_std_dev["ventas_totales_canal_venta"].to_csv('ventas_totales_canal_venta_dev_std.csv')

# ================ ================ ================ ================ ================

# COlUMNA # 3: "tarjetas_credito"
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["tarjetas_credito"], color='red', rwidth=0.50)
plt.title('Histograma de tarjetas_credito con outliers')
plt.xlabel('tarjetas_credito')
plt.ylabel('Frecuencia')
#plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["tarjetas_credito"]) 
plt.title("Outliers de tarjetas_credito")
#plt.show() 

# Método aplicando Cuartiles. - COlUMNA # 3: "tarjetas_credito"
y=df["tarjetas_credito"]
percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
iqr = percentile75 - percentile25

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
#print("Limite superior permitido usando Cuartiles", Limite_Superior_iqr)
#print("Limite inferior permitido usando Cuartiles", Limite_Inferior_iqr)

#Obtenemos datos limpios
data_clean_iqr_cuartiles = df[(y<Limite_Superior_iqr)&(y>Limite_Inferior_iqr)]
#print(data_clean_iqr_cuartiles)

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr_cuartiles["tarjetas_credito"]) 
plt.title("tarjetas_credito sin outliers (cuartiles)")
#plt.show() 

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr_cuartiles["tarjetas_credito"], color='blue', rwidth=0.50)
plt.title('Histograma de tarjetas_credito sin outliers (cuartiles)')
plt.xlabel('tarjetas_credito')
plt.ylabel('Frecuencia')
#plt.show()

data_clean_iqr_cuartiles["tarjetas_credito"].to_csv('tarjetas_credito_cuartiles.csv')

#Método desviación estándar - COlUMNA # 3: "tarjetas_credito"
y=df["tarjetas_credito"]
Limite_Superior_dev_std = y.mean() + 3 * y.std()
Limite_Inferior_dev_std = y.mean() - 3 * y.std()

#print('Limite superior permitido usando desv. estandar ', Limite_Superior_dev_std)
#print('Limite inferior permitido usando desv. estandar ', Limite_Inferior_dev_std)

data_clean_iqr_std_dev = df[(y<Limite_Superior_dev_std)&(y>Limite_Inferior_dev_std)]

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr_std_dev["tarjetas_credito"], color='purple', rwidth=0.50)
plt.title('Histograma de tarjetas_credito sin outliers (dev. std.)')
plt.xlabel('tarjetas_credito')
plt.ylabel('Frecuencia')
#plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr_std_dev["tarjetas_credito"]) 
plt.title("tarjetas_credito sin outliers (dev. std.)")
plt.show() 

data_clean_iqr_std_dev["tarjetas_credito"].to_csv('tarjetas_credito_dev_std.csv')
