from rest_framework.decorators import api_view, permission_classes
from datetime import datetime

from rest_framework.response import Response
from rest_framework import generics, permissions, status
from django.http import HttpResponse, JsonResponse
from factoryproject.constants import APIErrorCode
from rest_framework.pagination import PageNumberPagination
from app import crud
from app.schemas import QuizCreateUpdate, QuizesResponseAPI, QuestionWithAnswerResponseAPI, AnswerResponseAPI
from app.db.session import Session
from app.core.permissions import IsOwnerOrAdmin


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def create_quiz(request):
    try:
        quiz_data = QuizCreateUpdate(**request.data)
        quiz = crud.quiz.create(obj_in=quiz_data)
        return JsonResponse(QuizCreateUpdate.from_orm(quiz).__dict__, status=status.HTTP_200_OK, safe=False)
    except:
        return JsonResponse({"details": APIErrorCode.INVALID_DATA}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
@permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def update_quiz(request, quiz_id):
    quiz_data = QuizCreateUpdate(**request.data)
    updated_quiz = crud.quiz.update(obj_id=quiz_id, obj_in=quiz_data)
    if not updated_quiz:
        return JsonResponse({"details": APIErrorCode.ENTITY_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    return JsonResponse(QuizCreateUpdate.from_orm(updated_quiz).__dict__, status=status.HTTP_200_OK, safe=False)


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated, permissions.IsAdminUser])
def delete_quiz(request, quiz_id):
    quiz = crud.quiz.get_by_id(obj_id=quiz_id)
    if not quiz:
        return JsonResponse({"details": APIErrorCode.ENTITY_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    deleted_quiz = crud.quiz.delete(obj=quiz)
    if deleted_quiz:
        return JsonResponse({"details": "Successful"}, status=status.HTTP_200_OK, safe=False)
    return JsonResponse({"details": APIErrorCode.INVALID_DATA}, status=status.HTTP_400_BAD_REQUEST, safe=False)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_active_quizes(request):
    db = Session()
    paginator = PageNumberPagination()
    paginator.page_size = 10
    quizes_db = crud.quiz.get_active(db=db)
    quizes = []
    result_page = paginator.paginate_queryset(quizes_db, request)
    for quiz in result_page:
        quizes.append(QuizCreateUpdate.from_orm(quiz).__dict__)
    return paginator.get_paginated_response(quizes)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated, IsOwnerOrAdmin])
def get_answered_quizes(request):
    db = Session()
    user_id = request.query_params.get("user_id")
    quizes_db = crud.quiz.get_answered_quizes_by_user_id(db=db, user_id=user_id)
    paginator = PageNumberPagination()
    paginator.page_size = 10
    quizes = []
    result_page = paginator.paginate_queryset(quizes_db, request)
    for quiz in result_page:
        quizes.append(QuizesResponseAPI(
            **quiz.__dict__,
            questions=[QuestionWithAnswerResponseAPI(
                question_num=num,
                **question.__dict__,
                answer=AnswerResponseAPI.from_orm(
                    crud.answer.get_question_answer_by_user(db=db, user_id=user_id, question_id=question.id)
                ).__dict__
            ).__dict__ for num, question in enumerate(quiz.question, start=1)]
        ).__dict__)
    return paginator.get_paginated_response(quizes)
