# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 17:18:19 2023

@author: tjaun
"""

# Title:       Cleaning BDS Data Aggregated for U.S.
# File:        bds_agg_clean.py
# Date:        April 30, 2023
# Description: 



#INSTALL PANDAS AND LOAD DATA####

#install pandas as numpy
import pandas as pd
import numpy as np #if needed


#load business dynamics data (needs to be cleaned and formatted)
df_bds = pd.read_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\Business_Formation\bds_agg.csv')
df_bds.head()


#VIEW COLUMNS AND SORT####
#view columns
print(" ")
print("Original Columns")
for col in df_bds.columns:
    print(col)

#current columns
#"Geographic Area Name (NAME)"
#"2017 NAICS Code (NAICS)"
#"Meaning of NAICS Code (NAICS_LABEL)"
#"Meaning of Establishments located in Metropolitan or Micropolitan Statistical Area indicator (METRO_LABEL)"
#"Year (YEAR)"
#"Number of firms (FIRM)"
#"Number of establishments (ESTAB)"
#"Number of employees (EMP)"
#"(DHS) denominator (DENOM)"
#"Number of establishments born during the last 12 months (ESTABS_ENTRY)"
#"Rate of establishments born during the last 12 months (ESTABS_ENTRY_RATE)"
#"Number of establishments exited during the last 12 months (ESTABS_EXIT)"
#"Rate of establishments exited during the last 12 months (ESTABS_EXIT_RATE)"
#"Number of jobs created from expanding and opening establishments during the last 12 months (JOB_CREATION)"
#"Number of jobs created from opening establishments during the last 12 months (JOB_CREATION_BIRTHS)"
#"Number of jobs created from expanding establishments during the last 12 months (JOB_CREATION_CONTINUERS)"
#"Rate of jobs created from opening establishments during the last 12 months (JOB_CREATION_RATE_BIRTHS)"
#"Rate of jobs created from expanding and opening establishments during the last 12 months (JOB_CREATION_RATE)"
#"Number of jobs lost from contracting and closing establishments during the last 12 months (JOB_DESTRUCTION)"
#"Number of jobs lost from closing establishments during the last 12 months (JOB_DESTRUCTION_DEATHS)"
#"Number of jobs lost from contracting establishments during the last 12 months (JOB_DESTRUCTION_CONTINUERS)"
#"Rate of jobs lost from closing establishments during the last 12 months (JOB_DESTRUCTION_RATE_DEATHS)"
#"Rate of jobs lost from contracting and closing establishments during the last 12 months (JOB_DESTRUCTION_RATE)"
#"Number of net jobs created from expanding/contracting and opening/closing establishments during the last 12 months (NET_JOB_CREATION)"
#"Rate of net jobs created from expanding/contracting and opening/closing establishments during the last 12 months (NET_JOB_CREATION_RATE)"
#"Rate of reallocation during the last 12 months (REALLOCATION_RATE)"
#"Number of firms that exited during the last 12 months (FIRMDEATH_FIRMS)"
#"Number of establishments associated with firm deaths during the last 12 months (FIRMDEATH_ESTABS)"
#"Number of employees associated with firm deaths during the last 12 months (FIRMDEATH_EMP)"

#current columns KEEP
#"Geographic Area Name (NAME)"
#"2017 NAICS Code (NAICS)"
#"Meaning of NAICS Code (NAICS_LABEL)"
#"Year (YEAR)"
#"Number of firms (FIRM)"
#"Number of employees (EMP)"
#"Number of establishments (ESTAB)"
#"(DHS) denominator (DENOM)"
#"Number of establishments born during the last 12 months (ESTABS_ENTRY)"
#"Rate of establishments born during the last 12 months (ESTABS_ENTRY_RATE)"
#"Number of establishments exited during the last 12 months (ESTABS_EXIT)"
#"Rate of establishments exited during the last 12 months (ESTABS_EXIT_RATE)"
#"Number of jobs created from opening establishments during the last 12 months (JOB_CREATION_BIRTHS)"
#"Number of jobs lost from contracting and closing establishments during the last 12 months (JOB_DESTRUCTION)"
#"Number of net jobs created from expanding/contracting and opening/closing establishments during the last 12 months (NET_JOB_CREATION)"
#"Rate of net jobs created from expanding/contracting and opening/closing establishments during the last 12 months (NET_JOB_CREATION_RATE)"
#"Rate of reallocation during the last 12 months (REALLOCATION_RATE)"
#"Number of firms that exited during the last 12 months (FIRMDEATH_FIRMS)"

#current columns DROP
#"Meaning of Establishments located in Metropolitan or Micropolitan Statistical Area indicator (METRO_LABEL)"
#"Number of jobs created from expanding and opening establishments during the last 12 months (JOB_CREATION)"
#"Number of jobs created from expanding establishments during the last 12 months (JOB_CREATION_CONTINUERS)"
#"Rate of jobs created from opening establishments during the last 12 months (JOB_CREATION_RATE_BIRTHS)"
#"Rate of jobs created from expanding and opening establishments during the last 12 months (JOB_CREATION_RATE)"
#"Number of jobs lost from closing establishments during the last 12 months (JOB_DESTRUCTION_DEATHS)"
#"Number of jobs lost from contracting establishments during the last 12 months (JOB_DESTRUCTION_CONTINUERS)"
#"Rate of jobs lost from closing establishments during the last 12 months (JOB_DESTRUCTION_RATE_DEATHS)"
#"Rate of jobs lost from contracting and closing establishments during the last 12 months (JOB_DESTRUCTION_RATE)"
#"Number of establishments associated with firm deaths during the last 12 months (FIRMDEATH_ESTABS)"
#"Number of employees associated with firm deaths during the last 12 months (FIRMDEATH_EMP)"



#DROP AND RENAME COLUMNS####
df_bds = df_bds.drop(["Meaning of Establishments located in Metropolitan or Micropolitan Statistical Area indicator (METRO_LABEL)","Number of jobs created from expanding and opening establishments during the last 12 months (JOB_CREATION)"], axis=1)
df_bds = df_bds.drop(["Number of jobs created from expanding establishments during the last 12 months (JOB_CREATION_CONTINUERS)","Rate of jobs created from opening establishments during the last 12 months (JOB_CREATION_RATE_BIRTHS)"], axis=1)
df_bds = df_bds.drop(["Rate of jobs created from expanding and opening establishments during the last 12 months (JOB_CREATION_RATE)","Number of jobs lost from closing establishments during the last 12 months (JOB_DESTRUCTION_DEATHS)"], axis=1)
df_bds = df_bds.drop(["Number of jobs lost from contracting establishments during the last 12 months (JOB_DESTRUCTION_CONTINUERS)","Rate of jobs lost from closing establishments during the last 12 months (JOB_DESTRUCTION_RATE_DEATHS)"], axis=1)
df_bds = df_bds.drop(["Rate of jobs lost from contracting and closing establishments during the last 12 months (JOB_DESTRUCTION_RATE)","Number of establishments associated with firm deaths during the last 12 months (FIRMDEATH_ESTABS)"], axis=1)
df_bds = df_bds.drop(["Number of employees associated with firm deaths during the last 12 months (FIRMDEATH_EMP)"], axis=1)

#rename columns
df_bds = df_bds.rename({'Year (YEAR)':'YEAR',"Geographic Area Name (NAME)":"NAME"}, axis=1)
df_bds = df_bds.rename({"2017 NAICS Code (NAICS)":'NAICS', "Meaning of NAICS Code (NAICS_LABEL)" : 'NAICS_LABEL'}, axis=1)
df_bds = df_bds.rename({"Number of firms (FIRM)":'FIRM', "Number of employees (EMP)" : 'EMP', "Number of establishments (ESTAB)" : 'ESTAB', "(DHS) denominator (DENOM)" : "DENOM"}, axis=1)
df_bds = df_bds.rename({"Number of establishments born during the last 12 months (ESTABS_ENTRY)" : "ESTABS_ENTRY", "Rate of establishments born during the last 12 months (ESTABS_ENTRY_RATE)":'ESTABS_ENTRY_RATE'}, axis=1)
df_bds = df_bds.rename({"Number of establishments exited during the last 12 months (ESTABS_EXIT)" : "ESTABS_EXIT", "Rate of establishments exited during the last 12 months (ESTABS_EXIT_RATE)":'ESTABS_EXIT_RATE'}, axis=1)
df_bds = df_bds.rename({"Number of jobs created from opening establishments during the last 12 months (JOB_CREATION_BIRTHS)":'JOB_CREATION_BIRTHS'}, axis=1)
df_bds = df_bds.rename({"Number of jobs lost from contracting and closing establishments during the last 12 months (JOB_DESTRUCTION)":'JOB_DESTRUCTION'}, axis=1)
df_bds = df_bds.rename({"Number of net jobs created from expanding/contracting and opening/closing establishments during the last 12 months (NET_JOB_CREATION)" :'NET_JOB_CREATION'}, axis=1)
df_bds = df_bds.rename({"Rate of net jobs created from expanding/contracting and opening/closing establishments during the last 12 months (NET_JOB_CREATION_RATE)" :'NET_JOB_CREATION_RATE'}, axis=1)
df_bds = df_bds.rename({"Rate of reallocation during the last 12 months (REALLOCATION_RATE)":"REALLOCATION_RATE","Number of firms that exited during the last 12 months (FIRMDEATH_FIRMS)":'FIRMDEATH_FIRMS'}, axis=1)

#view columns
print(" ")
print("Updated Columns")
for col in df_bds.columns:
    print(col)



#FILTER OUT DATES####
#bfs data begins in 2005, so drop bds data before 2000
len(df_bds.index) #44,720
#convert year data to integer
df_bds['YEAR'] = df_bds['YEAR'].astype(int)

#drop years before 2005
df_bds = df_bds[~(df_bds['YEAR']<2005)]
len(df_bds.index) #16,640


df_bds.YEAR.describe()
min_year = df_bds['YEAR'].min
print(min_year)

#optional
pd.set_option('display.max_columns', None)
df_bds.YEAR.describe()
df_bds.head()


#SAVE NEW CSV####
df_bds.to_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\Business_Formation\bds_agg_clean.csv',index=False)
