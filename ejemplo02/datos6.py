from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_ # se importa el operador and

# se importa la clase(s) del
# archivo genera_tablas
from crear_tablas import *

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# Los cantones que tiene establecimientos como número de estudiantes tales como: 1, 74, 100"

establecimientos = session.query(Establecimiento).join(
    Establecimiento.parroquia
).join(
	Parroquia.canton
).filter(
	Establecimiento.numEstudiantes.in_([1, 74, 100])
).all()

print("Los cantones que tiene establecimientos como número de estudiantes tales como: 1, 74, 100")
for establecimiento in establecimientos:
	print("Nombre de las Parroquias: %s | Numero de estudiantes 1,74,100: %s" 
	   % (establecimiento.parroquia.canton.nombCanton,
	   establecimiento.numEstudiantes))
