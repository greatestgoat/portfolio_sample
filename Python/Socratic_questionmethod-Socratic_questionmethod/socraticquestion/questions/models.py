from django.db import models
from django.utils import timezone
from django.urls import reverse

Question_Cotents = [
    '問題の具体的なゴールは?',
    '問題についてわかっていないことは?',
    'いまの答えを事実だと考えた理由は?',
    'いまの自分の考え方やアイデアはどこから得たものだろう?',
    '問題を試したらどんな効果があるだろう?',
    '他の人はこの問題にどう答えるだろう?',
    'いまの答えの代わりにどんな答えが考えられるだろう?',
]

class Question(models.Model):
    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    question_title = models.CharField(
        max_length=200,
        verbose_name='タイトル',
    )
    question_and_anwers_clarification = models.CharField(
        max_length=200,
        verbose_name=Question_Cotents[0],
        null=True, blank=True,
    )
    question_and_anwers_premise = models.CharField(
        max_length=200,
        verbose_name=Question_Cotents[1],
        null=True, blank=True,
    )
    question_and_anwers_evidence = models.CharField(
        max_length=200,
        verbose_name=Question_Cotents[2],
        null=True, blank=True,
    )
    question_and_anwers_origin = models.CharField(
        max_length=200,
        verbose_name=Question_Cotents[3],
        null=True, blank=True,
    )
    question_and_anwers_result = models.CharField(
        max_length=200,
        verbose_name=Question_Cotents[4],
        null=True, blank=True,
    )
    question_and_anwers_view = models.CharField(
        max_length=200,
        verbose_name=Question_Cotents[5],
        null=True, blank=True,
    )
    question_and_anwers_assumption = models.CharField(
        max_length=200,
        verbose_name=Question_Cotents[6],
        null=True, blank=True,
    )
    def get_absolute_url(self):
        return reverse("question_detail",kwargs={'pk':self.pk})     

    def __str__(self):
        return self.question_title