from django.urls import path
from . import views

# app_name = 'questions'

urlpatterns = [
    path('',views.QuestionListView.as_view(),name='question_list'),
    path('question/<int:pk>', views.QuestionDetailView.as_view(), name='question_detail'),
    path('question/new/', views.CreateQuestionView.as_view(), name='question_new'),
    path('question/<int:pk>/edit/', views.QuestionUpdateView.as_view(), name='question_edit'),
    path('question/<int:pk>/remove/', views.QuestionDeleteView.as_view(), name='question_remove'),
]
