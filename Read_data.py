import pandas as pd
import numpy as np
#una series de funciones para leer los diferentes archivos de datos
def ReadCSV(direccion, enco):
    precio = pd.read_csv(direccion, encoding=enco)
    precio.dropna(inplace=True)
    precio.drop_duplicates(inplace=True)
    return precio

def ReadJSON(direccion):
    precio = pd.read_json(direccion)
    precio.dropna(inplace=True)
    precio.drop_duplicates(inplace=True)
    return precio

def ReadPARQUET(direccion):
    producto = pd.read_parquet(direccion, engine='pyarrow')
    producto.set_index('id',inplace=True)
    producto.drop(columns=['categoria1','categoria2','categoria3'], inplace=True)
    producto.dropna(inplace=True)
    producto.drop_duplicates(inplace=True)
    return producto

def ReadTXT(direccion):
    precio = pd.read_csv(direccion, sep='|')
    precio.dropna(inplace=True)
    precio.drop_duplicates(inplace=True)
    precio.reset_index(inplace=True, drop=True)
    return precio