# Import required libraries
import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX launch data
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create Dash app
app = dash.Dash(__name__)
app.title = "SpaceX Launch Dashboard"

# Define launch site options
site_options = [{'label': 'All Sites', 'value': 'ALL'}] + \
               [{'label': site, 'value': site} for site in spacex_df['Launch Site'].unique()]

# App layout
app.layout = html.Div([
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'fontSize': 40}),
    
    html.Div([
        html.Label("Select Launch Site:", style={'marginTop': 20}),
        dcc.Dropdown(
            id='site-dropdown',
            options=site_options,
            value='ALL',
            placeholder='Select a Launch Site',
            searchable=True,
            style={'width': '80%', 'margin': 'auto'}
        ),
    ], style={'textAlign': 'center'}),

    html.Br(),

    dcc.Graph(id='success-pie-chart'),

    html.Br(),

    html.Div([
        html.Label("Payload Range (Kg):"),
        dcc.RangeSlider(
            id='payload-slider',
            min=0,
            max=10000,
            step=500,
            marks={i: f'{i}' for i in range(0, 10001, 2500)},
            value=[min_payload, max_payload]
        ),
    ], style={'padding': '0px 40px 40px 40px'}),

    dcc.Graph(id='success-payload-scatter-chart')
])

# Callback for pie chart
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie_chart(selected_site):
    if selected_site == 'ALL':
        df_grouped = spacex_df.groupby('Launch Site')['class'].sum().reset_index()
        fig = px.pie(df_grouped, values='class', names='Launch Site',
                     title='Total Successful Launches by Site')
    else:
        df_filtered = spacex_df[spacex_df['Launch Site'] == selected_site]
        class_counts = df_filtered['class'].value_counts().reset_index()
        class_counts.columns = ['class', 'count']
        class_counts['class'] = class_counts['class'].map({1: 'Success', 0: 'Failure'})
        fig = px.pie(class_counts, values='count', names='class',
                     title=f'Success vs. Failure for site: {selected_site}')
    return fig

# Callback for scatter plot
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [Input('site-dropdown', 'value'),
     Input('payload-slider', 'value')]
)
def update_scatter_plot(selected_site, payload_range):
    df_filtered = spacex_df[spacex_df['Payload Mass (kg)'].between(payload_range[0], payload_range[1])]
    if selected_site != 'ALL':
        df_filtered = df_filtered[df_filtered['Launch Site'] == selected_site]
    fig = px.scatter(df_filtered,
                     x='Payload Mass (kg)',
                     y='class',
                     color='Booster Version Category',
                     hover_data=['Launch Site'],
                     title='Payload vs. Launch Outcome',
                     labels={'class': 'Launch Success (1=Success, 0=Failure)'})
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
