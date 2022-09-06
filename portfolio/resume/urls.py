from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from .views import myview

urlpatterns = [
    path('',myview.as_view())
]