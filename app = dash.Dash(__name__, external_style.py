app = dash.Dash(__name__, external_stylesheets= [dbc.themes.CYBORG, dbc.icons.BOOTSTRAP, dbc.icons.FONT_AWESOME])

cardimg_style = {'width': '100%', 'height': '100%', 
              "opacity": 0.2, "objectFit": "cover"
              }
cardbody_style = {"margin": "2%"}

card_style = {"width": "20rem", "height": "20rem"}
card_icon = {
    "color": "blue",
    "textAlign": "center",
    "fontSize": "4em",
    "margin": "auto"
}

img2 = './Img/stephen-dawson-qwtCeJ5cLYs-unsplash.jpeg'
homepage = html.Div(children=[
    dbc.Container(children=[
        dcc.Location(id='location_url'),
        dbc.Row([
                    html.H3('Analysis on Living Standard Measurement Survey')
                    
                ]
            ),
        html.Br(),
        dbc.Row(
                children=[
                    dbc.Tabs(
                        children=[
                                    dbc.Tab(
                                            children=[
                                                        html.Ul(
                                                            [
                                                                html.Br(),
                                                                html.Li('Number of states in Nigeria:37'),
                                                                html.Li('Number of lga:774'),
                                                                html.Li('Currency:Naira'),
                                                                html.Li('Population:175 million:2014 estimate'),
                                                                html.Li([
                                                                        'Source:',
                                                                        html.A('https://nigerianfinder.com/facts-about-nigeria/',
                                                                                href='https://nigerianfinder.com/facts-about-nigeria/'
                                                                                )
                                                                        ]
                                                                    )
                                                            ]
                                                        )
                                                    ], 
                                            label='Key Facts'
                                        ),
                                    dbc.Tab([
                                        html.Ul([
                                            html.Br(),
                                            html.Li('General Household Survey, Panel 2015-2016,'),
                                            html.Li('Analyzing and visualizing average expenditure of selected items by States'),
                                            html.Li('Dash presentation pracice'),
                                            html.Li([
                                                'Source:',
                                                    html.A('https://microdata.worldbank.org/index.php/catalog/2734/data-dictionary',
                                                        href='https://microdata.worldbank.org/index.php/catalog/2734/data-dictionary'),
                                                        
                                                    ])
                                        ])
                                    ], label='Project Info')
                                ]
                            ),
    
                        ]
                    ),
                html.Br(),
        dbc.Row([
                 dbc.Col([
                         dbc.Card(
                            [
                                dbc.CardImg(
                                    src='./Img/firmbee-com-jrh5lAq-mIs-unsplash.jpeg',
                                
                                    style=cardimg_style,
                                ),
                                dbc.CardLink(
                                    children=[
                                        dbc.CardImgOverlay(
                                            [
                                                dbc.CardBody(
                                                    html.H3(
                                                        "Analytics",
                                                        style=cardbody_style,
                                                    )
                                                )
                                            ]
                                        )
                                    ],
                                    href="analytics",
                                ),
                            ],
                            style=card_style,
                        )
                     #])
                     ]),
                 html.Br(),
                 dbc.Col([
                        dbc.Card(
                            dbc.Card(
                                [
                                    dbc.CardImg(
                                        src=img2,
                                        style=cardimg_style,
                                    ),
                                    dbc.CardLink(
                                        children=[
                                            dbc.CardImgOverlay(
                                                [
                                                    dbc.CardBody(
                                                        html.H3(
                                                            "Machine leARNING",
                                                            style=cardbody_style,
                                                        )
                                                    )
                                                ]
                                            )
                                        ],
                                        href="ml",
                                    ),
                                ],
                                style=card_style,
                            )
                        )
                    ])   
        ])
                ],
                  
            ),
    
        
        
    ])
#])

analytic_page = html.Div([
    dbc.Row(
            children=[
                    dbc.Label('Select Indicator'),
                    dbc.Col(
                        children=[
                            
                            html.Br(), html.Br(),
                            dtc.SideBar(children=[
                                dtc.SideBarItem(id='id_1', label='Income', icon='far fa-money-bill-alt'),
                                dtc.SideBarItem(id='credit_siderbar', label='Credit', icon='bi bi-credit-card'),
                                dtc.SideBarItem(id='expen_sidebar', label='Expenditure', icon='bi bi-wallet-fill')
                            ])
                            
                                 ]
                            )
                     ]
                        ),
                    dbc.Col(
                                [
                                    dbc.Row(
                                            children=[
                                                        dbc.Row(
                                                                children=[
                                                                    dbc.Col(
                                                                        dbc.CardGroup(
                                                                            children=[
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.H3(id='avg_income',
                                                                                                    children='50'
                                                                                                    ),
                                                                                            html.P('Average income')
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
                                                                                            html.H3(id='avg_income',
                                                                                                    children='100'
                                                                                                    ),
                                                                                            html.P('Average income')
                                                                                        ]
                                                                                    ),
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className='bi bi-cash-euro',
                                                                                                style=card_icon
                                                                                            )
                                                                                        ],
                                                                                        style={"backgroundColor": 'yellow'}
                                                                                )
                                                                            ]
                                                                        )),
                                                                    dbc.Col(
                                                                        dbc.CardGroup(
                                                                            children=[
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.H3(id='avg_income',
                                                                                                    children='499'
                                                                                                    ),
                                                                                            html.P('Average income')
                                                                                        ]
                                                                                    ),
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className='bi bi-piggy-bank',
                                                                                                style=card_icon
                                                                                            )
                                                                                        ],
                                                                                        style={"backgroundColor": 'yellow'}
                                                                                )
                                                                            ]
                                                                        ))
                                                                    
                                                                ]
                                                            ),
                                                        dbc.Row(
                                                                children=[
                                                                    dbc.Col(dbc.Col(
                                                                        dbc.CardGroup(
                                                                            children=[
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.H3(id='avg_credit',
                                                                                                    children='1000'
                                                                                                    ),
                                                                                            html.P('credit')
                                                                                        ]
                                                                                    ),
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className='bi bi-cash-stack',
                                                                                                style=card_icon
                                                                                            )
                                                                                        ],
                                                                                        style={"backgroundColor": 'blue'}
                                                                                )
                                                                            ]
                                                                        )
                                                                    ),),
                                                                    dbc.Col(dbc.Col(
                                                                        dbc.CardGroup(
                                                                            children=[
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.H3(id='Avg_credit',
                                                                                                    children='500'
                                                                                                    ),
                                                                                            html.P('credit')
                                                                                        ]
                                                                                    ),
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className='bi bi-cash-coin',
                                                                                                style=card_icon
                                                                                            )
                                                                                        ],
                                                                                        style={"backgroundColor": 'blue'}
                                                                                )
                                                                            ]
                                                                        )
                                                                    ),),
                                                                    dbc.Col(dbc.Col(
                                                                        dbc.CardGroup(
                                                                            children=[
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.H3(id='avg_credit',
                                                                                                    children='*8'
                                                                                                    ),
                                                                                            html.P('credit')
                                                                                        ]
                                                                                    ),
                                                                                dbc.Card(
                                                                                        children=[
                                                                                            html.Div(
                                                                                                className='bi bi-credit-card-fill',
                                                                                                style=card_icon
                                                                                            )
                                                                                        ],
                                                                                        style={"backgroundColor": 'yellow'}
                                                                                )
                                                                            ]
                                                                        )
                                                                    ),)
                                                                ]
                                                        )
                                            ]
                                        ),
                                    
                                    dbc.Row(
                                            children=[ 
                                                dcc.Dropdown(LSMS_df.state_name.unique(), id='state_name',placeholder='Select a city'),
                                            ]
                                                ),
                                    dbc.Row( 
                                           children=[
                                                    html.Div(id='output_container',children=[]),
                                                    html.Br(),
                                                    dcc.Graph(id='state_graph'),
                                           ]
            )                                                       
               ])
                                                
                                
                            ])
            
    #)
#])

ml_page = html.Div([])
analytic_page = html.Div([])
app.layout = homepage
if __name__ == '__main__':
    app.run_server(debug=False,use_reloader=False, port='8055')