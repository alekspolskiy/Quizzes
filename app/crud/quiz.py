from datetime import datetime
from .base import BaseCRUD
from app import models
from app import schemas


class QuizCRUD(
    BaseCRUD[
        schemas.QuizCreateUpdate,
        schemas.QuizCreateUpdate,
    ]
):
    def get_active(self, db):
        model = self.get_sa_model()
        return db.query(model).filter(model.end_date < datetime.utcnow()).all()

    def get_answered_quizes_by_user_id(self, db, user_id):
        model = self.get_sa_model()
        QuizUser = models.QuizUser.sa
        return db.query(model).join(QuizUser).filter(
            (QuizUser.user_id == user_id)
        ).all()


quiz = QuizCRUD(model=models.Quiz)
