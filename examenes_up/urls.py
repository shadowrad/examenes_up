"""examenes_up URL Configuration

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
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from generador_pdf import views as view_generador
from preguntas import views

router = routers.DefaultRouter()
router.register(r'preguntas', views.PreguntaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    path('parcial-ean/', view_generador.parcial_ean),
    path('parcial-up/', view_generador.parcial_up),
]

admin.site.site_header = "Examenes Admin"
admin.site.site_title = "Examenes Admin Portal"
admin.site.index_title = "Bienvenido al portal de Examenes"
