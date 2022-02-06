import requests
import datetime
from datetime import date

api_key = "your_api"  # change here
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def main():
    text = weather_of_the_day()
    # open and write on file
    path = "G:/Il mio Drive/Vault0.1/Daily Notes/"
    today = date.today()
    filename = today.strftime("%Y-%m-%d")+".md"
    file = open(path + filename, "a+", encoding='utf-8')
    file.write(text)
    file.close()


def weather_of_the_day():
    city_1 = 'trento'
    city_2 = 'valdagno'
    api_key = "your_api"  # change here
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_1
    response = requests.get(complete_url)
    x = response.json()

    complete_url = base_url + "appid=" + api_key + "&q=" + city_2
    response = requests.get(complete_url)
    z = response.json()

    if x["cod"] != "400" and z["cod"] != "404":
        y = x["main"]
        city1_current_temperature = round(y["temp"]-273.15, 1)
        city1_current_pressure = y["pressure"]
        city1_current_humidity = y["humidity"]
        city1_weather_description = x["weather"][0]["description"]
        city1_image = x["weather"][0]["icon"]
        city1_img_link = "http://openweathermap.org/img/wn/" + \
            str(city1_image)+"@2x.png"

        y = z["main"]
        city2_current_temperature = round(y["temp"]-273.15, 1)
        city2_current_pressure = y["pressure"]
        city2_current_humidity = y["humidity"]
        city2_weather_description = z["weather"][0]["description"]
        city2_image = z["weather"][0]["icon"]
        city2_img_link = "http://openweathermap.org/img/wn/" + \
            str(city2_image)+"@2x.png"

        now = datetime.datetime.now()
        date_it = convert_day_name(now.strftime("%A")).decode(
        )+now.strftime(" %d ")+convert_month_name(now.strftime("%B")).decode()+now.strftime(" %Y ")
        weather_table = "\n<table style = 'border-style:hidden'>\n 	<tr>\n		<td style = 'border-style:hidden'>"+date_it+"</td>\n		<td style = 'border-style:hidden'></td>\n		<td style = 'border-style:hidden'>" + \
            str(city1_current_temperature)+" °C</td>\n		<td  style = 'border-style:hidden'><img src='" + \
            city1_img_link+"' height=50px></td>\n		<td style = 'border-style:hidden'>" + \
            str(city2_current_temperature)+" °C</td>\n		<td  style = 'border-style:hidden'><img src='" + \
            city2_img_link+"' height=50px></td>\n	</tr>\n</table>\n\n"

        return weather_table

    else:
        print(" City Not Found ")


def convert_day_name(day):
    match day:
        case 'Monday':
            day = 'Lunedì'
        case 'Tuesday':
            day = 'Martedì'
        case 'Wednesday':
            day = 'Mercoledì'
        case 'Thursday':
            day = 'Giovedì'
        case 'Friday':
            day = 'Venerdì'
        case 'Saturday':
            day = 'Sabato'
        case 'Sunday':
            day = 'Domenica'
    return day.encode()


def convert_month_name(month):
    match month:
        case 'Genuary':
            month = 'Gennaio'
        case 'February':
            month = 'Febbraio'
        case 'March':
            month = 'Marzo'
        case 'April':
            month = 'Aprile'
        case 'May':
            month = 'Maggio'
        case 'June':
            month = 'Giugno'
        case 'July':
            month = 'Luglio'
        case 'August':
            month = 'Agosto'
        case 'September':
            month = 'Settembre'
        case 'October':
            month = 'Ottobre'
        case 'November':
            month = 'Novembre'
        case 'December':
            month = 'Dicembre'

    return month.encode()


if __name__ == "__main__":
    main()
