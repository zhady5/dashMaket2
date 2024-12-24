from dash import dcc, html
import dash_bootstrap_components as dbc

def create_layout(data):
    return html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1('Telegram Channel Analytics Dashboard', className='text-center mb-4'),
                    dcc.Dropdown(
                        id='channel-dropdown',
                        options=[{'label': c, 'value': c} for c in data['posts']['channel_name'].unique()],
                        value=data['posts']['channel_name'].unique()[0],
                        clearable=False,
                        className='mb-4'
                    )
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='publication-trend-graph')
                ], width=6),
                dbc.Col([
                    dcc.Graph(id='subscriber-growth-graph')
                ], width=6)
            ]),
            dbc.Row([
                dbc.Col([
                    html.H4('Channel Metrics', className='text-center'),
                    dbc.Row([
                        dbc.Col([
                            html.Div(id='mean-subs-pos'),
                            html.Div(id='mean-subs-neg'),
                            html.Div(id='max-subs-pos'),
                            html.Div(id='max-subs-neg')
                        ], width=3),
                        dbc.Col([
                            html.Div(id='mean-posts-day'),
                            html.Div(id='mean-posts-week'),
                            html.Div(id='mean-posts-month')
                        ], width=3),
                        dbc.Col([
                            html.Div(id='mean-views'),
                            html.Div(id='mean-reacts'),
                            html.Div(id='mean-idx')
                        ], width=3),
                        dbc.Col([
                            html.Div(id='top-reactions')
                        ], width=3)
                    ])
                ])
            ]),
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='publication-heatmap')
                ], width=6),
                dbc.Col([
                    dcc.Graph(id='subscriber-change-graph'),
                    dcc.RangeSlider(
                        id='date-slider',
                        min=0,
                        max=100,
                        step=1,
                        value=[0, 100],
                        marks={0: {'label': 'Start'}, 100: {'label': 'End'}},
                        className='mt-4'
                    )
                ], width=6)
            ]),
            dbc.Row([
                dbc.Col([
                    html.H4('Post Performance Analysis', className='text-center'),
                    dcc.Slider(
                        id='hours-slider',
                        min=1,
                        max=72,
                        step=1,
                        value=24,
                        marks={i: str(i) for i in range(0, 73, 12)},
                        className='mb-4'
                    ),
                    html.Div(id='post-performance-table')
                ])
            ])
        ], fluid=True)
    ])

