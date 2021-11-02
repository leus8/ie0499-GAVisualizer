#!/usr/bin/python

# library imports
import pandas as pd
import plotly.graph_objects as go
import dash_table
from dash import Dash, dcc, html, Input, Output

from collections import deque

X = deque(maxlen=20)
Y = deque(maxlen=20)
X.append(1)
Y.append(1)

# app declaration
app = Dash(__name__)

# set the color theme
theme = {
    'dark': True,
    'detail': '#007439',
    'primary': '#00EA64',
    'secondary': '#6E6E6E',
}

# reads the results.csv file data
df = pd.read_csv("../segmentation/results.csv", sep=',', header=0)

# extracts the data by column
generacion = df["Generacion"]
apt_promedio = df["Aptitud promedio"]
mejor_aptitud = df["Mejor Aptitud"]
seg_mejor_aptitud = ["Segunda Mejor Aptitud"]
desv_std = df["Desviacion estandar"]
duracion_prom = df["Duracion Promedio"]
cant_seg = df["Cantidad de segmentos"]
silencio = df["Silencio"]
sonido = df["Sonido"]
umbral = df["Umbral"]

# App layout
app.layout = html.Div([

    html.H1("Evolución del algoritmo genético", style={'text-align': 'center'}),

    html.Div([
        dash_table.DataTable(
            id='datatable_id',
            data=df.to_dict('records'),
            columns=[
                {"name": i, "id": i, "deletable": False, "selectable": False} for i in df.columns
            ],
            editable=True,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            row_selectable="multi",
            row_deletable=True,
            selected_rows=[],
            # page_action="native",
            # page_current= 0,
            # page_size= 6,
            page_action='none',
            style_cell={
            'whiteSpace': 'normal'
            },
            fixed_rows={ 'headers': True, 'data': 0 },
            virtualization=False,
            style_cell_conditional=[
                {'if': {'column_id': 'Generacion'},
                'width': '10%', 'textAlign': 'left'},
                {'if': {'column_id': 'Aptitud promedio'},
                'width': '10%', 'textAlign': 'left'},
                {'if': {'column_id': 'Mejor Aptitud'},
                'width': '10%', 'textAlign': 'left'},
                {'if': {'column_id': 'Segunda Mejor Aptitud'},
                'width': '10%', 'textAlign': 'left'},
                {'if': {'column_id': 'Desviacion estandar'},
                'width': '10%', 'textAlign': 'left'},
                {'if': {'column_id': 'Duracion Promedio'},
                'width': '10%', 'textAlign': 'left'},
                {'if': {'column_id': 'Cantidad de segmentos'},
                'width': '10%', 'textAlign': 'left'},
                {'if': {'column_id': 'Silencio'},
                'width': '10%', 'textAlign': 'left'},
                {'if': {'column_id': 'Sonido'},
                'width': '10%', 'textAlign': 'left'},
                {'if': {'column_id': 'Umbral'},
                'width': '10%', 'textAlign': 'left'},
            ],
        ),
    ],className='row'),

    html.Br(),
    html.Br(),

    dcc.Dropdown(id="slct_metric",
                options=[
                    {"label": "Aptitud promedio", "value": "Aptitud promedio"},
                    {"label": "Mejor aptitud", "value": "Mejor Aptitud"},
                    {"label": "Segunda mejor aptitud", "value": "Segunda Mejor Aptitud"},
                    {"label": "Desviación estándar", "value": "Desviacion estandar"},
                    {"label": "Duración promedio", "value": "Duracion Promedio"},
                    {"label": "Cantidad de segmentos", "value": "Cantidad de segmentos"},
                    {"label": "Silencio", "value": "Silencio"},
                    {"label": "Sonido", "value": "Sonido"},
                    {"label": "Umbral", "value": "Umbral"}],
                multi=False,
                value="Mejor Aptitud",
                style={'width': "70%"}
                ),

    dcc.Graph(id='algorithm_graph', animate=True, figure={}),

    dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )

])

# ------------------------------------>
# Interactive dropdown menu with graph
@app.callback(
    Output(component_id='algorithm_graph', component_property='figure'),
    Input(component_id='slct_metric', component_property='value'), Input('interval-component','n_intervals')
)

def update_graph(option_slctd, dff):
    dff = pd.read_csv("../segmentation/results.csv", sep=',', header=0)
    generacion = dff["Generacion"]
    y_selected = dff[option_slctd]

    fig = go.Figure(
        go.Scatter(
            x=generacion,
            y=y_selected,
        )
    )

    return fig
# ------------------------------------>

# ------------------------------------>
# real-time table update
@app.callback(
    Output('datatable_id', 'data'),
    Input('interval-component','n_intervals')
)

def update_table(n):
    df = pd.read_csv("../segmentation/results.csv", sep=',', header=0)
    return df.to_dict('records')
# ------------------------------------>


if __name__ == '__main__':
    app.run_server(debug=True)

    # uncomment for public access from same wifi.
    # app.run_server(debug=True, host='0.0.0.0', port = 8080)