from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions, status
from django.http import JsonResponse
from factoryproject.constants import APIErrorCode
from app import crud
from app.schemas import QuestionCreate, QuestionResponseAPI, QuestionUpdate
from app.db.session import Session


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def create_question(request, quiz_id):
    try:
        quiz = crud.quiz.get_by_id(obj_id=quiz_id)
        if not quiz:
            return JsonResponse({"details": APIErrorCode.ENTITY_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
        question_data = QuestionCreate(
            **request.data,
            quiz=quiz
        )
        question = crud.question.create(obj_in=question_data)
        return JsonResponse(QuestionResponseAPI.from_orm(question).__dict__, status=status.HTTP_200_OK, safe=False)
    except:
        return JsonResponse({"details": APIErrorCode.INVALID_DATA}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
@permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def update_question(request, quiz_id, question_id):
    db = Session()
    question = crud.question.get_question_by_quiz_id(db=db, quiz_id=quiz_id, question_id=question_id)
    if not question:
        return JsonResponse({"details": APIErrorCode.ENTITY_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    question_data = QuestionUpdate(**request.data)
    updated_question = crud.question.update(obj_id=question.id, obj_in=question_data)
    return JsonResponse(QuestionResponseAPI.from_orm(updated_question).__dict__, status=status.HTTP_200_OK, safe=False)


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def delete_question(request, quiz_id, question_id):
    db = Session()
    question = crud.question.get_question_by_quiz_id(db=db, quiz_id=quiz_id, question_id=question_id)
    if not question:
        return JsonResponse({"details": APIErrorCode.ENTITY_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    deleted_quiz = crud.question.delete(obj=question)
    if deleted_quiz:
        return JsonResponse({"details": "Successful"}, status=status.HTTP_200_OK, safe=False)
    return JsonResponse({"details": APIErrorCode.INVALID_DATA}, status=status.HTTP_400_BAD_REQUEST, safe=False)
