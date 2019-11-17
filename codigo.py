# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 18:43:43 2019

@author: Duber - Ernesto - Cristian

link del .csv (https://bit.ly/2r6diCb)

Tema: Valores financieros
Objetivo: Conocer el valor diaro de la bolsa de Santiago en Chile y el valor del dolar,
con el fin de observar si el aumento o disminucion del valor de la bolsa tiene impacto
en el valor del dolar.

"""

import pandas as pd
import requests

########################################################
############### CSV - Bolsa de Valores##################
########################################################

# Cargar datos de la bolsa de valores de Santiago (Diarios)
Bolsa_valores = pd.read_csv('Datos históricos S&P CLX IPSA.csv', sep=';')

print(Bolsa_valores.head(10))

print(Bolsa_valores.dtypes)

########################################################
############### API - Valor del dolar##################
########################################################

# cargar datos de la api del valor del dolar de todo el 2019
dolar = requests.get("https://mindicador.cl/api/dolar/2019")

# como usar si (condicion logica) si aplica, sino aplica
if dolar.status_code ==200:
    print("Captura exitosa")
else:
        print("error")

#pasamos datos a formato json
json_dolar = dolar.json()

#observamos el json para ver como se llama el campos que contiene los valores
json_dolar
json_dolar.keys()

# generamos el data frame
Valor_dolar = pd.DataFrame.from_dict(json_dolar["serie"])

# visualizamos el data frame
print(Valor_dolar.head(10))

# formato a columna fecha para que concida con el data frame de Bolsa_Valores