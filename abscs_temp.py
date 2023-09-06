# -*- coding: utf-8 -*-
"""
Created on Tue May  2 15:55:51 2023

@author: tjaun
"""



# Title:       Business Ownership Stats Cleaning
# File:        tbd
# Date:        May 2, 2023
# Description: Stats are taken from American Business Survey Data, FY2017-2020



#INSTALL PANDAS AND LOAD DATA####

#install pandas as numpy
import pandas as pd

#load abs data for 2017
df_abs17 = pd.read_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\Business_Formation\abscs2017_original.csv')
df_abs17.head()
len(df_abs17) #146,098

#load abs data for 2018
df_abs18 = pd.read_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\Business_Formation\abscs2018_original.csv')
df_abs18.head()
len(df_abs18) #119,378

#load abs data for 2019
df_abs19 = pd.read_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\Business_Formation\abscs2019_original.csv')
df_abs19.head()
len(df_abs19) #119,947

#load abs data for 2020
df_abs20 = pd.read_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\Business_Formation\abscs2020_original.csv')
df_abs20.head()
len(df_abs20) #122,770



#EDIT COLUMNS####

#view
print(" ")
print("2017 Original Columns")
for col in df_abs17.columns:
    print(col)

print(" ")
print("2018 Original Columns")
for col in df_abs18.columns:
    print(col)

print(" ")
print("2019 Original Columns")
for col in df_abs19.columns:
    print(col)

print(" ")
print("2020 Original Columns")
for col in df_abs20.columns:
    print(col)

#remove columns
col_drop = ['GEO_ID_F','NAICS2017_F','FIRMPDEMP_F','RCPPDEMP_F','EMP_F','PAYANN_F','FIRMPDEMP_S_F','RCPPDEMP_S_F','EMP_S_F','PAYANN_S_F']
for df in [df_abs17,df_abs18,df_abs19,df_abs20]:
    df.drop(columns=col_drop, inplace = True)

col_drop1 = ['INDLEVEL','INDGROUP','SUBSECTOR','SECTOR','Unnamed: 35']
for df in [df_abs17,df_abs18]:
    df.drop(columns=col_drop1, inplace=True)

col_drop2 = ['Unnamed: 31']
for df in [df_abs19,df_abs20]:
    df.drop(columns=col_drop2, inplace=True)

#view all remaining columns
pd.set_option('display.max_columns', None)
for df in [df_abs17,df_abs18,df_abs19,df_abs20]:
    print(df.head())



#EDIT ROWS####

#save column name and row 1 to new df as variable definition
df_variables = df_abs17.iloc[0:1,:]
df_variables

#drop row 1 variable definitions from df's
for df in [df_abs17,df_abs18,df_abs19,df_abs20]:
    df.drop(0,axis=0,inplace=True)
for df in [df_abs17,df_abs18,df_abs19,df_abs20]:
    print(df.head())



#SAVE NEW CSV####
df_abs = pd.concat([df_abs17,df_abs18,df_abs19,df_abs20], axis=0)
df_abs.describe() #len is 508,189
df_abs.to_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\Business_Formation\abscsTOTAL_agg_clean.csv',index=False)