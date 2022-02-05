import datetime
import io
import json
import os
import pprint
import time
import urllib
from .models import *
import pandas as pd
import requests


class GetWeather(object):
    def __init__(self, region, param):
        self.region = region
        self.param = param
        self.updated_date = datetime.date.today()

    def scrape_weather_data(self, parameter, region):
        dictionary = dict()
        for order in ["ranked", "date"]:
            url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{}/{}/{}.txt'.format(parameter,
                                                                                                          order,
                                                                                                          region)
            print(url)

            weather_url = requests.get(url).text
            time.sleep(1)

            ''' Below statement used To get last_updated date time from portal '''
            df2 = pd.read_csv(io.StringIO(weather_url), encoding="utf-8", skiprows=4, nrows=0)
            col = df2.columns[0].split(' ')
            date = col[2] + " " + col[3]
            updated_datetime = datetime.datetime.strptime(date, "%d-%b-%Y %H:%M")
            try:
                weather_obj = WeatherRegionParameters.objects.get(region=self.region, parameter=self.param,
                                                                  order=order,
                                                                  last_updated_on_MONCIL=updated_datetime)
                weather_obj.last_updated_in_db = self.updated_date
                weather_obj.last_updated_on_MONCIL = updated_datetime
                weather_obj.save()
                filtered_obj = RankWiseWeatherInfo.objects.filter(weather=weather_obj).delete()
                filtered_obj = YearWiseWeatherInfo.objects.filter(weather=weather_obj).delete()
            except WeatherRegionParameters.DoesNotExist:
                weather_obj = WeatherRegionParameters.objects.create(region=self.region, parameter=self.param,
                                                                     order=order,
                                                                     last_updated_in_db=self.updated_date,
                                                                     last_updated_on_MONCIL=updated_datetime)

            base_dir = os.path.abspath(os.path.dirname(__file__))  # finding current dir path to create csv file

            path = os.path.join(base_dir, 'weather.csv')
            ''' Below line of code is used to get weather data based on provided parameters '''
            df = pd.read_csv(io.StringIO(weather_url), encoding="utf-8", skiprows=5, delim_whitespace=True)
            df = df.replace('---', 0, regex=True)
            df.to_csv(path, index=False)

            self.save_data(path, order, weather_obj)
            prepared_data = self.prepare_data_order_wise(weather_obj, order)
            weather_summary = {"region": weather_obj.region, "parameter": weather_obj.parameter,
                               "order": weather_obj.order,
                               "last_updated at Met Office National Climate Information Centre (MONCIL)":
                                   weather_obj.last_updated_on_MONCIL.strftime('%d %b %Y %H:%M %p'),
                               "weather_data": prepared_data}
            if order == "ranked":
                name = "Rank Ordered Statistics"
            else:
                name = "Year Ordered Statistics"
            dictionary[name] = weather_summary

        return dictionary

    def get_parameter_value(self):
        if self.param == "Min temp":
            category = 'Tmin'
        elif self.param == "Max temp":
            category = 'Tmax'
        elif self.param == "Mean temp":
            category = 'Tmean'
        elif self.param == "Rain days >= 1.0mm":
            category = 'Raindays1mm'
        elif self.param == "Days of air frost":
            category = 'AirFrost'
        elif self.param == "Rainfall":
            category = 'Rainfall'
        elif self.param == "Sunshine":
            category = 'Sunshine'
        else:
            category = None
        return category

    def get_region_value(self):
        if self.region == "UK":
            value = 'UK'
        elif self.region == "England":
            value = 'England'
        elif self.region == "Wales":
            value = 'Wales'
        elif self.region == "Scotland":
            value = 'Scotland'
        elif self.region == "Northern Ireland":
            value = 'Northern_Ireland'
        elif self.region == "England & Wales":
            value = 'England_and_Wales'
        elif self.region == "England N":
            value = 'England_N'
        elif self.region == "England S":
            value = 'England_S'
        elif self.region == "Scotland N":
            value = 'Scotland_N'
        elif self.region == "Scotland E":
            value = 'Scotland_E'
        elif self.region == "Scotland W":
            value = 'Scotland_W'
        elif self.region == "England E & NE":
            value = 'England_E_and_NE'
        elif self.region == "England NW/Wales N":
            value = 'England_NW_and_N_Wales'
        elif self.region == "Midlands":
            value = 'Midlands'
        elif self.region == "East Anglia":
            value = 'East_Anglia'
        elif self.region == "England SW/Wales S":
            value = 'England_SW_and_S_Wales'
        elif self.region == "England SE/Central S":
            value = 'England_SE_and_Central_S'
        else:
            value = None
        return value

    def save_data(self, path, order, weather_obj):
        df = pd.read_csv(path)
        for index, row in df.iterrows():
            if order == "ranked":
                obj = RankWiseWeatherInfo.objects.create(
                    jan=row[0],
                    jan_year=datetime.datetime.strptime(str(int(row[1])), "%Y").date() if row[1] else None,
                    feb=row[2],
                    feb_year=datetime.datetime.strptime(str(int(row[3])), "%Y").date() if row[3] else None,
                    mar=row[4],
                    mar_year=datetime.datetime.strptime(str(int(row[5])), "%Y").date() if row[5] else None,
                    apr=row[6],
                    apr_year=datetime.datetime.strptime(str(int(row[7])), "%Y").date() if row[7] else None,
                    may=row[8],
                    may_year=datetime.datetime.strptime(str(int(row[9])), "%Y").date() if row[9] else None,
                    jun=row[10],
                    jun_year=datetime.datetime.strptime(str(int(row[11])), "%Y").date() if row[11] else None,
                    jul=row[12],
                    jul_year=datetime.datetime.strptime(str(int(row[13])), "%Y").date() if row[13] else None,
                    aug=row[14],
                    aug_year=datetime.datetime.strptime(str(int(row[15])), "%Y").date() if row[15] else None,
                    sep=row[16],
                    sep_year=datetime.datetime.strptime(str(int(row[17])), "%Y").date() if row[17] else None,
                    oct=row[18],
                    oct_year=datetime.datetime.strptime(str(int(row[19])), "%Y").date() if row[19] else None,
                    nov=row[20],
                    nov_year=datetime.datetime.strptime(str(int(row[21])), "%Y").date() if row[21] else None,
                    dec=row[22],
                    dec_year=datetime.datetime.strptime(str(int(row[23])), "%Y").date() if row[23] else None,
                    win=row[24],
                    win_year=datetime.datetime.strptime(str(int(row[25])), "%Y").date() if row[25] else None,
                    spr=row[26],
                    spr_year=datetime.datetime.strptime(str(int(row[27])), "%Y").date() if row[27] else None,
                    sum=row[28],
                    sum_year=datetime.datetime.strptime(str(int(row[29])), "%Y").date() if row[29] else None,
                    aut=row[30],
                    aut_year=datetime.datetime.strptime(str(int(row[31])), "%Y").date() if row[31] else None,
                    ann=row[32],
                    ann_year=datetime.datetime.strptime(str(int(row[33])), "%Y").date() if row[33] else None,
                    weather=weather_obj,
                    last_updated=self.updated_date
                )
            else:
                obj = YearWiseWeatherInfo.objects.create(
                    year=datetime.datetime.strptime(str(int(row[0])), "%Y").date() if row[0] else None,
                    jan=row[1],
                    feb=row[2],
                    mar=row[3],
                    apr=row[4],
                    may=row[5],
                    jun=row[6],
                    jul=row[7],
                    aug=row[8],
                    sep=row[9],
                    oct=row[10],
                    nov=row[11],
                    dec=row[13],
                    win=row[13],
                    spr=row[14],
                    sum=row[15],
                    aut=row[16],
                    ann=row[17],
                    weather=weather_obj,
                    last_updated=self.updated_date
                )

    def prepare_data_order_wise(self, obj, order):
        weather_list = []
        if order == "ranked":
            filtered_data = RankWiseWeatherInfo.objects.filter(weather=obj)
            for data in filtered_data:
                dictionary = {
                    "jan": data.jan,
                    "jan_year": data.jan_year,
                    "feb": data.feb,
                    "feb_year": data.feb_year,
                    "mar": data.mar,
                    "mar_year": data.mar_year,
                    "apr": data.apr,
                    "apr_year": data.apr_year,
                    "may": data.may,
                    "may_year": data.may_year,
                    "jun": data.jun,
                    "jun_year": data.jun_year,
                    "jul": data.jul,
                    "jul_year": data.jul_year,
                    "aug": data.aug,
                    "aug_year": data.aug_year,
                    "sep": data.sep,
                    "sep_year": data.sep_year,
                    "oct": data.oct,
                    "oct_year": data.oct_year,
                    "nov": data.nov,
                    "nov_year": data.nov_year,
                    "dec": data.dec,
                    "dec_year": data.dec_year,
                    "win": data.win,
                    "win_year": data.win_year,
                    "spr": data.spr,
                    "spr_year": data.spr_year,
                    "sum": data.sum,
                    "sum_year": data.sum_year,
                    "aut": data.aut,
                    "aut_year": data.aut_year,
                    "ann": data.ann,
                    "ann_year": data.ann_year,
                    "weather_id": data.weather.id,
                    "last_updated_locally": data.last_updated
                }
                dictionary = {field: field_value if field_value is not None else "-" for field, field_value in
                              dictionary.items()}
                weather_list.append(dictionary)
        else:
            filtered_data = YearWiseWeatherInfo.objects.filter(weather=obj)
            for data in filtered_data:
                dictionary = {
                    "year": data.year,
                    "jan": data.jan,
                    "feb": data.feb,
                    "mar": data.mar,
                    "apr": data.apr,
                    "may": data.may,
                    "jun": data.jun,
                    "jul": data.jul,
                    "aug": data.aug,
                    "sep": data.sep,
                    "oct": data.oct,
                    "nov": data.nov,
                    "dec": data.dec,
                    "win": data.win,
                    "spr": data.spr,
                    "sum": data.sum,
                    "aut": data.aut,
                    "ann": data.ann,
                    "weather_id": data.weather.id,
                    "last_updated_locally": data.last_updated
                }
                dictionary = {field: field_value if field_value is not None else "-" for field, field_value in
                              dictionary.items()}
                weather_list.append(dictionary)
        return weather_list
