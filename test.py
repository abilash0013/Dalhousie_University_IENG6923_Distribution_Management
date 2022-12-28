import csv
import json

import pandas as pd
import googlemaps
from itertools import tee

import requests


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)
def test1():
    df = pd.read_csv('test.csv')
    c=0
    dict_wor={}
    dict_list=[]
    df_marks = pd.DataFrame(dict_list)
    for (i1,row1), (i2, row2) in pairwise(df.iterrows()):

        loc = row1['Location']



        for (i1, row1), (i2, row2) in pairwise(df.iterrows()):
            list1=[]
            loc2 = row1['Location']
            index2 = row1['#patient No']
            c=c+1
            import urllib.parse
            origin = urllib.parse.quote(loc)
            dest = urllib.parse.quote(loc2)
            url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="+origin+"&destinations="+dest+"&key=AIzaSyAmhicKS1aPOYS21E8tTMx3ovkJtyPpI_s"

            payload = {}
            headers = {}

            response = requests.request("GET", url, headers=headers, data=payload)

            resp = json.loads(response.text)
            dict_wor[index2]=resp['rows'][0]['elements'][0]['distance']['text']
            list1.append(resp['rows'][0]['elements'][0]['distance']['text'])
            file = open('test1.txt', 'a')
            for items in list1:
                file.writelines(items + '\n')
            file.close()

if __name__ == '__main__':
    test1()