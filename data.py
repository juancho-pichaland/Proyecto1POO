from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    email = Column(String)
    password = Column(String)

class Receta(Base):
    __tablename__ = "recetas"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(String)
    ingredientes = Column(String)
    instrucciones = Column(String)

class Planificacion(Base):
    __tablename__ = "planificaciones"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    receta_id = Column(Integer, ForeignKey("recetas.id"))
    fecha = Column(DateTime)

class ListaCompras(Base):
    __tablename__ = "listas_compras"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    receta_id = Column(Integer, ForeignKey("recetas.id"))
    ingredientes = Column(String)

class Inventario(Base):
    __tablename__ = "inventarios"
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    ingredientes = Column(String)
