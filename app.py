import pandas as pd
import numpy as np
import plotly.express as px
from datar.all import case_when, f, mutate, pivot_wider
from datar import dplyr
import plotly.io as pio
#from plotly.offline import init_notebook_mode, plot
#init_notebook_mode()
import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
from dash.dependencies import Output, Input
import plotly.graph_objs as go
from Stylee import cardbody_style, card_icon, cardimg_style, card_style
from helping_components import output_card
import Analytics_page

LSMS1=pd.read_csv(r'C:\Users\flavi\Downloads\data for practice\sect11b_harvestw3.csv')
LSMS1.rename(columns={'s11bq4': 'expenditure',},inplace=True)
LSMS1.dropna(subset=['expenditure'],inplace=True)

LSMS1_data_list=['KEROSENE', 'PALM KERNEL OIL', 'OTHER LIQUID COOKING FUEL', 'ELECTRICITY', 'CANDLES', 'FIREWOOD', 'CHARCOAL', 
                'PETROL','DIESEL']
LSMS1_List=LSMS1[LSMS1.item_desc.isin(LSMS1_data_list)]

LSMS_df=mutate(LSMS1_List,state_name=case_when(f.state==1,'Abia', f.state==2,'Adamawa',f.state==3,'Akwa Ibom',
                                                         f.state==4,'Anambra',f.state==5,'Bauchi',f.state==6,'Bayelsa',
                                                          f.state==7,'Benue',f.state==8,'Borno',f.state==9,'Cross River',
                                                       f.state==10,'Delta', f.state==11,'Ebonyi',f.state==12,'Edo', 
                                                        f.state==13,'Ekiti', f.state==14,'Enugu',f.state==15,'Gombe',
                                                        f.state==16,'Imo',f.state==17,'Jigawa',f.state==18,'Kaduna',
                                                          f.state==19,'Kano',f.state==20,'Katsina',f.state==21,'Kebbi',
                                                         f.state==22,'Kogi',f.state==23,'Kwara',f.state==24,'Lagos',
                                                         f.state==25,'Nasarawa',f.state==26,'Niger',f.state==27,'Ogun',
                                                         f.state==28,'Ondo',f.state==29,'Osun',f.state==30,'Oyo',
                                                         f.state==31,'Plateau',f.state==32,'Rivers',f.state==33,'Sokoto',
                                                        f.state==34,'Taraba',f.state==35,'Yobe',f.state==36,'Zamfara',
                                                         f.state==37,'FCT Abuja')
                                        .drop(columns='state'))

LSMS2=pd.read_csv(r'C:\Users\flavi\Downloads\data for practice\sect3_plantingw3.csv',low_memory=False)
LSMS2.rename(columns={'s3q21a': 'Income_dist',},inplace=True)
LSMS2.dropna(subset=['Income_dist'],inplace=True)
LSMS2_df=mutate(LSMS2,state_name=case_when(f.state==1,'Abia', f.state==2,'Adamawa',f.state==3,'Akwa Ibom',
                                                         f.state==4,'Anambra',f.state==5,'Bauchi',f.state==6,'Bayelsa',
                                                          f.state==7,'Benue',f.state==8,'Borno',f.state==9,'Cross River',
                                                       f.state==10,'Delta', f.state==11,'Ebonyi',f.state==12,'Edo', 
                                                        f.state==13,'Ekiti', f.state==14,'Enugu',f.state==15,'Gombe',
                                                        f.state==16,'Imo',f.state==17,'Jigawa',f.state==18,'Kaduna',
                                                          f.state==19,'Kano',f.state==20,'Katsina',f.state==21,'Kebbi',
                                                         f.state==22,'Kogi',f.state==23,'Kwara',f.state==24,'Lagos',
                                                         f.state==25,'Nasarawa',f.state==26,'Niger',f.state==27,'Ogun',
                                                         f.state==28,'Ondo',f.state==29,'Osun',f.state==30,'Oyo',
                                                         f.state==31,'Plateau',f.state==32,'Rivers',f.state==33,'Sokoto',
                                                        f.state==34,'Taraba',f.state==35,'Yobe',f.state==36,'Zamfara',
                                                         f.state==37,'FCT Abuja')
                                        .drop(columns='state'))

LSMS2_df

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
              Input(component_id='state_dropdown', component_property='value'),
              )
def render_state_avg_income(state_selected):
    state6_df = LSMS2_df[LSMS2_df['state_name'] == state_selected] 
    state6_Inc_Avg = state6_df['Income_dist'].mean()  
    return f'{round(state6_Inc_Avg, 2)}'

@app.callback(Output(component_id='item', component_property='children'),
              Input(component_id='item_desc_dropdown', component_property='value'),
              )
def render_avg_desc_dropdown(item_selected):
    state7_df = LSMS1[LSMS1['item_desc'] == item_selected] 
    state7_Inc_Avg = state7_df['expenditure'].mean()
    return f'{round(state7_Inc_Avg, 2)}'

@app.callback(
              Output("content", "children"),
              Input("income_sidebar", "n_clicks_timestamp"),
              Input("Items_sidebar", "n_clicks_timestamp"),
              Input("expend_sidebar", "n_clicks_timestamp")
              )

def show_sidebar_content(income_sidebar: str, Items_sidebar: str, expend_sidebar: str):
    ctx = dash.callback_context
    button_clicked = ctx.triggered[0]["prop_id"].split(".")[0]

    if not ctx.triggered:
        button_clicked = "None"
    elif button_clicked == "income_sidebar":
        return Analytics_page.income_page
    elif button_clicked == "Items_sidebar":
        return Analytics_page.Items_page
    elif button_clicked == "expend_sidebar":
        return Analytics_page.expend_page
    else:
        return Analytics_page.welcome_page
if __name__ == '__main__':
    app.run_server(debug=False,use_reloader=False,)