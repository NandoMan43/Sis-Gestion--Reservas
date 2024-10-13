from sqlalchemy import Column, Integer, String, Float
from database import Base

class Alojamiento(Base):
    __tablename__ = "alojamientos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    direccion = Column(String)
    precio_noche = Column(Float)
    descripcion = Column(String)

class Reserva(Base):
    __tablename__ = "reservas"

    id = Column(Integer, primary_key=True, index=True)
    alojamiento_id = Column(Integer)
    nombre_cliente = Column(String)
    fecha_inicio = Column(String)  # Puedes cambiar esto a Date si prefieres
    fecha_fin = Column(String)      # Puedes cambiar esto a Date si prefieres
