from django.shortcuts import render
from django.http import HttpResponse
import pickle

import json
import threading
import time
import os.path
import math
import pathlib
import pathlib




def get_data_sort_za(x):
    return x['name']
def get_data_sort_az(x):
    return x["name"]

def get_data_sort_up(x):
    return x['price']
def get_data_sort_down(x):
    return x['price']

def index(request):

    x= request.POST.get("name")
    xx = request.POST.get("select","az")

    data = [
            {"name": "дрель мини", "price": 1000, "img": "static\main\images\drel-pre.jpg"},
            {"name": "бур мини", "price": 2000, "img": "static\main\images\drel-pre.jpg"},
            {"name": "электроинструмент", "price": 2000, "img": "static\main\images\drel-pre.jpg"},
            {"name": "универсальный электроинструментрумент", "price": 4000, "img": "static\main\images\drel-pre.jpg"},
            {"name": "дрель мини", "price": 5000, "img": "static\main\images\drel-pre.jpg"},
            {"name": "ярель", "price": 6000, "img": "static\main\images\drel-pre.jpg"},
            {"name": "aрель", "price": 7000, "img": "static\main\images\drel-pre.jpg"},
            {"name": "брель", "price": 8000, "img": "static\main\images\drel-pre.jpg"},
            {"name": "брель", "price": 8000, "img": "static\main\images\drel-pre.jpg"},
            ]
    
    MyList = ["Самара", "Сочи", "Мурманск", "Анапа"] 

    MyFile = open ('output.txt', 'w+') 
    MyList = map (lambda x: x + '\ n', MyList) 
    MyFile.writelines (MyList) 
    MyFile.close()


    d0=[
        ]       
    d1=[
        ]
    d2=[
        ]
    d3=[
        ]
    d4=[
        ]       
    d5=[
        ]
    d6=[
        ]
    d7=[
        ]  
    d8=[
        ]  
        
    if(xx =='za'):    

        d = sorted(data, key=get_data_sort_za, reverse=True)
        d1=d[1]
        d2=d[2]
        d0=d[0]

        d3=d[3]
        d4=d[4]
        d5=d[5]

        d6=d[6]
        d7=d[7]
        d8=d[8]
    elif(xx == 'az'):    
        d = sorted(data, key=get_data_sort_az)

        d1=d[1]
        d2=d[2]
        d0=d[0]

        d3=d[3]
        d4=d[4]
        d5=d[5]

        d6=d[6]
        d7=d[7]
        d8=d[8]
    elif(xx=='up'):    
        d = sorted(data, key=get_data_sort_up)

        d1=d[1]
        d2=d[2]
        d0=d[0]

        d3=d[3]
        d4=d[4]
        d5=d[5]

        d6=d[6]
        d7=d[7]
        d8=d[8]
    elif(xx=='down'):    
        d = sorted(data, key=get_data_sort_down, reverse=True)

        d1=d[1]
        d2=d[2]
        d0=d[0]

        d3=d[3]
        d4=d[4]
        d5=d[5]

        d6=d[6]
        d7=d[7]
        d8=d[8]

    dt = dict([("0", d0),
                (1, d1),
                ("2", d2),
                ("3", d3),
                ("4", d4),
                ("5", d5),
                ("6", d6),
                ("7", d7),
                ("8", d8)
                ])

#'https://metanit.com/python/django/2.3.php'
    return render(request, "main\index.html", context=dt)






'''
def index(request):
    # получаем из строки запроса имя пользователя
    name = request.POST.get("name", "Undefined")
    if (name =="name"):
        f = open('text.txt', 'w+')
    return render(request, "main\index.html")
'''







'''
по цене вниз

def get_data_sort_za(x):
    return x['name'],-x['price'],x['img'],

data = [
        {"name": "дрель", "price": 1000, "img": 3},
        {"name": "дрель", "price": 2000, "img": 3},
        {"name": "дрель", "price": 3000, "img": 3},
]

data=sorted(data, key=get_data_sort_za)

print(data)

'''
