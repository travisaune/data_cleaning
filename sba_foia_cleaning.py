# -*- coding: utf-8 -*-
"""
Created on Wed May  3 08:48:16 2023

@author: tjaun
"""



# Title:       SBA Lending FOIA Data as of 3/31/2023
# File:        sba_foia_cleaning.py
# Date:        May 3, 2023
# Description: 7a and 504 programs data



#INSTALL PANDAS AND LOAD DATA####

#install pandas as numpy
import pandas as pd

#load sba 7a data for 1990s
df_7a90 = pd.read_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\SBA_Lending\7a90_original.csv')
df_7a90.head() #39 columns
len(df_7a90) #337,043

#load sba 7a data for 2000s
df_7a00 = pd.read_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\SBA_Lending\7a00_original.csv', encoding='latin-1')
df_7a00.head() #39 columns
len(df_7a00) #690,347

#load sba 7a data for 2010s
df_7a10 = pd.read_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\SBA_Lending\7a10_original.csv', encoding='latin-1')
df_7a10.head() #39 columns
len(df_7a10) #545,751

#load sba 7a data for 2020s
df_7a20 = pd.read_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\SBA_Lending\7a20_original.csv', encoding='latin-1')
df_7a20.head() #39 columns
len(df_7a20) #168,211

#load 504 data for 1990s and 2000s
df_504_pre2010 = pd.read_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\SBA_Lending\504pre2010_original.csv')
df_504_pre2010.head() #38 columns
len(df_504_pre2010) #111341

#load 504 data for 2010s and 2020s
df_504_post2010 = pd.read_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\SBA_Lending\504post2010_original.csv')
df_504_post2010.head() #38 columns
len(df_504_post2010) #97798



#EDIT COLUMNS####

#view
print(" ")
print("7a90 Original Columns")
for col in df_7a90.columns:
    print(col)

print(" ")
print("7a00 Original Columns")
for col in df_7a00.columns:
    print(col)

print(" ")
print("7a10 Original Columns")
for col in df_7a10.columns:
    print(col)

print(" ")
print("7a20 Original Columns")
for col in df_7a20.columns:
    print(col)

print(" ")
print("504pre10 Original Columns")
for col in df_504_pre2010.columns:
    print(col)

print(" ")
print("504post10 Original Columns")
for col in df_504_post2010.columns:
    print(col)



#SAVE NEW CSV####
df_7aALL = pd.concat([df_7a90,df_7a00,df_7a10,df_7a20], axis=0)
df_7aALL.describe() #len is 
df_7aALL.to_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\SBA_Lending\7aALL_clean.csv',index=False)

df_504ALL = pd.concat([df_504_pre2010,df_504_post2010], axis=0)
df_504ALL.describe() #len is 
df_504ALL.to_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\SBA_Lending\504ALL_clean.csv',index=False)







#MAKE REDUCED VARIABLE DATASET

#remove columns not needed
df_7aALL_reduced = df_7aALL.drop(['BorrStreet','BankName','BankFDICNumber','BankNCUANumber','BankStreet','BankCity','BankState','BankZip','SBAGuaranteedApproval','ApprovalFiscalYear','FirstDisbursementDate','DeliveryMethod','subpgmdesc','InitialInterestRate','FranchiseCode','FranchiseName','CongressionalDistrict','BusinessType','BusinessAge','PaidInFullDate','ChargeOffDate','GrossChargeOffAmount','RevolverStatus'], axis=1)
df_504ALL_reduced = df_504ALL.drop(['BorrStreet','CDC_Name','CDC_Street','CDC_City','CDC_State','CDC_Zip','ThirdPartyLender_Name','ThirdPartyLender_City','ThirdPartyLender_State','ThirdPartyDollars','ApprovalFiscalYear','FirstDisbursementDate','DeliveryMethod','subpgmdesc','FranchiseCode','FranchiseName','CongressionalDistrict','BusinessType','BusinessAge','PaidInFullDate','ChargeOffDate','GrossChargeOffAmount'],axis=1)

df_7aALL_reduced.head()
df_504ALL_reduced.head()


df_sba_agg_reduced = pd.concat([df_7aALL_reduced,df_504ALL_reduced], axis=0)
df_sba_agg_reduced.describe() #len is 1,950,491 
df_sba_agg_reduced.to_csv(r'C:\Users\tjaun\OneDrive\Documents\My Data Sources\SBA_Lending\sba_agg_reduced.csv',index=False)



#MAKE REDUCED VARIABLE DATASET EXCLUDING 1990s
pd.set_option('display.max_columns', None)
df_7a_exc90s = pd.concat([df_7a00,df_7a10,df_7a20], axis=0)

df_7a_exc90s = df_7a_exc90s.drop(['BorrStreet','BankName','BankFDICNumber','BankNCUANumber','BankStreet','BankCity','BankState','BankZip','SBAGuaranteedApproval','ApprovalFiscalYear','FirstDisbursementDate','DeliveryMethod','subpgmdesc','InitialInterestRate','FranchiseCode','FranchiseName','CongressionalDistrict','BusinessType','BusinessAge','PaidInFullDate','ChargeOffDate','GrossChargeOffAmount','RevolverStatus'], axis=1)


sba_exc_90s_agg = pd.concat([df_7a_exc90s,df_504ALL_reduced], axis=0)
sba_exc_90s_agg.describe() #len is 1,613,448
#nevermind











































