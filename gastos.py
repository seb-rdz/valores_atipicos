import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_excel('gastos_costos_20_23.xlsx')
#print(df.isnull().sum())

# LIMPIO VALORES NULOS 
df['FOLIO'].fillna('--', inplace=True)
df['GASTO'].fillna('--', inplace=True)
df['TC'].fillna('--', inplace=True)
df['IMPORTE'].fillna(0, inplace=True)
df['IVA'].fillna(0, inplace=True)
df['TIPO'].fillna('--', inplace=True)
df['POLIZA'].fillna('--', inplace=True)

valores_nulos = df.isnull().sum()
#print(valores_nulos)

# =========== =========== =========== =========== =========== ===========
# COLUMNA # 1: "IMPORTE"
#fig = plt.figure(figsize =(7, 3))
#plt.hist(x=df["IMPORTE"], color='red', rwidth=0.50)
#plt.title('Histograma de IMPORTE con outliers')
#plt.xlabel('IMPORTE')
#plt.ylabel('Frecuencia')
#plt.show() 

#fig = plt.figure(figsize =(5, 3))
#plt.boxplot(df["IMPORTE"]) 
#plt.title("Outliers de IMPORTE")
#plt.show() 

# Método Cuartiles. - Columna #1 "IMPORTE"
y=df["IMPORTE"] 
percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
#print(percentile25)
#print(percentile75)
iqr = percentile75 - percentile25
#print(iqr)

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
#print("Limite superior permitido usando Cuartiles", Limite_Superior_iqr)
#print("Limite inferior permitido usando Cuartiles", Limite_Inferior_iqr)

#Obtenemos datos limpios
data_clean_iqr_cuartiles= df[(y<Limite_Superior_iqr)&(y>Limite_Inferior_iqr)]
#print(data_clean_iqr)

#fig = plt.figure(figsize =(5, 3))
#plt.boxplot(data_clean_iqr_cuartiles["IMPORTE"]) 
#plt.title("IMPORTE sin outliers (cuartiles)")
#plt.show() 

#fig = plt.figure(figsize =(7, 3))
#plt.hist(x=data_clean_iqr_cuartiles["IMPORTE"], color='blue', rwidth=0.50)
#plt.title('Histograma de IMPORTE sin outliers (cuartiles)')
#plt.xlabel('IMPORTE')
#plt.ylabel('Frecuencia')
#plt.show()

data_clean_iqr_cuartiles["IMPORTE"].to_csv('IMPORTE_cuartiles.csv')

#Método desviación estándar - Columna #1 "IMPORTE"
y=df["IMPORTE"]
Limite_Superior_dev_std = y.mean() + 3 * y.std()
Limite_Inferior_dev_std = y.mean() - 3 * y.std()
#print('Limite superior permitido usando desv. estandar ', Limite_Superior_dev_std)
#print('Limite inferior permitido usando desv. estandar ', Limite_Inferior_dev_std)

data_clean_iqr_std_dev = df[(y<Limite_Superior_dev_std)&(y>Limite_Inferior_dev_std)]

#fig = plt.figure(figsize =(7, 3))
#plt.hist(x=data_clean_iqr_std_dev["IMPORTE"], color='purple', rwidth=0.50)
#plt.title('Histograma de IMPORTE sin outliers (dev. std.)')
#plt.xlabel('IMPORTE')
#plt.ylabel('Frecuencia')
#plt.show()

#fig = plt.figure(figsize =(5, 3))
#plt.boxplot(data_clean_iqr_std_dev["IMPORTE"]) 
#plt.title("IMPORTE sin outliers (dev. std.)")
#plt.show() 

data_clean_iqr_std_dev["IMPORTE"].to_csv('IMPORTE_dev_std.csv')

# =========== =========== =========== =========== =========== ===========
# # COLUMNA # 2: "TOTAL MX"
#fig = plt.figure(figsize =(7, 3))
#plt.hist(x=df["TOTAL MX"], color='red', rwidth=0.50)
#plt.title('Histograma de TOTAL MX con outliers')
#plt.xlabel('TOTAL MX')
#plt.ylabel('Frecuencia')
#plt.show() 

#fig = plt.figure(figsize =(5, 3))
#plt.boxplot(df["TOTAL MX"]) 
#plt.title("Outliers de TOTAL MX")
#plt.show() 

# Método Cuartiles. - Columna #2 "TOTAL MX"
y=df["TOTAL MX"] 
percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
#print(percentile25)
#print(percentile75)
iqr = percentile75 - percentile25
#print(iqr)

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
#print("Limite superior permitido usando Cuartiles", Limite_Superior_iqr)
#print("Limite inferior permitido usando Cuartiles", Limite_Inferior_iqr)

#Obtenemos datos limpios
data_clean_iqr_cuartiles= df[(y<Limite_Superior_iqr)&(y>Limite_Inferior_iqr)]
#print(data_clean_iqr)

#fig = plt.figure(figsize =(5, 3))
#plt.boxplot(data_clean_iqr_cuartiles["TOTAL MX"]) 
#plt.title("TOTAL MX sin outliers (cuartiles)")
#plt.show() 

