from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpRequest
from django.views.generic import (TemplateView, FormView, ListView)

from .forms import InputCityForm
from .models import WeatherData, CityData

# backends
from .Get5Days_WeatherForecast import getWeatherForecast

# Create your views here.

class SelectView(FormView):
    template_name = 'Get_5Days_WeatherData/select_test.html'
    form_class=InputCityForm
    # success_url = '/weather/'

    def form_valid(self, form, **kwargs):
        city_name = form.cleaned_data['citydata']
        city_name=city_name.split(':')
        city_name=city_name[1].split('}')
        [forecastDatetime, weatherDescription, temperature, rainfall] = \
            getWeatherForecast(city_name)
        weather_data = list(zip(forecastDatetime, weatherDescription, temperature, rainfall))
        context = super().get_context_data(**kwargs)
        context['weather_data'] = weather_data
        return render(self.request, 'Get_5Days_WeatherData/select.html', context)
    
class WeatherView(FormView):
    template_name = 'Get_5Days_WeatherData/select.html'
    form_class=InputCityForm
    # success_url = '/weather/'
    model = WeatherData

    def form_valid(self, form, **kwargs):
        # import pdb; pdb.set_trace()
        city_name = form.cleaned_data['citydata']
        city_name=city_name.split(':')
        city_name=city_name[1].split('}')
        [forecastDatetime, weatherDescription, temperature, rainfall] = \
            getWeatherForecast(city_name)
        weather_data = list(zip(forecastDatetime, weatherDescription, temperature, rainfall))
        context = super().get_context_data(**kwargs)
        context['weather_data'] = weather_data
        return render(self.request, 'Get_5Days_WeatherData/select.html', context)
    
    ## before version
    # [forecastDatetime, weatherDescription, temperature, rainfall] = \
    #         getWeatherForecast(1861060)
    # weather_data = list(zip(forecastDatetime, weatherDescription, temperature, rainfall))

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['weather_data'] = self.weather_data
    #     return context
