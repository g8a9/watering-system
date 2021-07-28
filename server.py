# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__)


def create_fig():
    df = pd.read_csv("moisture.csv", header=None, index_col=0, parse_dates=True)
    df.columns = ["Sensor Value", "Moisture (%)"]
    df.index.name = "Date"

    fig = px.line(df, y="Moisture (%)")
    fig.update_layout(title="Soil moisture over time")
    return fig

fig = create_fig()

app.layout = html.Div(children=[
    html.H1(children='Hypa monitoring'),
    dcc.Graph(
        id='moisture_chart',
        figure=fig
    ),
    html.Button("Refresh", id="refresh_button")
])


@app.callback(
    Output("moisture_chart", "figure"),
    [Input("refresh_button", "n_clicks")]
)
def update_chart(n_clicks):
    return create_fig()


if __name__ == '__main__':
        app.run_server(debug=True, host="0.0.0.0")