#fig = plt.figure(figsize =(7, 3))
#plt.hist(x=data_clean_iqr_cuartiles["TOTAL MX"], color='blue', rwidth=0.50)
#plt.title('Histograma de TOTAL MX sin outliers (cuartiles)')
#plt.xlabel('TOTAL MX')
#plt.ylabel('Frecuencia')
#plt.show()

data_clean_iqr_cuartiles["TOTAL MX"].to_csv('TOTAL_MX_cuartiles.csv')

#Método desviación estándar - Columna #2 "TOTAL MX"
y=df["TOTAL MX"]
Limite_Superior_dev_std = y.mean() + 3 * y.std()
Limite_Inferior_dev_std = y.mean() - 3 * y.std()
#print('Limite superior permitido usando desv. estandar ', Limite_Superior_dev_std)
#print('Limite inferior permitido usando desv. estandar ', Limite_Inferior_dev_std)

data_clean_iqr_std_dev = df[(y<Limite_Superior_dev_std)&(y>Limite_Inferior_dev_std)]

#fig = plt.figure(figsize =(7, 3))
#plt.hist(x=data_clean_iqr_std_dev["TOTAL MX"], color='purple', rwidth=0.50)
#plt.title('Histograma de TOTAL MX sin outliers (dev. std.)')
#plt.xlabel('TOTAL MX')
#plt.ylabel('Frecuencia')
#plt.show()

#fig = plt.figure(figsize =(5, 3))
#plt.boxplot(data_clean_iqr_std_dev["TOTAL MX"]) 
#plt.title("TOTAL MX sin outliers (dev. std.)")
#plt.show() 

data_clean_iqr_std_dev["TOTAL MX"].to_csv('TOTAL_MX_dev_std.csv')

# =========== =========== =========== =========== =========== ===========
# COLUMNA # 3: "TOTAL SAT"
fig = plt.figure(figsize =(7, 3))
plt.hist(x=df["TOTAL SAT"], color='red', rwidth=0.50)
plt.title('Histograma de TOTAL SAT con outliers')
plt.xlabel('TOTAL SAT')
plt.ylabel('Frecuencia')
#plt.show() 

fig = plt.figure(figsize =(5, 3))
plt.boxplot(df["TOTAL SAT"]) 
plt.title("Outliers de TOTAL SAT")
#plt.show() 

# Método Cuartiles. - Columna #3 "TOTAL SAT"
y=df["TOTAL SAT"] 
percentile25=y.quantile(0.25) #Q1
percentile75=y.quantile(0.75) #Q3
#print(percentile25)
#print(percentile75)
iqr = percentile75 - percentile25
#print(iqr)

Limite_Superior_iqr= percentile75 + 1.5*iqr
Limite_Inferior_iqr= percentile25 - 1.5*iqr
#print("Limite superior permitido usando Cuartiles", Limite_Superior_iqr)
#print("Limite inferior permitido usando Cuartiles", Limite_Inferior_iqr)

#Obtenemos datos limpios
data_clean_iqr_cuartiles= df[(y<Limite_Superior_iqr)&(y>Limite_Inferior_iqr)]
#print(data_clean_iqr)

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr_cuartiles["TOTAL SAT"]) 
plt.title("TOTAL SAT sin outliers (cuartiles)")
#plt.show() 

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr_cuartiles["TOTAL SAT"], color='blue', rwidth=0.50)
plt.title('Histograma de TOTAL SAT sin outliers (cuartiles)')
plt.xlabel('TOTAL SAT')
plt.ylabel('Frecuencia')
#plt.show()

data_clean_iqr_cuartiles["TOTAL SAT"].to_csv('TOTAL_SAT_cuartiles.csv')

#Método desviación estándar - Columna #3 "TOTAL SAT"
y=df["TOTAL SAT"]
Limite_Superior_dev_std = y.mean() + 3 * y.std()
Limite_Inferior_dev_std = y.mean() - 3 * y.std()
#print('Limite superior permitido usando desv. estandar ', Limite_Superior_dev_std)
#print('Limite inferior permitido usando desv. estandar ', Limite_Inferior_dev_std)

data_clean_iqr_std_dev = df[(y<Limite_Superior_dev_std)&(y>Limite_Inferior_dev_std)]

fig = plt.figure(figsize =(7, 3))
plt.hist(x=data_clean_iqr_std_dev["TOTAL SAT"], color='purple', rwidth=0.50)
plt.title('Histograma de TOTAL SAT sin outliers (dev. std.)')
plt.xlabel('TOTAL SAT')
plt.ylabel('Frecuencia')
#plt.show()

fig = plt.figure(figsize =(5, 3))
plt.boxplot(data_clean_iqr_std_dev["TOTAL SAT"]) 
plt.title("TOTAL SAT sin outliers (dev. std.)")
plt.show() 

data_clean_iqr_std_dev["TOTAL SAT"].to_csv('TOTAL_SAT_dev_std.csv')