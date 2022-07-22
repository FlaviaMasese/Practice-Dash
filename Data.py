#%%
import pandas as pd
import io
import numpy as np
#%%
LSMS1=pd.read_csv(r'C:\Users\flavi\Downloads\data for practice\sect11b_harvestw3.csv')
LSMS2=pd.read_csv(r'C:\Users\flavi\Downloads\data for practice\sect3_plantingw3.csv',low_memory=False)
#%%
LSMS1.rename(columns={'s11bq4': 'expenditure',},inplace=True)
LSMS1.rename(columns={'s11bq3':'purchase'},inplace=True)
#%%
LSMS2.rename(columns={"s3q13a": 'labour_type'}, inplace=True)
LSMS2.rename(columns={'s3q21a': 'Income_dist',},inplace=True)
#%%
LSMS2.dropna(subset=['Income_dist'],inplace=True)
LSMS1.dropna(subset=['expenditure'],inplace=True)
LSMS2.dropna(subset=['labour_type'],inplace=True)
#%%
LSMS1_data_list=['KEROSENE', 'PALM KERNEL OIL', 'OTHER LIQUID COOKING FUEL', 'ELECTRICITY', 'CANDLES', 'FIREWOOD', 'CHARCOAL', 
                'PETROL','DIESEL']
LSMS1_sv=LSMS1[LSMS1.item_desc.isin(LSMS1_data_list)]
#%%
from datar.all import case_when, f, mutate, pivot_wider
LSMS_df=mutate(LSMS1_sv,state_name=case_when(f.state==1,'Abia', f.state==2,'Adamawa',f.state==3,'Akwa Ibom',
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
LSMS_df
#%%
LSMS2.rename(columns={'s3q13a': 'labour_type',},inplace=True)
LSMS2_sv=LSMS2[['state','labour_type','Income_dist']]
#%%
LSMS2_df=mutate(LSMS2_sv,state_name=case_when(f.state==1,'Abia', f.state==2,'Adamawa',f.state==3,'Akwa Ibom',
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
#%%
LSMS3 = pd.read_csv(r'C:\Users\flavi\Downloads\data for practice\sect4c2_plantiNG.csv')
LSMS3.rename(columns={'s4cq6':'credit',},inplace=True)
LSMS3
#%%
LSMS1_df = mutate(LSMS_df,Items=case_when(f.sector==1,'purchased', f.sector==2,'Not purchased')
                                      .drop(columns='purchase'))
