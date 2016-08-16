from django.http import JsonResponse
import requests

def externalSumar(number_a, number_b):
    url='https://django-bigdata-daniellogic.c9users.io/sumar/'
    params = {'number_a': number_a,'number_b': number_b}
    r = requests.get(url, params=params)
    #r.write("External")
    return r
    
def externalRestar(number_a, number_b):
    url='https://django-bigdata-daniellogic.c9users.io/restar/'
    params = {'number_a': number_a,'number_b': number_b}
    r = requests.get(url, params=params)
    #r.write("External")
    return r
    
def externalPotencia(number_a, number_b):
    url='https://django-bigdata-daniellogic.c9users.io/potencia/'
    params = {'number_a': number_a,'number_b': number_b}
    r = requests.get(url, params=params)
    #r.write("External")
    return r
