from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from django.http import JsonResponse
from factoryproject.constants import APIErrorCode
from app import crud
from app.schemas import TypingOrChooseOneAnswerCreate, AnswerResponseAPI, QuizUserCreateUpdate
from app.db.session import Session


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_answer(request, quiz_id, question_id):
    try:
        db = Session()
        quiz = crud.quiz.get_by_id(obj_id=quiz_id)
        question = crud.question.get_question_by_quiz_id(db=db, quiz_id=quiz_id, question_id=question_id)
        if not quiz or not question:
            return JsonResponse({"details": APIErrorCode.ENTITY_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        is_answered = crud.answer.is_answered(db=db, question_id=question_id, user_id=request.user.id)
        if not is_answered:
            answer_data = TypingOrChooseOneAnswerCreate(
                **request.data,
                username=request.user.username if not request.data.get("anonymously") else None,
                question=question,
                user=request.user,
            )
            error = check_answer_errors(question, request.data.get("text"))
            if error:
                return error

            answer = crud.answer.create(obj_in=answer_data)
            quiz_answered_handler(quiz, request.user)
            return JsonResponse(AnswerResponseAPI.from_orm(answer).__dict__, status=status.HTTP_200_OK, safe=False)
        return JsonResponse({"details": APIErrorCode.ANSWERED}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return JsonResponse({"details": APIErrorCode.INVALID_DATA}, status=status.HTTP_400_BAD_REQUEST)


def quiz_answered_handler(quiz, user):
    quiz_questions = quiz.question.all()
    question_answers = [answer for question in quiz_questions
                        for answer in question.answer.all()
                        if answer.user_id == user.id]
    if len(quiz_questions) == len(question_answers):
        create_data = QuizUserCreateUpdate(
            quiz=quiz,
            user=user
        )
        crud.quiz_user.create(obj_in=create_data)


def check_answer_errors(question, text):
    if question.type == 'typing' or question.type == 'choose_one':
        if type(text) != str:
            return JsonResponse({"details": APIErrorCode.WRONG_DATA_TYPE}, status=status.HTTP_400_BAD_REQUEST)
    if question.type == 'choose_one':
        if text not in question.answer_options.keys():
            return JsonResponse({"details": APIErrorCode.WRONG_ONE_ANSWER}, status=status.HTTP_400_BAD_REQUEST)
    elif question.type == 'choose_many':
        if (type(text) != list) or (len(text) < 2):
            return JsonResponse({"details": APIErrorCode.WRONG_COUNT_ANSWERS}, status=status.HTTP_400_BAD_REQUEST)
        if not all(item in [i for i in question.answer_options.keys()] for item in text):
            return JsonResponse({"details": APIErrorCode.WRONG_MANY_ANSWERS}, status=status.HTTP_400_BAD_REQUEST)
