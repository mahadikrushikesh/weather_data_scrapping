from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(WeatherRegionParameters)
admin.site.register(RankWiseWeatherInfo)
admin.site.register(YearWiseWeatherInfo)

