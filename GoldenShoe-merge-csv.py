# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 13:44:45 2020

@author: kuris
"""
import GoldenShoe
import pandas as pd
import glob
import datetime
now = datetime.datetime.now()
fname = now.strftime('%Y%m%d')

files = glob.glob('C:\\Users\\kuris\\python\\data\\' + fname + '\\*' + fname + '.csv')

dataframes = []

for file in files:
    league = file.split('-')[0]
    print (league)
    df = pd.read_csv(file)
    dataframes.append(df)

join = pd.concat(dataframes)
join = join.sort_values(by='ポイント', ascending=False)
#join.to_csv('C:\\Users\\kuris\\python\\data\\' + fname + '\\Merged' + '-' + now.strftime('%Y%m%d') + '.csv')
#allduplicate = join.loc[join.名前.duplicated(keep=False),:]
#alldupsorted = allduplicate.sort_values(by='名前')
#alldupsorted.to_csv('C:\\Users\\kuris\\python\\data\\' + fname + '\\duplicate' + '-' + now.strftime('%Y%m%d') + '.csv')

filt = (join['名前'] == 'Erling Braut Haaland')

df1 = join[filt]


df11 = df1.loc[df1.名前.duplicated(keep='first')]
df12 = df1.loc[df1.名前.duplicated(keep='last')]

df11.set_index('所属チーム', inplace=True)
df12.set_index('所属チーム', inplace=True)
df12.loc['Dortmund(Germany)', 'ポイント']= df12.loc['Dortmund(Germany)', 'ポイント'] + df11.loc['Salzburg(Austria)', 'ポイント']
df11.reset_index(inplace=True)
df12.reset_index(inplace=True)
df12.loc[0,'所属チーム'] = df12.loc[0,'所属チーム'] + '/' + df11.loc[0,'所属チーム'] 
join.drop(index=join[filt].index, inplace=True)
df100 = join.append(df12, sort=False)
df100.sort_values(by='ポイント', ascending=False, inplace=True)
final = df100[['名前', '所属チーム','ゴール数','ポイント']].head(40)
final['順位'] = final['ポイント'].rank(ascending=False, method='min')
final.to_csv('C:\\Users\\kuris\\python\\data\\' + fname + '\\' + 'final-'+ fname + '.csv')


#first1 = join.loc[join.名前.duplicated(keep='first'), :]
#second1 = join.loc[join.名前.duplicated(keep='last'), :]
#
#first = first1.sort_values(by='名前')
#second = second1.sort_values(by='名前')
#n1 = first.set_index('名前')
#n2 = second.set_index('名前')

#s = n1['ゴール数'] + n2['ゴール数'] 
#print (first)
#print (second)
#first.to_csv('first_name_sorted.csv')   
#second.to_csv('second_name_sorted.csv')
#n1.to_csv
#a1 = first1.loc[first1.名前.duplicated(keep='first'),:]
#a2 = first1.loc[first1.名前.duplicated(keep='last'),:]
#b1 = second1.loc[second1.名前.duplicated(keep='first'),:]
#b2 = second1.loc[second1.名前.duplicated(keep='last'),:]

#a1.to_csv('a1.csv')
#a2.to_csv('a2.csv')
#b1.to_csv('b1.csv')
#b2.to_csv('b2.csv')    



