import pandas as pd
import Read_data
from tables import Sucursal, Producto, Precio
from declarative_base import Base, engine, Session
import sqlite3
#En una variables guardo el PATH de los archivos que se van a usar en el ETL
precio1 = 'Datasets/precios_semana_20200413.csv'
precio2 = 'Datasets/precios_semana_20200503.json'
precio3 = 'Datasets/precios_semana_20200518.txt'
sucursal = 'Datasets/sucursal.csv'
producto = 'Datasets/producto.parquet'
#Concateno los DataFrame de los precios para luego subirlo a la db(Uso las funciones que estan en 'Read_data')
"""
df1 = Read_data.ReadCSV(precio1,'utf-16')
df2 = Read_data.ReadJSON(precio2)
df = pd.concat([df1,df2])
df.reset_index(inplace=True, drop=True)
"""
#Aca inicia la creacion de la db
if __name__ == '__main__':
   #Crea la BD
   Base.metadata.create_all(engine)

   #Abre la sesión
   session = Session()
   #Aca inicio la primera carga de datos
   """
   df.to_sql('precio', con=engine, if_exists='append')

   df = Read_data.ReadCSV(sucursal, 'utf-8')
   df.set_index('id',inplace=True) #Pongo el id como indice para que se cargue como un primary key
   df.to_sql('sucursal', con=engine, if_exists='append')

   df = Read_data.ReadPARQUET(producto)
   df.to_sql('producto', con=engine, if_exists='append')
   """
   #Me conecto a la base de datos para hacer consultas
   conn = sqlite3.connect('DataBase.db')
   """
   #Hago la carga incremental de datos
   #Primero guardo los datos en la bd en una variable
   df = pd.read_sql("SELECT * FROM precio", conn)
   #Arreglo el indice
   df.drop(columns='index', inplace=True)
   #Leo el archivo a cargar
   df1 = Read_data.ReadTXT(precio3)
   #Concateno los dos DataFrame
   df = pd.concat([df,df1])
   #Arreglo el indice para que sean valores unicos, es la primary key
   df.reset_index(inplace=True, drop=True)
   #Subo los datos a la db reemplazando los anteriores
   df.to_sql('precio', con=engine, if_exists='replace')
   """

   #Hago la consulta
   df = pd.read_sql("SELECT AVG(precio) as Promedio, sucursal_id FROM precio WHERE sucursal_id = '9-1-688'", conn)
   #Imprimo la consulta en pantalla
   print(df)
   #Sube la sesion
   session.commit()
   #Cierra la sesion
   session.close()