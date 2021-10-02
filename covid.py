# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:39:04 2021

@author: hp
"""

import pandas as pd
covid=pd.read_csv('C:/Users/hp/Desktop/Covid/covid_19_india.csv')
covid.columns
kerala=covid[covid['State/UnionTerritory']=='Kerala']
kerala_death=max(kerala['Deaths'])
kerala_confirmed=max(kerala['Confirmed'])
kerala=covid[covid['State/UnionTerritory']=='Kerala']
kerala_date=kerala[kerala['Date']=='02-08-2021']
kerala_rate=kerala[kerala['Date']=='26-07-2021']
kerala_con=kerala_date['Confirmed']
kerala_c=kerala_rate['Confirmed']
k_confirmed=max(kerala_con)
k_con=max(kerala_c)
diff=k_confirmed-k_con
doubling=k_confirmed/diff
doubling_rate=doubling*7
new=[]
for i in covid['State/UnionTerritory']:
    if i not in new:
        new.append(i)
def covid_func(st):
    kerala=covid[covid['State/UnionTerritory']==st]
    kerala_death=max(kerala['Deaths'])
    kerala_confirmed=max(kerala['Confirmed'])
    return st,kerala_death,kerala_confirmed
for i in new:
    x=covid_func(st=i)
    print(x)
new=[]
for i in covid['State/UnionTerritory']:
    if i not in new:
        new.append(i)
exp=['West Bengal','Telengana','Unassigned','Cases being reassigned to states','Daman & Diu','Dadra and Nagar Haveli','Bihar***','Bihar****','Madhya Pradesh***','Himanchal Pradesh','Karanataka','Maharashtra***']
def double_func(s):
    kerala=covid[covid['State/UnionTerritory']==s]
    kerala_date=kerala[kerala['Date']=='02-08-2021']
    kerala_rate=kerala[kerala['Date']=='26-07-2021']
    kerala_con=kerala_date['Confirmed']
    kerala_c=kerala_rate['Confirmed']
    k_confirmed=max(kerala_con)
    k_con=max(kerala_c)
    diff=k_confirmed-k_con
    doubling=k_confirmed/diff
    doubling_rate=doubling*7
    return s,doubling_rate
output=[]
for i in new:
    if i not in exp:
        x=double_func(s=i)
        output.append(x)
output_series=pd.Series(output)
output_series.to_csv('C:/Users/hp/Desktop/OutputCovid/output.csv')