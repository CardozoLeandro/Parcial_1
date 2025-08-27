from app import db
from app.models import Alumno
from app.repositories import MetodoCRUD

class AlumnoRepository(MetodoCRUD):
    
    model = Alumno

    @staticmethod
    def actualizar(alumno) -> Alumno:
        """
        Actualiza un alumno en la base de datos.
        """
        alumno_existente = db.session.merge(alumno)
        if not alumno_existente:
            return None
        db.session.commit()
        return alumno_existente