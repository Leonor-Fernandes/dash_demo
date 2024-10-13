import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html

df=pd.read_csv('sample_df_20241013.csv')

#plot histogram
fig = px.histogram(df, x='distrito')

#plot bar
agg=df.groupby(['distrito']).agg({'valor-compra':'median'}).reset_index().dropna(subset=['valor-compra'])
fig_bar = px.bar(agg, x='distrito', y='valor-compra')


app = Dash()
server = app.server

app.layout = html.Div([
    dcc.Graph(figure=fig),
    dcc.Graph(figure=fig_bar)
])

app.run_server(debug=True, use_reloader=False)


