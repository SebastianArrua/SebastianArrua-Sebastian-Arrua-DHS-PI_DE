from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///DataBase.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()
#Inicio las clases que van a dar a lugar para crear la base de datos