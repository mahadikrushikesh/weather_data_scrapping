import datetime

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .weather_data_handler import GetWeather
from .models import *
# Create your views here.


@api_view(['GET', 'POST'])
def get_region_wise_weather_data(request):
    """
    To download region wise weather data, based on provided parameters
    url:   http://127.0.0.1:8000/weather/download_weather_data/

    Select regions and parameters from given below lists

    Parameters list = ["Min temp", "Max temp", "Mean temp", "Rain days >= 1.0mm", "Rainfall", "Sunshine", "Days of air frost"]

    Regions list = ["UK", "England", "Wales", "Scotland", "England S", "Scotland N", "Scotland E",
        "Northern Ireland", "England & Wales", "England N", "Scotland W", "England E & NE", "England NW/Wales N",
        "Midlands", "East Anglia", "England SW/Wales S", "England SE/Central S"]

    request:
    Method POST:

    *** Payload ***
    {
    "region": "UK",
    "parameter": "Rainfall"
    }

    :return:
    JSON data by ordered by rank and year wise
    """
    selected_region = request.data.get("region", None)
    selected_parameter = request.data.get("parameter", None)
    response_data = {"data": None, "status": False, "response_msg": ""}
    if selected_region and selected_parameter:
        obj = GetWeather(selected_region, selected_parameter)
        region = obj.get_region_value()
        parameter = obj.get_parameter_value()
        if region and parameter:
            data = obj.scrape_weather_data(parameter, region)
            if data:
                response_data["data"] = data
                response_data["status"] = True
                response_data["response_msg"] = "Data Retrieved successfully"
            else:
                response_data["response_msg"] = "Data Not Found for given parameters"
        else:
            response_data["response_msg"] = "Provide valid Region and Parameter from given lists"
    else:
        response_data["response_msg"] = "Provide region and parameter values"
    return Response(response_data)

