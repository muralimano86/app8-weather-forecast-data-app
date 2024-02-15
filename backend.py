import requests

API_KEY = "141710af2113bab9f55ef73e1bcd33d5"

def get_data(place, forecast_days=None, kind=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__=="__main__":
    print(get_data("Tokyo"))