from Stylee import cardbody_style, card_icon, cardimg_style, card_style
from helping_components import output_card
import Analytics_page

app = dash.Dash(__name__, external_stylesheets= [dbc.themes.CYBORG, dbc.icons.BOOTSTRAP, dbc.icons.FONT_AWESOME])

img2 = './Img/stephen-dawson-qwtCeJ5cLYs-unsplash.jpeg'


start_page = html.Div(
    children=[     
        dcc.Location(id='location_url'),
        dbc.Row(html.Div(id="page_location"))
        ],
)

homepage = html.Div(children=[
    
    dbc.Container(children=[       
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
                                dbc.CardLink(id="analytics_link",
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
                                    dbc.CardLink(id="ml_link",
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


ml_page = html.Div([])

app.layout = start_page
app.validation_layout = html.Div([homepage, Analytics_page.page_view, ml_page])

######## callback  ######
@app.callback(Output(component_id="page_location", component_property="children"),
              Input(component_id="location_url", component_property="href")
              )
def render_page_selected(page_link):
    page_selected = page_link.split('/')[-1]
    
    if page_selected == 'ml':
        return ml_page
    elif page_selected == 'analytics':
        return Analytics_page.page_view
    else:
        return homepage
    
@app.callback(Output(component_id='avg_expense', component_property='children'),
              Input(component_id='state_dropdown', component_property='value'))
def render_state_avg_income(state_selected):
    state_df = LSMS_df[LSMS_df['state_name'] == state_selected] 
    state_avg_expd = state_df['expenditure'].mean()  
    return f'{round(state_avg_expd, 2)}'


@app.callback(
    Output("content", "children"),
    Input("income_sidebar", "n_clicks_timestamp"),
    Input("credit_sidebar", "n_clicks_timestamp"),
    Input("expend_sidebar", "n_clicks_timestamp")
)
def show_sidebar_content(income_sidebar: str, credit_sidebar: str, expend_sidebar: str):
    ctx = dash.callback_context
    button_clicked = ctx.triggered[0]["prop_id"].split(".")[0]

    if not ctx.triggered:
        button_clicked = "None"
    elif button_clicked == "income_sidebar":
        return Analytics_page.income_page
    elif button_clicked == "credit_sidebar":
        return Analytics_page.credit_page
    elif button_clicked == "expend_sidebar":
        return Analytics_page.expend_page
    else:
        return Analytics_page.welcome_page


if __name__ == '__main__':
    app.run_server(debug=False,use_reloader=False, port='8055')
   
# %%