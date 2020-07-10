import json
from datetime import datetime

import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np

# {"city":{"id":14256,"name":"Azadshahr","findname":"AZADSHAHR","country":"IR","coord":{"lon":48.570728,"lat":34.790878},"zoom":10},"time":1554462304,"main":{"temp":287.07,"pressure":1022,"humidity":71,"temp_min":284.15,"temp_max":289.15},"wind":{"speed":4.1,"deg":340},"clouds":{"all":90},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}]},

#   city
# id #name # findname# country # coordinates #time,
#
#Interesting questions?
# Is there a relationship between wind speeds and

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#
with open('weather-reformat.json', encoding="utf-8") as f:
    data = json.load(f)
    test = pd.json_normalize(data)
    df = pd.DataFrame(test)
    print("hi")


test = pd.read_json('weather-reformat.json', orient='records')
test2 = pd.json_normalize(test)
print("hi")

def printContent(content, data):
    if content == "all":
        for record in data:
            print(record)

    if content == "city":
        for record in data:
            print(record["city"])
    if content == "time":
        # for idx, record in enumerate(data):
        print(df["time"].mode())
    if content == "main":
        for record in data:
            print(record["main"])
    if content == "wind":
        for record in data:
            print(record["wind"])
    if content == "clouds":
        for record in data:
            print(record["clouds"])
    if content == "weather":
        for record in data:
            print(record["weather"])
    if content == "country":
        for record in data:
            print(str(record["wind"]["speed"]) + " " + str(record["wind"]["deg"]))


# timelist = []
# templist = []
# timelist_str = []
# for record in data:
#     timelist.append(record["time"])
#     templist.append(record["main"]["temp"])
#
# timelistlist_str = []
# for x in timelist:
#     y = datetime.fromtimestamp(x).strftime('%d/%m/%Y %H:%M:%S')
#     timelist_str.append(y)

# wind_speed = []
# temp_list = []
# for record in data:
#     wind_speed.append(record["wind"]["speed"])
#     temp_list.append(record["main"]["temp"])
#
# temp_list_celcius = []
# y = 273
# for x in temp_list:
#     x = x - y
#     temp_list_celcius.append(x)
#
#
#
# # fig = go.Figure(data=[go.Scatter(x=wind_speed, y=temp_list_celcius,  mode='markers')])
# fig = go.Figure(data=[go.Histogram(x=temp_list_celcius)])
#
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_us_cities.csv')
# # df = pd.read_json("weather-reformat.json", index)
# df.head()
#


if __name__ == '__main__':
    # print("hi")
    # app.run_server(debug=True)
    printContent("time", data)
    # df[df.duplicated(keep=False)]



