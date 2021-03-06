"""firsthomework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from operation import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^sumar/$', views.sumar, name = 'sumar'),
    url(r'^sumarext/$', views.sumarext, name = 'sumarext'),
    url(r'^restar/$', views.restar, name = 'restar'),
    url(r'^restarext/$', views.restarext, name = 'restarext'),
    url(r'^potencia/$', views.potencia, name = 'potencia'),
    url(r'^potenciaext/$', views.potenciaext, name = 'potenciaext'),
    url(r'^stream/$', views.stream_response, name = 'stream_response'),
    url(r'^admin/', admin.site.urls),
]
