import datetime
from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template
from app_inicial.models import User, Review, Location, ReviewForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


"""
home view: principal page
Args: request
Returns: HttpResponse
"""
def home(request):
    is_logged = request.user.is_authenticated
    return render(request, 'app_inicial/home.html', {'is_logged': is_logged})
    

"""
log_in view: log in page
Args: request
Returns: HttpResponse
"""
def log_in(request):
    if request.method == 'POST':
        nick=request.POST['username']
        contraseña=request.POST['password']
        usuario = authenticate(username=nick, password=contraseña)
        if usuario is not None:
            login(request,usuario)
            return HttpResponseRedirect('/home')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
            return HttpResponseRedirect('/log_in')
        
    return render(request,"app_inicial/logIn.html")

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
        if User.objects.filter(username=nombre).exists():
            #devolver al mismo login ojalá sin borrar la info ingresada con un mensaje que diga que ya existe ese username
            return render(request,"app_inicial/signUp.html", {"error":"El nombre de usario '"+nombre+"' ya existe, eliga uno diferente"})
        user= User.objects.create_user(username=nombre, password=contraseña, email=email)
        login(request, user)
        return HttpResponseRedirect('/home',{"is_logged": request.user.is_authenticated })
                    
    #sign_up=get_template('signUp.html')
    #sign_up=sign_up.render()
    #return HttpResponse(sign_up)

@login_required(login_url='/log_in')
def add_review(request):
    if request.method == 'GET':
        return render(request,"app_inicial/add_review.html", {"is_logged": request.user.is_authenticated })
    if request.method =='POST':
        user_id = request.user
        concert = request.POST['event']
        venue = Location.objects.get(name=request.POST['place-select'])
        sit_sector = request.POST['sit-select']
        content = request.POST['content']
        photo = None
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.cleaned_data.get("image")
        stars = request.POST['puntuacion']
        up_votes = 0
        down_votes = 0
        current_datetime = datetime.datetime.now()
        review = Review(
            user_id=user_id, 
            concert=concert, 
            venue=venue, 
            sit_sector=sit_sector, 
            content=content, 
            photo=photo, 
            stars=stars, 
            up_votes=up_votes, 
            down_votes=down_votes, 
            date=current_datetime)
        review.save()
        return HttpResponseRedirect('/my_reviews')
    
@login_required(login_url='/log_in')
def my_reviews(request):
    reviews=Review.objects.filter(user_id=request.user.id)
    return render(request, 'app_inicial/my_reviews.html', {"is_logged": request.user.is_authenticated, "reviews": reviews})


def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'app_inicial/reviews.html')