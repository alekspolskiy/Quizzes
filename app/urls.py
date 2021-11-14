from django.urls import path, include
from app.api import views


urlpatterns = [
    path('quiz/create/', views.create_quiz, name='create-quiz'),
    path('quiz/delete/<str:quiz_id>/', views.delete_quiz, name='delete-quiz'),
    path('quiz/update/<str:quiz_id>/', views.update_quiz, name='update-quiz'),
    path('quiz/actives/', views.get_active_quizes, name='active-quiz'),
    path('quiz/<str:quiz_id>/question/create/', views.create_question, name='create-question'),
    path('quiz/<str:quiz_id>/question/update/<str:question_id>/', views.update_question, name='update-question'),
    path('quiz/<str:quiz_id>/question/delete/<str:question_id>/', views.delete_question, name='delete-question'),
    path('quiz/<str:quiz_id>/question/<str:question_id>/answer/', views.create_answer, name='create-answer'),
    path('quiz/answered/', views.get_answered_quizes, name='answered-quizes'),
]
