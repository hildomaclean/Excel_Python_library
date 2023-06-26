import pandas as pd
# esta funcion levanta un excel y lo convierte en un objeto del tipo dataframe
# filename, es un string q corresponde al nombre del file (excel)
# sheet_number, es el numero de la hoja del excel que inicia en 0
# titles_list, es una lista de stream que corresponde a la cadena que esta en la primera fila del excel

def excel_filename_to_dataframe(filename,sheet_number,titles_list):
  # def es para crear una funcion en python
  # Si no especifico el numero de hoja, por defecto coge la 1ra hoja
  data=pd.read_excel(filename,sheet_name=sheet_number)
  # data es del tipo dataframe que es de PANDA
  data=data[titles_list];
  return data;

# esta funcion convierte una columna categorica en varias columnas categoricas binarias 
# que se representan en N dimensiones (iguial a N categorias)
# data, que es un objeto del tipo DATAFRAME (ES UN ARREGLE DE CADENAS)
# label, es un string con el nombre de la columna que deseo convertir a categorico binarios

def dataframe_categorical_to_dataframe_binary(data,label):
  # agarra un label (catgeorico) y lo convierte en binario
  data[label]=data[label].astype('category');
  dummies=pd.get_dummies(data, columns=[label],prefix='',prefix_sep='');
  #convierten datos en 1 dimension a n dimensiones binarias
  return dummies
