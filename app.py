#%%
import pandas as pd
import numpy as np
import plotly.express as px
from datar.all import case_when, f, mutate, pivot_wider
from datar import dplyr
import plotly.io as pio
import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
from dash.dependencies import Output, Input
import plotly.graph_objs as go
from Stylee import cardbody_style, card_icon, cardimg_style, card_style
from helping_components import output_card
import Analytics_page
#%%
from Data import LSMS_df
from Data import LSMS2_df
from Data import LSMS3
from Data import LSMS1_df
#%%
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
    
@app.callback(Output(component_id='state_graph', component_property='figure'),
              Output(component_id='avg_expense', component_property='children'),
              Input(component_id='state_dropdown', component_property='value'),
              Input(component_id='state_name', component_property='value'),
              )
def update_graph(state_selected, avg_expensed ):
    df = LSMS_df[LSMS_df['state_name']==state_selected]
    fig=px.bar(data_frame=df,
                x='item_desc',
                y='expenditure',
                color='state_name',
                opacity=0.9,
                orientation='v',
                barmode='relative',
                hover_name='expenditure',
                template='plotly_dark',
                animation_frame='state_name',
                title=f'Graph of {state_selected}'
                )
    state_df = LSMS_df[LSMS_df['state_name'] == state_selected] 
    state_avg_expd = state_df['expenditure'].mean()  
    return fig, f'{round(state_avg_expd, 2)}'

@app.callback(Output(component_id='avg2', component_property='children'),
              Input(component_id='state_dropdown', component_property='value')
              )
def render_state_avg_income(state_selected):
    state3_df = LSMS_df[LSMS_df['state_name'] == state_selected] 
    state3_Min_Avg = state3_df['expenditure'].min()  
    return f'{round(state3_Min_Avg, 2)}'

@app.callback(Output(component_id='avg3', component_property='children'),
              Input(component_id='state_dropdown', component_property='value')
              )
def render_state_avg_income(state_selected):
    stateX_df = LSMS_df[LSMS_df['state_name'] == state_selected] 
    stateX_Min_Avg = stateX_df['expenditure'].max()  
    return f'{round(stateX_Min_Avg, 2)}'

@app.callback(Output(component_id='cred1', component_property='children'),
              Input(component_id='state_dropdown', component_property='value')
              )
def render_state_avg_income(state_selected):
    state2_df = LSMS2_df[LSMS2_df['state_name'] == state_selected] 
    state2_Inc_Avg = state2_df['Income_dist'].mean()  
    return f'{round(state2_Inc_Avg, 2)}'

@app.callback(Output(component_id='cred2', component_property='children'),
              Input(component_id='state_dropdown', component_property='value')
              )
def render_state_avg_income(state_selected):
    state4_df = LSMS2_df[LSMS2_df['state_name'] == state_selected] 
    state4_Inc_Avg = state4_df['Income_dist'].min()
    return f'{round( state4_Inc_Avg, 2)}'

@app.callback(Output(component_id='cred3', component_property='children'),
              Input(component_id='state_dropdown', component_property='value')
              )
def render_state_avg_income(state_selected):
    state5_df = LSMS2_df[LSMS2_df['state_name'] == state_selected] 
    state5_Inc_Avg = state5_df['Income_dist'].max()  
    return f'{round(state5_Inc_Avg, 2)}'


@app.callback(Output(component_id='Avg_Inc', component_property='children'),
              Output(component_id='histo_graph', component_property='figure'),
              Input(component_id='state_dropdown', component_property='value'),
              Input(component_id='state_name', component_property='value')
              )
def update_graph(state_selected,Avg_selected):
    fig2 = px.histogram(LSMS1_df, x="item_desc", y="expenditure",
             color='Items', barmode='group',
             histfunc='avg',
             height=400)
    state51_df = LSMS1_df[LSMS1_df['state_name'] == state_selected] 
    state51_avg_expd = state51_df['expenditure'].mean()  
    return fig2, f'{round(state51_avg_expd, 2)}'
    
@app.callback(Output(component_id='cre', component_property='children'),
              Input(component_id='state_dropdown', component_property='value')
              )
def render_state_avg_credit(state_selected):
    state22_df = LSMS3[LSMS3['state_name'] == state_selected] 
    state22_Inc_Avg = state22_df['credit'].mean()  
    return f'{round(state22_Inc_Avg, 2)}'  

@app.callback(Output(component_id='cre1', component_property='children'),
              Input(component_id='state_dropdown', component_property='value')
              )
def render_state_avg_credit(state_selected):
    state23_df = LSMS3[LSMS3['state_name'] == state_selected] 
    state23_Inc_Avg = state23_df['credit'].mean()  
    return f'{round(state23_Inc_Avg, 2)}'

@app.callback(Output(component_id='cre2', component_property='children'),
              Input(component_id='state_dropdown', component_property='value')
              )
def render_state_avg_credit(state_selected):
    state24_df = LSMS3[LSMS3['state_name'] == state_selected] 
    state24_Inc_Avg = state24_df['credit'].mean()  
    return f'{round(state24_Inc_Avg, 2)}'


@app.callback(
              Output("content", "children"),
              Input("income_sidebar", "n_clicks_timestamp"),
              Input("Credit_sidebar", "n_clicks_timestamp"),
              Input("expend_sidebar", "n_clicks_timestamp")
              )

def show_sidebar_content(income_sidebar: str, Credit_sidebar: str, expend_sidebar: str):
    ctx = dash.callback_context
    button_clicked = ctx.triggered[0]["prop_id"].split(".")[0]

    if not ctx.triggered:
        button_clicked = "None"
    elif button_clicked == "income_sidebar":
        return Analytics_page.income_page
    elif button_clicked == "Credit_sidebar":
        return Analytics_page.Credit_page
    elif button_clicked == "expend_sidebar":
        return Analytics_page.expend_page
    else:
        return Analytics_page.welcome_page
if __name__ == '__main__':
    app.run_server(debug=False,use_reloader=False,)