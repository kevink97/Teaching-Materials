import requests

# gets the weather data on the zip code specified and returns it in json format
def get_data(zipcode):
    payload = {'zip': zipcode, 'units': 'imperial', 'appid': 'b73db8c0f065450acf87c6598cbfd37c', 'cnt': '16'}
    r = requests.get('http://api.openweathermap.org/data/2.5/forecast/daily', params=payload)
    if r.status_code != 200:
        print('problem getting data')
        exit()
    json = r.json()
    return json

# returns a tuple (temp, forecast) for 16 days
def get_temp_forecast(zipcode):
    data = get_data(zipcode)
    temp = list()
    forecast = list()
    res = data['list']
    for day in res:
        forecast.append(day['weather'][0]['description'])
        temp.append(float(day['temp']['day']))
    return (temp, forecast)

# returns just the temperature
def get_temp(zipcode):
    return get_temp_forecast(zipcode)[0]

# returns just the forecast
def get_forecast(zipcode):
    return get_temp_forecast(zipcode)[1]
