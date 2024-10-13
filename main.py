from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from models import Base
from schemas import AlojamientoCreate, Alojamiento, ReservaCreate, Reserva
import crud

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/alojamientos/", response_model=Alojamiento)
def crear_alojamiento(alojamiento: AlojamientoCreate, db: Session = Depends(get_db)):
    return crud.create_alojamiento(db=db, alojamiento=alojamiento)

@app.post("/reservas/", response_model=Reserva)
def crear_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    return crud.create_reserva(db=db, reserva=reserva)

@app.get("/alojamientos/", response_model=list[Alojamiento])
def obtener_alojamientos(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    alojamientos = crud.get_alojamientos(db, skip=skip, limit=limit)
    return alojamientos

@app.get("/reservas/", response_model=list[Reserva])
def obtener_reservas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    reservas = crud.get_reservas(db, skip=skip, limit=limit)
    return reservas
