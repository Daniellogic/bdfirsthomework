from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from decimal import Decimal

# Create your views here.
# Create your views here.

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
    return HttpResponse(response)
    
def restar(request):
    try:
        number_a = Decimal(request.POST['number_a'])
        number_b=  Decimal(request.POST['number_b'])
        response = number_a - number_b
    except:
        print("exception")
        return HttpResponse("Exception")
        #return render(request,'answer.html',{'answer':response})
    #return render(request,'answer.html',{'answer':response})
    return HttpResponse(response)
    
def potencia(request):
    try:
        number_a = Decimal(request.GET['number_a'])
        number_b=  Decimal(request.GET['number_b'])
        response = number_a ** number_b
    except:
        return HttpResponse("Exception")
    return HttpResponse(response)
