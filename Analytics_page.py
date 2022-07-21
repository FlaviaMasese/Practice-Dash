from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_trich_components as dtc
from Stylee import cardbody_style, card_icon, cardimg_style, card_style
from helping_components import output_card
import pandas as pd
from datar.all import case_when, f, mutate, pivot_wider
from Data import LSMS_df
from Data import LSMS2_df

expend_page = html.Div([
    dbc.Row(
            children=[ 
                    dbc.Col(lg=1),
                    dbc.Col(lg=2, #style={'marginRight': '2%'},
                            children=[
                                dbc.Label('Select State'),
                                dcc.Dropdown(id='state_dropdown',
                                                options=[{'label': state, 'value': state}
                                                        for state in LSMS_df['state_name'].unique()
                                                        ],
                                                placeholder='Select states'
                                                )
                            ]
                        
                    ),
                    dbc.Col(lg=9,
                            children=[
                                    dbc.Row(
                                            children=[
                                                        dbc.Row(
                                                                children=[
                                                                    dbc.Col(
                                                                        dbc.CardGroup(
                                                                            children=[
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.H3(id='avg_expense'
                                                                                                    ),
                                                                                            html.P('Average Expenditure')
                                                                                        ]
                                                                                    ),
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className='bi bi-cash-coin',
                                                                                                style=card_icon
                                                                                            )
                                                                                        ],
                                                                                        style={"backgroundColor": 'yellow'}
                                                                                )
                                                                            ]
                                                                        )
                                                                    ),
                                                                    dbc.Col(
                                                                        dbc.CardGroup(
                                                                            children=[
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.H3(id='avg2',
                                                                                                    children='50'
                                                                                                    ),
                                                                                            html.P('Average Min Expenditure')
                                                                                        ]
                                                                                    ),
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className='bi bi-cash-coin',
                                                                                                style=card_icon
                                                                                            )
                                                                                        ],
                                                                                        style={"backgroundColor": 'yellow'}
                                                                                )
                                                                            ]
                                                                        )
                                                                        ),
                                                                    dbc.Col(
                                                                        dbc.CardGroup(
                                                                            children=[
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.H3(id='avg3',
                                                                                                    children='50'
                                                                                                    ),
                                                                                            html.P('Average Max Expenditure')
                                                                                        ]
                                                                                    ),
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className='bi bi-cash-coin',
                                                                                                style=card_icon
                                                                                            )
                                                                                        ],
                                                                                        style={"backgroundColor": 'yellow'}
                                                                                )
                                                                            ]
                                                                        )
                                                                    )
                                                                    
                                                                ]
                                                            ),
                                                        #html.Br(), html.Br(), html.Br(),
                                                        html.Hr(),
                                                        dbc.Row(
                                                                children=[
                                                                    dbc.Col(
                                                                        dbc.CardGroup(
                                                                            children=[
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.H3(id='cred1',
                                                                                                    children='50'
                                                                                                    ),
                                                                                            html.P('Average Income Earning')
                                                                                        ]
                                                                                    ),
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className='bi bi-cash-coin',
                                                                                                style=card_icon
                                                                                            )
                                                                                        ],
                                                                                        style={"backgroundColor": 'yellow'}
                                                                                )
                                                                            ]
                                                                        )
                                                                        ),
                                                                    dbc.Col(
                                                                        dbc.CardGroup(
                                                                            children=[
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.H3(id='cred2',
                                                                                                    children='50'
                                                                                                    ),
                                                                                            html.P('Income Min earning')
                                                                                        ]
                                                                                    ),
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className='bi bi-cash-coin',
                                                                                                style=card_icon
                                                                                            )
                                                                                        ],
                                                                                        style={"backgroundColor": 'yellow'}
                                                                                )
                                                                            ]
                                                                        )
                                                                        ),
                                                                    html.Br(),
                                                                    output_card(card_id='cred3',card_label='Income Max earning', 
                                                                                icon='bi bi-cash-coin', style={'backgroundColor': 'yellow'}
                                                                                ),
                                                                   
                                                                ]
                                                        )
                                            ]
                                        ),
                                    
                                    #dbc.Row([output_card(card_id='newcard', card_label='test card')]),
                                    html.Br(),
                                    dbc.Row([html.Div([('Expenditure: Visualization of average expenditure of selected items per state'),
     dcc.Dropdown(LSMS_df.state_name.unique(), id='state_name',placeholder='Select a city'),
                                              
     html.Div(id='output_container',children=[]),
     html.Br(),
     dcc.Graph(id='state_graph'),
    
                                                      ])
                                        ]),
                                    
                                    html.Div([], id="container_to_render")
                                ]
                            )
            ]
    )
])

