import requests
import json

requestSuccessful = False
while(requestSuccessful == False):
    print("In which city do you live?")
    city = input()
    url = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=8c4734cc2af49e2c60f07a7768efc391"

    response = requests.get(url)
    data = json.loads(response.text)
    cod = response.json()
    if(cod["cod"] != "404"):
        kelvin = data['main']['temp']
        farenheit = int((kelvin-273.15)*1.8+32.0)
        celsius = int(kelvin-273.15)
        print("The weather in " + data['name'] + ", " + data['sys']['country'] + " is " + data['weather'][0]['description'] + " and it's " + str(farenheit) + "°F (" + str(celsius) + "°C) outside")
        print("Do you want to continue? (Y/N)")
        answer = input()
        if(answer.lower() != 'y'):
            print("Goodbye!")
            requestSuccessful = True
    else:
        print("OpenWeatherMap doesn't know your city")
    


