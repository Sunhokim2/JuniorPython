import requests

#날씨API
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
#해당사이트에 회원가입을 하고 api key 발급을 받아야 가능합니다.
api_key = ""

weather_params = { #위치는 인천
    "lat" : 37.424707,
    "lon": 126.726769,
    "appid": api_key,
    "exclude": "current, minutely,daily"
}

response = requests.get(OWM_Endpoint, params = weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
#날씨id를 불러온다

will_rain = False
for hour_datra in weather_slice:
    condition_code = hour_datra["weather"][0]["id"]
    #id가 700보다 낮으면 우천,눈 등 하늘에서 뭐가 내리는것이다.
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("우산챙기세요")
