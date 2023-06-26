import pandas as pd
def excel_filename_to_dataframe(filename,sheet_number,titles_list):
  # def es para crear una funcion en python
  # Si no especifico el numero de hoja, por defecto coge la 1ra hoja
  data=pd.read_excel(filename,sheet_name=sheet_number)
  # data es del tipo dataframe que es de PANDA
  data=data[titles_list];
  return data;

def dataframe_categorical_to_dataframe_binary(data,label):
  # agarra un label (catgeorico) y lo convierte en binario
  data[label]=data[label].astype('category');
  dummies=pd.get_dummies(data, columns=[label],prefix='',prefix_sep='');
  #convierten datos en 1 dimension a n dimensiones binarias
  return dummies
