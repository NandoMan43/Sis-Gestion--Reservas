from sqlalchemy.orm import Session
from models import Alojamiento, Reserva
from schemas import AlojamientoCreate, ReservaCreate

def create_alojamiento(db: Session, alojamiento: AlojamientoCreate):
    db_alojamiento = Alojamiento(**alojamiento.dict())
    db.add(db_alojamiento)
    db.commit()
    db.refresh(db_alojamiento)
    return db_alojamiento

def create_reserva(db: Session, reserva: ReservaCreate):
    db_reserva = Reserva(**reserva.dict())
    db.add(db_reserva)
    db.commit()
    db.refresh(db_reserva)
    return db_reserva

def get_alojamientos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Alojamiento).offset(skip).limit(limit).all()

def get_reservas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Reserva).offset(skip).limit(limit).all()
