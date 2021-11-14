from .base import BaseCRUD
from app.models import Question
from app import schemas


class QuestionCRUD(
    BaseCRUD[
        schemas.QuestionCreate,
        schemas.QuestionUpdate,
    ]
):
    def get_question_by_quiz_id(self, db, quiz_id, question_id):
        model = self.get_sa_model()
        obj_sa = db.query(model).filter(
            (model.quiz_id == quiz_id) &
            (model.id == question_id)
        ).one_or_none()
        return Question.objects.get(id=obj_sa.id) if obj_sa else None

    def get_questions_by_quiz_id(self, db, quiz_id):
        model = self.get_sa_model()
        return db.query(model).filter(
            (model.quiz_id == quiz_id)
        ).all()


question = QuestionCRUD(model=Question)
