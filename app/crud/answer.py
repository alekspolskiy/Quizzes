from .base import BaseCRUD
from app import models
from app import schemas


class AnswerCRUD(
    BaseCRUD[
        schemas.TypingOrChooseOneAnswerCreate,
        schemas.TypingOrChooseOneAnswerCreate,
    ]
):
    def is_answered(self, db, question_id, user_id):
        model = self.get_sa_model()
        answer = db.query(model).filter(
            (model.question_id == question_id) &
            (model.user_id == user_id)
        ).one_or_none()
        return True if answer else False

    def get_question_answer_by_user(self, db, user_id, question_id):
        model = self.get_sa_model()
        return db.query(model).filter(
            (model.user_id == user_id) &
            (model.question_id == question_id)
        ).one_or_none()

    def get_question_answers_by_user(self, db, user_id, question_id):
        model = self.get_sa_model()
        return db.query(model).filter(
            (model.user_id == user_id) &
            (model.question_id == question_id)
        ).all()


answer = AnswerCRUD(model=models.Answer)
