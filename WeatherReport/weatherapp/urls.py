from django.conf import settings
from django.urls import path
from .views import *


urlpatterns = [
    # path('', index, name='index'),
    path('download_weather_data/', get_region_wise_weather_data),

]
