from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_tablas import Establecimiento,Canton,Base

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()


##Consutas
#-A cada cantón pedirle el número de estudiantes
for canton in session.query(Canton).all():
    print(f"Cantón: {canton.nombCanton}")
    print(f"Número de estudiantes: {canton.obtener_numero_estudiantes(session)}")
    print("-------------------------")

#- A cada provincia perdile el número de docentes
# Suponiendo que 'session' es tu sesión SQLAlchemy activa

#- A cada parroaquia preguntar el número de establecimientos
# Suponiendo que 'session' es tu sesión SQLAlchemy activa


#- A cada provincia preguntar la lista de parroquias
# Suponiendo que 'session' es tu sesión SQLAlchemy activa

#- A cada parroquia preguntarle los tipos jornada de los establecimientos
