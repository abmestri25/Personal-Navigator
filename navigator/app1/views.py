from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def navigate(request):
    return render(request,'navigate.html')

