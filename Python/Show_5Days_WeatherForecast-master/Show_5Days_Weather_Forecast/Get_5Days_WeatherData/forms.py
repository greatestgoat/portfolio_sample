from django import forms
from .load_citynames import load_citynames

from .models import InputCity, CityData

# class InputCityForm(forms.ModelForm):
    
#     class Meta:
#         model = InputCity
#         fields = ('input_city_name',\
#         )

#         widgets = {
#             'input_city_name': forms.TextInput(attrs={'size': 10}),
#         }

class InputCityForm(forms.Form):
    citydata = forms.ModelChoiceField(queryset=CityData.objects.all().values('id'))
    # class Meta:
    #     model = CityData
    #     fields = ('id',\
    #     )

    #     widgets = {
    #         'id': forms.ModelChoiceField(queryset=model.objects.all().values('id')),
    #     }