from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Puedes cambiar 'test.db' por el nombre que desees

# Crear el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Crear una clase base para los modelos
Base = declarative_base()

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para obtener la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
