import dash_core_components as dcc
import pandas as pd

from lib import config
# TODO: ver locais onde tem parenteses encapsulando objetos, desnecessariamente
# TODO: spam converter para int() senão dá erro

def linha(tipo, horas=config.GRA['spam']):
    # Quantidade de amostras no intervalo informado
    spam = int((3600 / 5) * horas)

    if tipo == 'Temperatura':
        _sufixo = config.GRA['tempSuf']
        _cor = config.GRA['tempCol']
        _minimo = config.GRA['tempMin']
        _maximo = config.GRA['tempMax']

    elif tipo == 'Umidade':
        _sufixo = config.GRA['umidSuf']
        _cor = config.GRA['umidCol']
        _minimo = config.GRA['umidMin']
        _maximo = config.GRA['umidMax']

    elif tipo == 'Luminosidade':
        _sufixo = config.GRA['lumiSuf']
        _cor = config.GRA['lumiCol']
        _minimo = config.GRA['lumiMin']
        _maximo = config.GRA['lumiMax']

    else:
        _sufixo = config.GRA['extrSuf']
        _cor = config.GRA['extrCol']
        _minimo = config.GRA['extrMin']
        _maximo = config.GRA['extrMax']

    # TODO: erro quando inicia e não tem arquivo de dados no local
    df = pd.read_csv(config.ARQ['dados'], index_col=['Tempo'], usecols=['Tempo', tipo]).tail(spam)

    return dcc.Graph(id=tipo, figure={
        'data': [{"x": df.index.tolist(),
                  "y": df[tipo].tolist(),
                  "connectgaps": False,
                  "hoverinfo": "x+y+name",
                  "line": {
                      "color": _cor,
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
                   "title": tipo,
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
                       "range": [_minimo, _maximo],
                       "showgrid": True,
                       "showline": False,
                       "ticksuffix": _sufixo,
                       "showspikes": False,
                       "showticklabels": True,
                       "ticks": "",
                       "title": "",
                       "type": "linear",
                       "zeroline": True
                   }
                   }
    })