# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 15:12:39 2020

@author: kuris
"""
import os
from requests_html import HTML,HTMLSession
import csv
import codecs
import datetime
now = datetime.datetime.now()
fname = now.strftime('%Y%m%d')
os.mkdir('C:\\Users\\kuris\\python\\data\\' + fname)






abbrevs = []
countries = []
ranking = []

with open('cabbrev.csv', 'r') as f:
    for i in f.readlines():
        abbrevs.append(i.split(',')[0])
        countries.append(i.split(',')[1])

with open('UefaRanking2020.csv', 'r') as f:
    for i in f.readlines():
        ranking.append(i.strip('\n'))



for abbrev, country in zip(abbrevs[1:],countries[1:]):
    url = f'https://www.uefa.com/memberassociations/association={abbrev[0:3]}/domesticleague/topscorers/index.html'
    #print (abbrev)
    #print (country)

    if '[n' in country.strip('\n'):
        title = country.strip('\n')[:-5]
        print (title)
    else:
        title = country.strip('\n')
        
        print (title)
    csv_file = open('C:\\Users\\kuris\\python\\data\\' + fname + '\\' + title + '-' + fname + '.csv', 'w', encoding='utf8', newline='')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['ゴール数','試合数','名前','所属チーム', 'ポイント'])
    session = HTMLSession()
    r = session.get(url)
    datas = r.html.find('tr')


    goal = []
    game = []
    name = []
    team = []

    for data in datas[1:]:
        datalist = data.text.split('\n')
        if datalist[0] == 'Date':
            break
        goal = int(datalist[0])
        game = int(codecs.encode(datalist[1]))
        name = datalist[2]
        team = datalist[3] + '(' + title + ')' 

        if title == ranking[0] or title == ranking[1] or title == ranking[2] or title == ranking[3] or title == ranking[4]:
            point = goal * 2

        elif title == ranking[5] or title == ranking[6] or title == ranking[7] or title == ranking[8] or title == ranking[9] or title == ranking[10] or title == ranking[11] or title == ranking[12] or title == ranking[13] or title == ranking[14] or title == ranking[15] or title == ranking[16] or title == ranking[17] or title == ranking[18] or title == ranking[19] or title == ranking[20]:
            point = goal * 1.5

        else:
            point = goal


        csv_writer.writerow([goal, game, name, team, point])

    csv_file.close()
    

