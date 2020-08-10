# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:15:08 2020

@author: ztand
"""


import json
import urllib.request
import tkinter as tk
import time

root = tk.Tk()
root.title("Desktop MLB Ticker")
root.geometry('600x400')
frame = tk.Frame(root, bg = '#000066')
frame.place(relwidth = 1, relheight =1)


urllib.request.urlopen('https://api.sportsdata.io/v3/mlb/scores/json/Standings/2020?key=b39e49ef26924224a3eaf68f3dd88250').read()
response = urllib.request.urlopen('https://api.sportsdata.io/v3/mlb/scores/json/Standings/2020?key=b39e49ef26924224a3eaf68f3dd88250').read()

json_obj = str(response, 'utf-8')

data = json.loads(json_obj)

mytext = tk.Label(root,
               text='Sports\nTicker',
               width=600,
               height=400,
               bg="orange",
               fg="white",
               font=("Verdana",20))

mlbteams = [];


class Team:
   def __init__(self, name, city,wins,losses, league, division, winpct):
        self.name = name
        self.city = city
        self.wins = wins
        self.losses= losses
        self.league = league
        self.division = division
        self.winpct = winpct

for item in data:
    wins = str(item['Wins'])
    city = str(item['City'])
    name = str (item['Name'])
    losses = str(item['Losses'])
    league = str(item['League'])
    division = str(item['Division'])
    winpct = str(item['Percentage'])
    a = Team(name, city, wins,losses, league,division,winpct)
    mlbteams.append(a)

#for obj in mlbteams:
   # print("Team: " + obj.city + ' ' +  obj.name)
    #print("Record: " + obj.wins+ ' - ' + obj.losses)

americanleague = []
nationalleague = []
aleast = []
alcentral = []
alwest = []
nleast = []
nlwest = []
nlcentral = []

for obj in mlbteams:
    if obj.league == 'AL':
        americanleague.append(obj)
        if obj.division == 'East':
            aleast.append(obj)
        elif obj.division == 'Central':
            alcentral.append(obj)
        else:
            alwest.append(obj)
    else:
        nationalleague.append(obj)
        if obj.division == 'East':
            nleast.append(obj)
        elif obj.division == 'Central':
            nlcentral.append(obj)
        else:
            nlwest.append(obj)

txt = ''


x = True
while x == True:
    i = 1
    if i==1:
        txt = 'AL East \n'
        z = 1
        for item in aleast:
            y = (str(z) + ' - ' + item.city + ' ' + item.name + ': ' + item.wins + ' - ' + item.losses + '\n')
            txt = txt+y
            z+=1
        mytext.config(text=txt,bg="#00004D")
        mytext.pack()
        root.update()
        time.sleep(10)
        i+=1
        
    if i ==2:
        txt = 'Al Central \n'
        z = 1
        for item in alcentral:
            y = (str(z) + ' - ' + item.city + ' ' + item.name + ': ' + item.wins + ' - ' + item.losses + '\n')
            txt = txt+y
            z+=1
        mytext.config(text=txt,bg="#00004D")
        mytext.pack()
        root.update()
        time.sleep(10)
        i+=1
    
    if i ==3:
        txt = 'Al West \n'
        z = 1
        for item in alwest:
                y = (str(z) + ' - ' + item.city + ' ' + item.name + ': ' + item.wins + ' - ' + item.losses + '\n')
                txt = txt+y
                z+=1
        mytext.config(text=txt,bg="#00004D")
        mytext.pack()
        root.update()
        time.sleep(10)
        i+=1
    
    if i ==4:
        txt = 'NL East \n'
        z = 1
        for item in nleast:
            y = (str(z) + ' - ' + item.city + ' ' + item.name + ': ' + item.wins + ' - ' + item.losses + '\n')
            txt = txt+y
            z+=1
        mytext.config(text=txt,bg="#00004D")
        mytext.pack()
        root.update()
        time.sleep(10)
        i+=1
    
    if i ==5:
        txt = 'NL Central \n'
        z = 1
        for item in nlcentral:
            y = (str(z) + ' - ' + item.city + ' ' + item.name + ': ' + item.wins + ' - ' + item.losses + '\n')
            txt = txt+y
            z+=1
        mytext.config(text=txt,bg="#00004D")
        mytext.pack()
        root.update()
        time.sleep(10)
        i+=1
    
    if i ==6:
        txt = 'NL West \n'
        z = 1
        for item in nlwest:
            y = (str(z) + ' - ' + item.city + ' ' + item.name + ': ' + item.wins + ' - ' + item.losses + '\n')
            txt = txt+y
            z+=1
        mytext.config(text=txt,bg="#00004D")
        mytext.pack()
        root.update()
        time.sleep(10)
        i-5

root.mainloop()
    

    

    



    

    
    


    
    

        
