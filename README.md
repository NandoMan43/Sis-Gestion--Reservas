# Sistema de Gestión de Reservas de Alojamiento

El Sistema de Gestión de Reservas de Alojamiento es una aplicación basada en FastAPI que permite la creación, consulta, actualización y eliminación (CRUD) de alojamientos y reservas. El objetivo de este proyecto es gestionar de forma eficiente las reservas en alojamientos, permitiendo a los usuarios administrar su inventario de propiedades y las reservas asociadas de manera simple y rápida.

Este sistema utiliza FastAPI como framework web para crear una API RESTful, SQLAlchemy para la interacción con la base de datos y Pydantic para la validación de datos.

## Características

- Gestión de alojamientos (crear, leer, actualizar, eliminar).
- Gestión de reservas (crear, leer, actualizar, eliminar).
- Validación de datos con Pydantic.
- API documentada automáticamente con Swagger UI.
- Conexión a base de datos relacional mediante SQLAlchemy.

## Tecnologías Utilizadas

- **FastAPI**: Framework moderno para la creación de APIs web rápidas.
- **SQLAlchemy**: ORM utilizado para la gestión de la base de datos.
- **Pydantic**: Para validación de datos y manejo de esquemas.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación FastAPI

## Instalación

Para ejecutar este sistema de chat, sigue estos pasos:

1. **Crea un entorno virtual**:
   ```bash
   python -m venv venv
venv\Scripts\activate     # En Windows

2. **IInstala las dependencias del proyecto**:
   ```bash
   pip install -r requirements.txt

3. **IIniciar el servidor con Uvicorn**:
   ```bash
   uvicorn main:app --reload

### Estructura del Proyecto

La estructura del proyecto está organizada de la siguiente manera:

- **main.py**:   Archivo principal con los endpoints de la API.
- **models.py**:   Definición de los modelos de la base de datos
- **schemas.py**:   Esquemas para la validación de datos con Pydantic
- **crud.py**:   Operaciones CRUD encapsuladas para alojamientos y reservas
- **database.py**:    Configuración de la base de datos con SQLAlchemy
- **requirements.txt**:  Dependencias del proyecto
- **README.md**:   Información sobre el proyecto

## Descripción de los archivos principales:

- **main.py**:  Define los endpoints que gestionan las solicitudes HTTP y realiza las operaciones CRUD.
- **models.py**:  Contiene la definición de las tablas de la base de datos.
- **schemas.py**:  Contiene las clases de validación de datos que definen la estructura de las solicitudes.
- **crud.py**:  Incluye las funciones que realizan las operaciones en la base de datos.
- **database.py**:  Configura la conexión a la base de datos y gestiona las sesiones de la base de datos.

## Conclusión

Este sistema de gestión de reservas de alojamiento es un ejemplo práctico de cómo se pueden utilizar tecnologías modernas como FastAPI, SQLAlchemy y Pydantic para construir aplicaciones web escalables y eficientes. Gracias a la documentación generada automáticamente y la facilidad de despliegue, es una solución ideal para gestionar de manera sencilla las reservas de alojamiento en cualquier contexto.

El código está diseñado para ser extensible, lo que significa que nuevas características pueden ser agregadas sin comprometer la estructura base. Esto lo convierte en un excelente punto de partida para futuros proyectos o implementaciones más complejas.

