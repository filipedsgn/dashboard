import plotly.plotly as py
from plotly.graph_objs import *
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from lib import config
# TODO: ver locais onde tem parenteses encapsulando objetos, desnecessariamente

def grafico_linha(tipo, horas=1):
    # Quantidade de amostras no intervalo informado
    spam = (3600 / 5) * horas

    # TODO: Adicionar erro
    df = pd.read_csv(r'~/Documentos/backuptcc/dados.csv', index_col=['Tempo'], usecols=['Tempo', tipo]).tail(spam)
    return dcc.Graph(id=tipo, figure={
        'data': [{"x": df.index.tolist(),
                  "y": df['Temperatura'].tolist(),
                  "connectgaps": False,
                  "hoverinfo": "x+y+name",
                  "line": {
                      "color": config.GRA['tempCol'],
                      "dash": "solid",
                      "shape": "spline",
                      "width": 2
                  },
                  "marker": {
                      "sizemode": "area",
                      "sizeref": 0.11125  # FIXME: aqui
                  },
                  "mode": "lines",
                  "name": "Temp",
                  "opacity": 1,
                  "showlegend": True,
                  "type": "scatter"
                  }],
        'layout': {"autosize": True,
                   "hovermode": "x",
                   "legend": {
                       "x": 0,
                       "y": -0.05,
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
                       "autorange": True,
                       "gridwidth": 1,
                       "mirror": False,
                       "nticks": 0,
                       "range": '',
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
                       "range": [config.GRA['tempMin'], config.GRA['tempMax']],  # FIXME: aqui
                       "showgrid": True,
                       "showline": False,
                       "showspikes": False,
                       "showticklabels": True,
                       "ticks": "",
                       "title": "",
                       "type": "linear",
                       "zeroline": True
                   }
                   }
    })


app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    grafico_linha('Temperatura', 1)
])

if __name__ == '__main__':
    app.run_server(debug=True)
