#!/usr/bin/env python3

import csv



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

with open("file.csv", "w+") as csv_file:
    csv_writer = csv.writer(csv_file)
    # write column names
    csv_writer.writerow(data[0].keys())
    # iterate over data dicts and write values
    for dict_item in data:
        csv_writer.writerow(dict_item.values())

file = open("file.csv")
onstring = file.read().split("\n")[:-1]
dict = dict()

for item in onstring:
    key = item.split(" ")[0]
    value = item.split(" ")[1:]
    dict[key] = value

file.close()

print(dict)
