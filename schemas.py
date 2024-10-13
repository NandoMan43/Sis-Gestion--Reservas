from pydantic import BaseModel
from datetime import date

class AlojamientoBase(BaseModel):
    nombre: str
    direccion: str
    precio_noche: float
    descripcion: str

class AlojamientoCreate(AlojamientoBase):
    pass

class Alojamiento(AlojamientoBase):
    id: int

    class Config:
        orm_mode = True

class ReservaBase(BaseModel):
    alojamiento_id: int
    nombre_cliente: str
    fecha_inicio: str
    fecha_fin: str

class ReservaCreate(ReservaBase):
    pass

class Reserva(ReservaBase):
    id: int

    class Config:
        orm_mode = True
