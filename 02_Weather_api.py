import requests
import json
import win32com.client # adding text to speech

city = input("Enter your city name:\n")

speaker = win32com.client.Dispatch("SAPI.SpVoice") # assigning speaker

url = f"http://api.weatherapi.com/v1/current.json?key=4569af98a4d148b7a9a61146242810&q={city}"

req = requests.get(url)

formatter = json.loads(req.text)

say = formatter["current"]["temp_c"]

speaker.speak(say)