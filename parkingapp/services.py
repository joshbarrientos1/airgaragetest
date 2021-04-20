from django.http import HttpResponse
from django.shortcuts import render
import requests
import json

def yelp_call(location):
    api_key='Bw_SyPaByh2ooQYQ7dPr8xwnc_gAAWL5GcLlBMpqFcRhk_ZdYDJDeJ3Xefnu9fC3wEX0dtL66BWWene-7nO4pAXoWwhFVrnR5wRYQb0Vl4GuME129DUrPCQClx5-YHYx'
    headers = {'Authorization': 'Bearer %s' % api_key}

    url='https://api.yelp.com/v3/businesses/search'
    params = {'term':'parking','location':location}

    req=requests.get(url, params=params, headers=headers)
    return(req.json())