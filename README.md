# weather_data_scrapping
Scrapping Weather data and provide through API to UI side for UK regions based on user provided parameters

REST-API-in-Django-using-Django-REST-Framework.

Clone this Projects by using below link
https://github.com/mahadikrushikesh/weather_data_scrapping.git

Main Version
Python3.7  
Django 3.2

Install requirements:
pip install -r requirements.txt

Apply Migrations:

python manage.py makemigrations
python manage.py migrate

Create Superuser to check table structure and add dummy data through Admin Panel:
python manage.py createsuperuser

This is an example project to illustrate an implementation of weather data scrapping for UK based all regions and parameters 
by ordering year and rank wise weather data based on user API request.


Want to Provide different regions and parameters, can select in list of Regions and Parameters over API payload
    please do changes in 'region' and 'parameters' for different results 


Note:
   Currently "Order" parameter is not taking from User Input it has been handled from backend for both "Rank" and "Year" 
   wise every successful request. 

if code run successfully it will generate weather.csv file and will give result through API
API local URL:
 http://127.0.0.1:8000/weather/download_weather_data/


Future works needs to be done for better performance and user experience:
    1)  Can use Scrappy Module Framework for scrapping large amount data so, multiple requests and code efficiently work.
    2)  We can use request sessions, to reduce getting loss of requests access and to get re-gain access.
    3)  In Model Table Fields needs to renamed for better understanding.
    4)  Response keys need to be changed by understanding Functional things.
    5)  Additional, if we added loggers to keep track over error logs if code break.
    6)  Designing and integrating API with Frontend 

