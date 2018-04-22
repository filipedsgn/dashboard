import pandas as pd
import plotly.plotly as py
from plotly.graph_objs import *

from lib import config



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