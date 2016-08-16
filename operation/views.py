from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from decimal import Decimal
from django.http import JsonResponse

# Create your views here.
# Create your views here.

import services

import time
from django.http import StreamingHttpResponse

def stream_response(request):
    try:
        number_a = Decimal(request.GET['number_a'])
        number_b =  Decimal(request.GET['number_b'])
    except:
        return HttpResponse("Exception")
    resp = StreamingHttpResponse(stream_response_generator(number_a, number_b))
    return resp

def stream_response_generator(number_a, number_b):
    cont = 0
    res = 1
    while (cont < number_b) :
        res = res * number_a
        yield '{} <br /> {}'.format(res, ' ')
        cont = cont + 1
        time.sleep(0.2)

def home(request):  
    #return render_to_response("sumar.html", RequestContext(request))
    return render(request,"sumar.html")

def sumar(request):
    try:
        number_a = Decimal(request.GET['number_a'])
        number_b =  Decimal(request.GET['number_b'])
        response = number_a + number_b
    except:
        return HttpResponse("Exception")
    data = {'result':response}
    return JsonResponse(data)
    
def sumarext(request):
    try:
        number_a = Decimal(request.GET['number_a'])
        number_b =  Decimal(request.GET['number_b'])
        response = services.externalSumar(number_a,number_b).json()
    except:
        return HttpResponse("Exception, is the worker down?")
    return render(request,'answer.html',{'answer':response['result']})
    
def restar(request):
    try:
        number_a = Decimal(request.GET['number_a'])
        number_b=  Decimal(request.GET['number_b'])
        response = number_a - number_b
    except:
        print("exception")
        return HttpResponse("Exception")
        #return render(request,'answer.html',{'answer':response})
    #return render(request,'answer.html',{'answer':response})
    data = {'result':response}
    return JsonResponse(data)
    
def restarext(request):
    try:
        number_a = Decimal(request.POST['number_a'])
        number_b = Decimal(request.POST['number_b'])
        response = services.externalRestar(number_a,number_b).json()
    except:
        return HttpResponse("Exception, is the worker down?")
    return render(request,'answer.html',{'answer':response['result']})
        

def potencia(request):
    try:
        number_a = Decimal(request.GET['number_a'])
        number_b=  Decimal(request.GET['number_b'])
        response = number_a ** number_b
    except:
        return HttpResponse("Exception")
    data = {'result':response}
    return JsonResponse(data)
    
def potenciaext(request):
    try:
        number_a = Decimal(request.GET['number_a'])
        number_b = Decimal(request.GET['number_b'])
        response = services.externalPotencia(number_a,number_b).json()
    except:
        return HttpResponse("Exception, is the worker down?")
    return render(request,'answer.html',{'answer':response['result']})
