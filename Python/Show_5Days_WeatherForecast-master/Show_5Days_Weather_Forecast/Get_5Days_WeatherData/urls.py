from django.urls import path
from . import views

app_name='Get_5Days_WeatherData'

urlpatterns = [
    path('', views.SelectView.as_view(), name='select'),
    path('weather/', views.WeatherView.as_view(), name='weather')
]
