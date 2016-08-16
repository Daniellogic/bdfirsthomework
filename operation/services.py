from django.http import JsonResponse
import requests

def externalSumar(number_a, number_b):
    url='https://django-bigdata-daniellogic.c9users.io/sumar/'
    params = {'number_a': number_a,'number_b': number_b}
    r = requests.get(url, params=params)
    #r.write("External")
    return r
