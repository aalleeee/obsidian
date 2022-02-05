import requests, json
from datetime import date
 
api_key = "your_api" #change here
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
#city_name = input("Enter city name : ")
city_name = "valdagno"
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)
x = response.json()
 
if x["cod"] != "404":
    y = x["main"]
    current_temperature = round(y["temp"]-273.15,1)
    current_pressure = y["pressure"]
    current_humidity = y["humidity"]
    weather_description = x["weather"][0]["description"]
    image = x["weather"][0]["icon"]

    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature)+"°C"+chr(167)+
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidity) +
          "\n description = " +
                    str(weather_description) +
		  "\n image = " +
					str(image))
	
    img_link = "http://openweathermap.org/img/wn/"+str(image)+"@2x.png"
    weather_string = "\n\n## Weather\n<b>Temperature:</b> "+ str(current_temperature)+"°C"+"\n<b>Weather:</b> "+ str(weather_description)+ "\n![]("+img_link+")"

    weather_table = "\n\n<table style = 'border-style:hidden'>\n 	<tr>\n		<td style = 'border-style:hidden'>Mercoledì 2 Febbraio 2022</td>\n		<td style = 'border-style:hidden'>"+str(current_temperature)+"</td>\n		<td style ='border-style:hidden'>"+str(weather_description)+"</td>\n		<td  style = 'border-style:hidden'><img src='"+img_link+"' height=50px></td>\n	</tr>\n</table>\n"
					
    print("-----------------------------------")
    print(weather_table)
    path = "G:/Il mio Drive/Vault0.1/Daily Notes/"
    today = date.today()
    filename = today.strftime("%Y-%m-%d")+".md"
    #print(filename)
    file = open(path + filename,"a")
    file.write(weather_table)
    file.close()
 
else:
    print(" City Not Found ")
	

	
