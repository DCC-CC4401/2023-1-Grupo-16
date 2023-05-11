from django.shortcuts import render
from django.template import Template, Context
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def home(request):
    home=loader.get_template('home.html')
    home=home.render()
    return HttpResponse(home)

def log_in(request):
    log_in=loader.get_template('logIn.html')
    log_in=log_in.render()
    return HttpResponse(log_in)

def sign_up(request):
    sign_up=loader.get_template('signUp.html')
    sign_up=sign_up.render()
    return HttpResponse(sign_up)