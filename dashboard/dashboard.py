#!/usr/bin/python

# library imports
from os import name
import pandas as pd
import plotly.graph_objects as go
import dash_table
from dash import Dash, dcc, html, Input, Output



# app declaration
app = Dash(__name__)

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

    # define titulo de la interfaz
    html.H1("Interfaz de visualización de resultados de la evolución del algoritmo genético", style={'text-align': 'center'}),

    html.Div([
        "Seleccione el parámetro del eje Y en la gráfica..."
    ]),

    # define el menu desplegable
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
                style={'width': "50%"}
    ),

    # define el area del grafico
    dcc.Graph(id='algorithm_graph', animate=False, figure={}),

    # define la tabla de datos que lee del archivo results.csv
    html.Div([
        "Tabla con los datos contenidos en el archivo results.csv",
        dash_table.DataTable(
            id='datatable_id',
            data=df.to_dict('records'),
            columns=[
                {"name": i, "id": i, "deletable": False, "selectable": False, 'type':'numeric', 'format':{'specifier':'.2f'}} for i in df.columns
            ],
            editable=True,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            row_selectable=False,
            row_deletable=False,
            selected_rows=[],
            # page_action="native",
            # page_current= 0,
            # page_size= 1,
            page_action='none',
            style_cell={
                'whiteSpace': 'normal'
            },
            fixed_rows={ 'headers': True, 'data': 0 },
            virtualization=False,
            style_cell_conditional=[
                {'if': {'column_id': 'Generacion'},
                'width': '10%', 'textAlign': 'center'},
                {'if': {'column_id': 'Aptitud promedio'},
                'width': '10%', 'textAlign': 'center'},
                {'if': {'column_id': 'Mejor Aptitud'},
                'width': '10%', 'textAlign': 'center'},
                {'if': {'column_id': 'Segunda Mejor Aptitud'},
                'width': '10%', 'textAlign': 'center'},
                {'if': {'column_id': 'Desviacion estandar'},
                'width': '10%', 'textAlign': 'center'},
                {'if': {'column_id': 'Duracion Promedio'},
                'width': '10%', 'textAlign': 'center'},
                {'if': {'column_id': 'Cantidad de segmentos'},
                'width': '10%', 'textAlign': 'center'},
                {'if': {'column_id': 'Silencio'},
                'width': '10%', 'textAlign': 'center'},
                {'if': {'column_id': 'Sonido'},
                'width': '10%', 'textAlign': 'center'},
                {'if': {'column_id': 'Umbral'},
                'width': '10%', 'textAlign': 'center'},
            ],
        ),
    ],className='row'),

    # html.Br(),
    # html.Br(),

    # Informacion de la interfaz y su uso
    html.Div([
        html.Center(html.H3('Uso de la interfaz')),
    ]),

    dcc.Markdown(
        
        '''
        La interfaz cuenta con tres componentes principales: una tabla de datos, un menú desplegable y una gráfica.

        #### Uso de la tabla de resultados

        Corresponde al primer elemento de la interfaz (el que se encuentra más arriba).

        La tabla permite visualizar los datos de entrada de una mejor manera, entre las interacciones que tiene está un espacio de filtrado al inicio de cada columna se observa como una entrada con el nombre Filter data.

        Su formato es el siguiente: <expresión> <valor> Ej: > 2021 muestra en la columna ingresada los valores mayores a 2021. Algunas expresiones son <,>,= y != (distinto a).

        #### Uso del menú desplegable y la gráfica

        El segundo elemento que se puede observar (en el medio).

        Este menú desplegable permite seleccionar los datos del eje Y, de la gráfica que es el tercer elemento de la interfaz (el de más abajo).

        La gráfica permite visualizar de manera más simple e intuitiva la evolución de los parámetros de desempeño para cada generación.

        Al realizar un cambio con el menú desplegable se debe dar al noveno botón (al colocar el cursor sobre este aparece la palabra Autoscale) para ajustar y actualizar los ejes de la gráfica.

        La gráfica cuenta además con una barra de herramientas en su esquina superior derecha, de izquierda a derecha se irá describiendo cada una de ellas:

        * El primer icono permite guardar la gráfica en el computador del usuario en formato PNG.

        * El segundo permite hacer zoom a un área seleccionada.

        * El tercero permite desplazarse dentro de la gráfica.

        * El cuarto corresponde a un seleccionador en forma cuadrada.

        * El quinto es un seleccionador de tipo lazo, que tiene una forma de selección más libre que el basado en cuadros.

        * El sexto es aumentar el zoom en la gráfica pero de forma general y no en una sola área.

        * El séptimo es lo mismo que lo anterior pero para reducir el zoom sobre la gráfica.

        * El octavo permite auto ajustar la escala de los ejes de la gráfica.

        * El noveno permite reiniciar los ejes.

        * El último es información acerca del desarrollador del framework

        ### Acerca de la interfaz

        Esta interfaz de visualización de resultados de algoritmos genéticos fue desarrollada por el estudiante Leonardo Agüero para el curso IE-0499 - Proyecto Eléctrico.

        El segmentador utilizado fue desarrolado por Natalia Bolaños Murillo.

        '''
        
    ),


    # define el intervalo de actualizacion de los datos
    dcc.Interval(
        id='interval-component',
        interval=1*1000, # en milisegunos
        n_intervals=0
    )

])

# ------------------------------------>
# Grafica con menu desplegable para selecionar metricas
@app.callback(
    Output(component_id='algorithm_graph', component_property='figure'),
    Input(component_id='slct_metric', component_property='value'), Input('interval-component','n_intervals')
)

def update_graph(option_slctd, dff):

    # se lee los datos del csv
    dff = pd.read_csv("../segmentation/results.csv", sep=',', header=0)

    # se lee para x los datos de generacion y y con base en el dropdown
    generacion = dff["Generacion"]
    y_selected = dff[option_slctd]

    # se genera la grafica
    fig = go.Figure(
        go.Scatter(
            x = generacion,
            y = y_selected,
        )
    )

    # se actualiza el titulo y eje-y con base en el dropdown
    fig.update_layout(
        title={
        'text': option_slctd + " en función de la generación",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        xaxis_title = "Generación",
        yaxis_title = option_slctd,
    )

    return fig

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

    # en 0 se correr privado, en 1 publico
    public = 0
    if (public): app.run_server(host="0.0.0.0", port="8050") # de forma publica
    else: app.run_server(debug=True) # de forma privada