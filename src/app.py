import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# Sample Data
data = pd.DataFrame({
    'Year': [2019, 2020, 2021, 2022],
    'Value1': [100, 120, 90, 110],
    'Value2': [80, 110, 95, 105]
})

# Initialize the Dash app
app = dash.Dash(__name__)
server = app.server

# Layout of the Dash app
app.layout = html.Div([
    dcc.Graph(id='yearly-change-graph1'),
    dcc.Graph(id='yearly-change-graph2'),
    dcc.Slider(
        id='year-slider',
        min=data['Year'].min(),
        max=data['Year'].max(),
        value=data['Year'].min(),
        marks={str(year): str(year) for year in data['Year'].unique()},
        step=None
    )
])

# Callback to update the graphs based on the selected year
@app.callback(
    [Output('yearly-change-graph1', 'figure'),
     Output('yearly-change-graph2', 'figure')],
    [Input('year-slider', 'value')]
)
def update_figure(selected_year):
    filtered_data = data[data['Year'] == selected_year]

    trace1 = go.Bar(
        x=[selected_year],
        y=filtered_data['Value1'],
        name='Value1'
    )

    trace2 = go.Bar(
        x=[selected_year],
        y=filtered_data['Value2'],
        name='Value2'
    )

    layout1 = go.Layout(
        title=f'Value1 change over years (Year {selected_year})',
        xaxis={'title': 'Year'},
        yaxis={'title': 'Value1'},
        bargap=0.1,
        bargroupgap=0.1
    )

    layout2 = go.Layout(
        title=f'Value2 change over years (Year {selected_year})',
        xaxis={'title': 'Year'},
        yaxis={'title': 'Value2'},
        bargap=0.1,
        bargroupgap=0.1
    )

    return [{'data': [trace1], 'layout': layout1}, {'data': [trace2], 'layout': layout2}]

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
