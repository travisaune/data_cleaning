# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 17:13:03 2023

@author: tjaun
"""



# Title:       Analysis of SBA Lending and Entrepreneurship
# File:        sba_lending_analysis.py
# Date:        April 30, 2023
# Description: 



#INSTALL PANDAS AND LOAD DATA####

#install pandas as numpy
import pandas as pd
import numpy as np #if needed
import matplotlib.pyplot as plt


#load business formation data (previously cleaned but need to aggregate from county and state level to national level)
df_bfs = pd.read_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\Business_Formation\bfs_apps_pdmelt.csv')
df_bfs.head()
    #aggregate to national level
df_bfs = pd.read_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\Business_Formation\bfs_agg.csv')
df_bfs.head()
len(df_bfs)

#load business dynamics data (previously cleaned but need to aggregate for NAICS and national level)
df_bds = pd.read_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\Business_Formation\bds_agg_clean.csv')
df_bds.head()
    #question on bds, look at total for all industries? If so, remove other NAICS labels here:
        #filter for all sectors, U.S. - remove state-level data and sector-level data
df_bds_totalsector_usa = df_bds[(df_bds['NAICS_LABEL']=='Total for all sectors')]
df_bds_totalsector_usa = df_bds_totalsector_usa[(df_bds_totalsector_usa['NAME']=='United States')]
#now check index
len(df_bds.index) #16,640
len(df_bds_totalsector_usa.index) #16
for col in df_bds.columns:
    print(col)


#load SBA lending data (needs to be cleaned and formatted)
df_sba = pd.read_excel(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\Business_Formation\sba_lending.xlsx', sheet_name='Yearly', header=3)
df_sba.head()
    #clean data
for col in df_sba.columns:
    print(col)
    #reformat - wide to narrow; 10 columns to 5 columns, 33 rows to 66 rows
df_504 = df_sba.loc[:,['FY.1','MAJPGM.1','Approved Loans.1','Approved Dollars.1','Approved SBA Guaranty Amount.1']]
df_7a = df_sba.loc[:,['FY','MAJPGM','Approved Loans','Approved Dollars','Approved SBA Guaranty Amount']]
df_504.head
df_7a.head
for col in df_7a.columns:
    print(col)
for col in df_504.columns:
    print(col)
df_504 = df_504.rename({'FY.1':'FY','MAJPGM.1':'MAJPGM','Approved Loans.1':'Approved Loans','Approved Dollars.1':'Approved Dollars','Approved SBA Guaranty Amount.1':'Approved SBA Guaranty Amount'}, axis=1)
df_sba = pd.concat([df_504,df_7a], axis=0)
df_sba.head




df_sba.describe

# show all rows and columns

print(df_sba)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(df_bds_totalsector_usa)


#DOWNLOAD VERSION FOR GOOGLE SHEETS####

#bfs
df_bfs.to_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\Business_Formation\google_bfs_agg_clean.csv',index=False)

#bds
df_bds_totalsector_usa.to_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\Business_Formation\google_bds_agg_clean.csv',index=False)

#sba
df_sba.to_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\Business_Formation\google_sba_agg_clean.csv',index=False)















#SUMMARIES AND GRAPHS####

#SBA Lending

# 










df_7apd = pd.df_7a({"Approved Dollars"}, index=['FY'])
lines = df_7a.plot.line()


Year7a = df_7a['FY']
Approved7a = df_7a['Approved Dollars']
#Guaranty7a = df_7a['Approved SBA Guaranty Amount']

# Create a new figure and axis
fig, ax = plt.subplots()

# Plot the data as a line graph
ax.plot(Year7a, Approved7a)
ax.set_ylim([0, 5000000])

# Add axis labels and a title
ax.set_xlabel('Year')
ax.set_ylabel('Amount')



ax.set_title('7a Lending Approved')

# Display the graph
plt.show()








#New Business Applications















#BDS Data






















