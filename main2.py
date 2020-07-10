import json
import pandas as pd
import dash
import psutil
import dash_core_components as dcc
import plotly.graph_objects as go
import requests

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

with open('weather-reformat.json', encoding="utf-8") as f:
    data = json.load(f)
    df = pd.json_normalize(data)
    df_sample = df.sample(frac = 1, replace=True, random_state=1)#(n=100, random_state=1)
    # df_sample = df.sample(n=10, random_state=1)
    df_gb = df[df['city.country'] == "GB"]
    df_pt = df[df['city.country'] == "PT"]
    df_gb_sample = df_gb.sample(n=3000, random_state=1)
    df_pt_sample = df_pt.sample(n=3000, random_state=1)

    pt = df_gb_sample["time"].value_counts()
    dt = df_pt_sample["time"].value_counts()
    print("hi")
    # df_sample = df_gb.sample(n=25, random_state=1)
    # df_sample = df_sample.sort_values(by = ["wind.speed"])

    # df_time_mode = df["time"].value_counts()
    # df_timestamp = df[df['city.country']=="GB"]
    # df_wind_iqr= df["time"].value_counts()




# fig = go.Figure(data=go.Choropleth(
#     locations=df['code'], # Spatial coordinates
#     z = df['total exports'].astype(float), # Data to be color-coded
#     locationmode = 'USA-states', # set of locations match entries in `locations`
#     colorscale = 'Reds',
#     colorbar_title = "Millions USD",
# ))
#
# fig.update_layout(
#     title_text = '2011 US Agriculture Exports by State',
#     geo_scope='usa', # limite map scope to USA
# )


# fig = go.Figure([go.Bar(x=df_sample["city.name"], y=df_sample["wind.speed"])])

# fig = go.Figure(data=[go.Histogram(x=df_gb["wind.speed"], histnorm='probability')])
fig = go.Figure()
fig.add_trace(go.Histogram(x=df_gb_sample["wind.speed"]))#, histnorm='probability'))
fig.add_trace(go.Histogram(x=df_pt_sample["wind.speed"]))#, histnorm='probability'))

# The two histograms are drawn on top of another
fig.update_layout(barmode='overlay')
# Reduce opacity to see both histograms
fig.update_traces(opacity=0.75)
# fig = go.Figure(go.Densitymapbox(lat= df['city.coord.lat'], lon=    df['city.coord.lon'], z=    df['wind.speed'],
#                                  radius=1))
# fig.update_layout(mapbox_style="stamen-terrain")#, mapbox_center_lon=180)
# fig.update_layout(width=1920,
#     height=1080)
# fig.update_layout(
#     title_text = '2011 US Agriculture Exports by State',
# )


#margin={"r":-100,"t":-100,"l":-100,"b":100})
# fig.update_layout(
#     autosize=True)

# fig = go.Figure()
# fig.add_trace(go.Scattergeo(
#     # locationmode = 'USA-states',
#     lon=df_sample['city.coord.lon'],
#     lat=df_sample['city.coord.lat'],
#     text=df_sample['city.name'],
#     marker=dict(
#         size=df_sample['wind.speed'], #/ scale,
#         # color = colors[i],
#         line_color='rgb(40,40,40)',
#         line_width=0.5,
#         sizemode='area'
#     ),
#     name='{0} - {1}'))  # .format(lim[0],lim[1])))



# app.layout = dcc.Graph(
#         id='example-graph',
#         figure=fig
#     )


if __name__ == '__main__':
    fig.write_image("fig1.png")
    fig.write_image("fig1.svg")
    fig.write_image("fig1.pdf")

    # print("wind speed:" + df[df['wind']=="GB"])


    # app.run_server(debug=True)
