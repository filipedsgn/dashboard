from lib import config, graficos

import plotly.plotly as py
from plotly.graph_objs import *
import dash
import dash_core_components as dcc
import dash_html_components as html
from flask import send_from_directory
import os
from threading import Thread


class siteApp(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        app = dash.Dash()

        # Utilização de formatação de página de web com arquivos locais
        app.css.config.serve_locally = True
        app.scripts.config.serve_locally = True

        def homepage():
            return html.Div([
                html.Link(rel='stylesheet', href='/static/stylesheet.css'),
                html.Div(children="Residência", className="header"),
                html.Div(children=graficos.linha('Temperatura'), className="g1"),
                html.Div(children=graficos.linha('Umidade'), className="g2"),
                html.Div(children=graficos.linha('Luminosidade'), className="g3"),
                html.Div(children=graficos.linha('Extra'), className="g4")
            ], className="wrapper")

        # Cria metódo, para carregar dados novos em carregamento de página
        app.layout = homepage()

        # Método para utilização de arquivos de formatação de página utilizando arquivos locais
        @app.server.route('/static/<resource>')
        def serve_static(resource):
            return send_from_directory(config.ARQ['static'], resource)

        app.run_server(host='0')