income_page =html.Div([
    dbc.Row(
            children=[ 
                    dbc.Col(lg=1),
                    dbc.Col(lg=2, #style={'marginRight': '2%'},
                            children=[
                                #dbc.Label('Select State'),
                                #dcc.Dropdown(id='state_dropdown',
                                                #options=[{'label': state, 'value': state}
                                                        #for state in LSMS_df['state_name'].unique()
                                                        #],
                                                #placeholder='Select states'
                                                #)
                                dbc.Label('Labour Type'),
                                dcc.Dropdown(LSMS2_df.labour_type.unique(), id='labour_type',placeholder='Select labour type')
                            ]
                        
                    ),
                    dbc.Col(lg=9,
                            children=[
                                    dbc.Row(
                                            children=[
                                                        dbc.Row(
                                                                children=[
                                                                    dbc.Col(
                                                                        dbc.CardGroup(
                                                                            children=[
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.H3(id='Avg_Inc'
                                                                                                    ),
                                                                                            html.P('Average income per Labour Type')
                                                                                        ]
                                                                                    ),
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className='bi bi-cash-coin',
                                                                                                style=card_icon
                                                                                            )
                                                                                        ],
                                                                                        style={"backgroundColor": 'green'}
                                                                                )
                                                                            ]
                                                                        )
                                                                    ),
                                                                            ]
                                                                )
                                            ]
                                    ),
                                              #html.Br(),
                                    #dbc.Row([html.Div([('Average Income distribution per labour type'),
     #dcc.Dropdown(LSMS2_df.labour_type.unique(), id='labour_type',placeholder='Select labour type'),
                                              
     #html.Div(id='output_container',children=[]),
     #html.Br(),
     #dcc.Graph(id='state2_graph'),
                            #])
                    
                                    #])
                            ]
                    )
                    
            ]
    )
])
                                                                                                                     
                                                                 
#html.Div([
    #dbc.Row(dbc.Row([dbc.Col(lg=1),
                    # output_card(card_id='inc', card_label='Average income')
                   # ]
                   # )
            #)
#)


Credit_page = html.Div([
                    dbc.Row(
                            children=[ 
                                     dbc.Col(lg=1),
                                     dbc.Col(lg=2, #style={'marginRight': '2%'},
                                             children=[
                                                    dbc.Label('Select State'),
                                                    dcc.Dropdown(id='state_dropdown',
                                                       options=[{'label': state, 'value': state}
                                                        for state in LSMS_df['state_name'].unique()
                                                        ],
                                                              placeholder='Select state'
                                                                 )
                                                ]
                        
                                    ),
                                     
                                     #dbc.Row([output_card(card_id='cre', card_label='test card')]),
                                     #dbc.Row([output_card(card_id='cre1', card_label='test card')]),
                                     #dbc.Row([output_card(card_id='cre2', card_label='test card')]),
                                      
                            
                                    html.Br(),                 
                                    dbc.Row(dbc.Row([dbc.Col(lg=1),
                                                     output_card(card_id='cre', card_label='Average Income')
                    
                                     ])
                                            ),
                    
                                    html.Br(),  
                                    dbc.Col(dbc.Row([dbc.Col(lg=1),
                                    output_card(card_id='cre1', card_label='Min Average Credit')
                    
                                                 ])
                                    ),
                                    html.Br(),
                                    dbc.Col(dbc.Row([dbc.Col(lg=1),
                                    output_card(card_id='cre2', card_label='Max Average Credit')
                                                    ])
                   
                                            )
                    
                        ]
                )
                
])

welcome_page = html.Div([
    dbc.Row(dbc.Row([dbc.Col(lg=1),
                        output_card(card_id='welcome', card_label='Welcome')
                    ]
                    )
            )

])
page_view = html.Div(
    [
        dtc.SideBar(children=[
                                dtc.SideBarItem(id='income_sidebar', label='Income', icon='far fa-money-bill-alt'),
                                dtc.SideBarItem(id='Credit_sidebar', label='Credit', icon='bi bi-credit-card'),
                                dtc.SideBarItem(id='expend_sidebar', label='Expenditure', icon='bi bi-wallet-fill')
                            ]),
        html.Div([], id="content")
    ]
)
