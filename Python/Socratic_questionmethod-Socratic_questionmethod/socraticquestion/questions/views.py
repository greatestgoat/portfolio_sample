from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import (TemplateView, ListView, 
                                    DetailView, CreateView,
                                    UpdateView, DeleteView)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Question
from .forms import QuestionForm
# Create your views here.

class QuestionListView(ListView):
    model = Question

    def get_queryset(self):
        return Question.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

class QuestionDetailView(DetailView):
    model = Question

class CreateQuestionView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'questions/question_detail.html'
    form_class = QuestionForm
    model = Question
        

class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'questions/question_detail.html'
    form_class = QuestionForm
    model = Question

class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('question_list')