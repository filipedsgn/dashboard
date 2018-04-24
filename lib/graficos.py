import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *

from lib import config


def grafico_linha(tipo, horas=config.GRA['spam']):
    # Quantidade de amostras no intervalo informado
    spam = (3600 / config.ADC['amostragem']) * horas

    # Adicionar erro
    df = pd.read_csv(config.ARQ['dados'], names=tipo, nrows=spam,)
    return dcc.Graph(id=
    )


class GETTING_STARTED(object):
    colors = {
        'background': '#FFFFFF',
        'text': '#506784'
    }

    app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
        html.H1(
            children='Hello Dash',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div(children='Dash: A web application framework for Python.', style={
            'textAlign': 'center',
            'color': colors['text']
        }),

        dcc.Graph(
            id='example-graph-2',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': {
                        'color': colors['text']
                    }
                }
            }
        )
    ])

    if __name__ == '__main__':
        app.run_server(debug=True)


# TODO: ver locais onde tem parenteses encapsulando objetos, desnecessariamente

class Grafico(object):
    def __init__(self):
            if tempo == '2H':
                # TODO: evitar criar variaveis
                df = pd.read_csv(config.CFG['dados'], names=['Temperatura', 'Umidade', 'Luminosidade', 'Extra'],
                                 header=0).tail(720)

            #ínicio código

        trace1 = {
            "x": [0,1,2]# TODO: DICIONARIO VALORES STRING
            "y": [0,1,2]# TODO: DICIONARIO VALORES STRING
            "connectgaps": False,
            "hoverinfo": "x+y+name",
            "line": {
                "color": "rgb(255, 127, 14)",
                "dash": "solid",
                "shape": "spline",
                "width": 2
            },
            "marker": {
                "sizemode": "area",
                "sizeref": 0.11125 # FIXME: aqui
            },
            "mode": "lines",
            "name": "Temp",
            "opacity": 1,
            "showlegend": True,
            "type": "scatter",
            "uid": "581fe5", # FIXME: aqui
            "xsrc": "FilipeDSGN:3:3a1a3e", # FIXME: aqui
            "ysrc": "FilipeDSGN:3:e034fe"  # FIXME: aqui

        }
        data = Data([trace1])
        layout = {
            "autosize": True,
            "hovermode": "x",
            "legend": {
                "x": 0, # FIXME: aqui
                "y": -0.05, # FIXME: aqui
                "borderwidth": 0,
                "orientation": "h",
                "traceorder": "normal",
                "xanchor": "left",
                "yanchor": "top"
            },
            "showlegend": False,
            "title": "Temperatura",
            "titlefont": {"size": 24},
            "xaxis": {
                "autorange": False,
                "gridwidth": 1,
                "mirror": False,
                "nticks": 0,
                "range": ["2018-04-11 23:54:55", "2018-04-11 23:59:55"], # FIXME: aqui
                "rangeselector": {
                    "bgcolor": "rgb(245, 245, 245)",
                    "borderwidth": 0,
                    "buttons": [
                        {
                            "label": "reset",
                            "step": "all"
                        },
                        {
                            "count": 30,
                            "label": "30 min",
                            "step": "minute",
                            "stepmode": "backward"
                        },
                        {
                            "count": 10,
                            "label": "10 min",
                            "step": "minute",
                            "stepmode": "backward"
                        },
                        {
                            "count": 5,
                            "label": "5 min",
                            "step": "minute"
                        }
                    ],
                    "visible": True
                },
                "showgrid": True,
                "showline": False,
                "showspikes": False,
                "showticklabels": True,
                "side": "bottom",
                "tickangle": "auto",
                "tickformat": "",
                "ticklen": 15,
                "tickmode": "auto",
                "tickprefix": "",
                "ticks": "",
                "ticksuffix": "",
                "title": "",
                "type": "date",
                "zeroline": True
            },
            "yaxis": {
                "autorange": True,
                "fixedrange": True,
                "range": [19.1111111111, 36.8888888889], # FIXME: aqui
                "showgrid": True,
                "showline": False,
                "showspikes": False,
                "showticklabels": True,
                "ticks": "",
                "title": "",
                "type": "linear",
                "zeroline": True
            },
            "yaxis2": {
                "anchor": "x",
                "autorange": True,
                "nticks": 1,
                "overlaying": "y",
                "range": [372.111111111, 1029.88888889], # FIXME: aqui
                "showticklabels": True,
                "side": "right",
                "tickangle": "auto",
                "tickmode": "auto",
                "ticks": "",
                "title": "",
                "type": "linear"
            }
        }
        fig = Figure(data=data, layout=layout)
        plot_url = py.plot(fig)

#----------------------------------------
class TESTE(object):
    app.layout = html.Div(style={'backgroundColor': 'green'},
                          children=[dcc.Graph(id='example-graph-2',
                                              figure={
                                                  'data': [{'x': [1, 2, 3], 'y': [4, 1, 2]},{'x': [1, 2, 3], 'y': [2, 4, 5]},],
                                                  'layout': {'plot_bgcolor': 'green','paper_bgcolor': 'green','font': {'color': 'green'}}
                                              })
                                    ])
    if __name__ == '__main__':
        app.run_server(debug=True)

#---------------------------------------DO SITE
<div class="dashboard__view__header__title js-dashboard-header-title" style="font-size: 1.6em; font-weight: 200;">Residência</div>
(children=[
    dcc.Graph(id'xyz', figure={data,layout})
])