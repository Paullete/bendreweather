import _tkinter as tk
from cProfile import label
import json
from tkinter import Tk
import requests
import time

def getWeather():
    city=textfield.get()
    api ="http://api.openweathermap.org/data/2.5/weather?q="+ city +"&APPID=f5447d5c70dd98a450cc9df113a2e5a1"
    json_data=requests.get(api).json()
    
    condition = json_data['weather'][0]['main']
    temp = int(json_data ['main']['temp']-273.15)

canvas = tk.Tk()
canvas.geometry("600*500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady=20)
textfield.focus()

label1 = tk.Label(canvas, font =t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()