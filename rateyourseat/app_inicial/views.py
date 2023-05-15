from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template
from app_inicial.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout

"""
home view: principal page
Args: request
Returns: HttpResponse
"""
def home(request):
    if request.method=='GET':
        return render(request, "app_inicial/home.html")


"""
log_in view: log in page
Args: request
Returns: HttpResponse
"""
def log_in(request):
    if request.method == 'GET':
        return render(request,"app_inicial/logIn.html")
    if request.method == 'POST':
        username=request.POST['username']
        contraseña=request.POST['contraseña']
        usuario= authenticate(username=username,password=contraseña)
        if usuario is not None:
            login(request,usuario)
            return HttpResponseRedirect('/home')
        else:
            return HttpResponseRedirect('/signUp')
        
    #log_in=get_template('logIn.html')
    #log_in=log_in.render()
    #return HttpResponse(log_in)


"""
log_out view: log out page
Args: request
Returns: HttpResponse
"""
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/home')


"""
sign_up view: sign up page
Args: request
Returns: HttpResponse
"""
def sign_up(request):
    if request.method == 'GET':
        return render(request,"app_inicial/signUp.html")
    if request.method=='POST':
        nombre= request.POST['usuario']
        email= request.POST['email']
        contraseña= request.POST['password']
        user= User.objects.create_user(username=nombre, password=contraseña, email=email)
        return HttpResponseRedirect('/home')
                    
    #sign_up=get_template('signUp.html')
    #sign_up=sign_up.render()
    #return HttpResponse(sign_up)