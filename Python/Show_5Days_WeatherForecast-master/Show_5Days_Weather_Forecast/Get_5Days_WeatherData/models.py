from django.db import models

# # Create your models here.

class CityData(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.

    # input_city_name = models.CharField(
    #     max_length = 100,
    #     choices=id,
    #     verbose_name='City:',
    # )
    class Meta:
        managed = False
        db_table = 'city_data'

    # def __str__(self):
    #     return self.input_city_name

class InputCity(models.Model):
    # citydata = CityData()
    # city_iddata = citydata.objects.all().values('id')
    input_city_name = models.CharField(
        max_length = 100,
        verbose_name='City:',
    )

    def __str__(self):
        return self.input_city_name
    
class WeatherData(models.Model):
    time = models.CharField(
        max_length=100,
    )
    weather = models.CharField(
        max_length=100,
    )
    temperature = models.FloatField(
    )
    rainfall = models.FloatField(
    )

