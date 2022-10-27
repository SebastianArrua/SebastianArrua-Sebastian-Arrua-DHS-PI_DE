from sqlalchemy import Column, Integer, String, Float, ForeignKey
from declarative_base import Base

#Creo las tablas que se van a usar, con sus respectivas foreing key y primary key

class Sucursal(Base):

  __tablename__ = 'sucursal'
  id = Column(String(150), primary_key=True)
  comercioId = Column(Integer)
  banderaId = Column(Integer)
  banderaDescripcion = Column(String(150))
  comercioRazonSocial = Column(String(150))
  provincia = Column(String(150)) 
  localidad = Column(String(150))
  direccion = Column(String(150))
  lat = Column(Integer)
  lng = Column(Integer)
  sucursalNombre = Column(String(150))
  sucursalTipo = Column(String(150))

class Producto(Base):

  __tablename__ = 'producto'
  id = Column(String(150), primary_key=True)
  marca = Column(String(150))
  nombre = Column(String(150))
  presentacion = Column(String(150))

class Precio(Base):

  __tablename__ = 'precio'
  index = Column(Integer, primary_key=True)
  precio = Column(Float)
  producto_id = Column(Integer, ForeignKey('producto.id'))
  sucursal_id = Column(Integer, ForeignKey('sucursal.id'))