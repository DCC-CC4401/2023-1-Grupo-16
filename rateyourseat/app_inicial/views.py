import datetime
from django.shortcuts import render, redirect
from django.template import Template, Context
from django.template.loader import get_template
from app_inicial.models import User, Review, Location, ReviewForm, Comment, Vote_Review
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.urls import reverse


"""
home view: principal page
Args: request
Returns: HttpResponse
"""
def home(request):
    is_logged = request.user.is_authenticated
    context = {
        'is_logged': is_logged,
        'current_page': 'home',
    }
    return render(request, 'app_inicial/home.html', context)
    

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
        user = User.objects.create_user(username=nombre, password=contraseña, email=email)
        login(request, user)
        context = {
            "is_logged": request.user.is_authenticated
        }
        return HttpResponseRedirect('/home', context)
                    

@login_required(login_url='/log_in')
def add_review(request):
    if request.method == 'GET':
        context = {
            "is_logged": request.user.is_authenticated,
            'current_page': 'add_review',
        }
        return render(request,"app_inicial/add_review.html", context)
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
        context = {
            'current_page': 'add_review'
        }
        return HttpResponseRedirect('/my_reviews', context)
    
@login_required(login_url='/log_in')
def my_reviews(request):
    reviews=Review.objects.filter(user_id=request.user.id)
    context = {
        "is_logged": request.user.is_authenticated, 
        "reviews": reviews,
        'current_page': 'my_reviews',
    }
    return render(request, 'app_inicial/my_reviews.html', context)

def reviews(request):
    is_logged = request.user.is_authenticated
    queryset = Review.objects.all()
    order = request.GET.get('order')
    venueFilter = request.GET.get('venueFilter', '')
    if venueFilter:
        queryset = queryset.filter(venue__name=venueFilter)
    if order == 'recent':
        queryset = queryset.order_by('-date')
    elif order == 'oldest':
        queryset = queryset.order_by('date')
    reviews = queryset.all()
    context = {
        'is_logged': is_logged,
        'all_reviews': reviews,
        'current_page': 'reviews',	
    }
    # Search review by artist or event
    concert = request.GET.get('searchReview')
    if concert:
        context['all_reviews'] = Review.objects.filter(concert__icontains=concert)
    return render(request, 'app_inicial/reviews.html', context)

def single_review(request,id):
    context = {
        "is_logged": request.user.is_authenticated,
        'current_page': 'reviews',
    }
    if not id:
        return HttpResponseRedirect('/reviews', context)
    
    review=Review.objects.get(id=id)
    if not review:
        return HttpResponseRedirect('/reviews', context)

    comments = Comment.objects.filter(review_id=id)

    if request.method == 'GET': 
        context = {
            'is_logged': request.user.is_authenticated,
            'single_review':review, 
            'comments':comments,
            'current_page': 'reviews',
        }
        return render(request, 'app_inicial/single_review.html', context)
    
    if request.method == 'POST':
        modify=request.POST['modify']
        if modify=="delete":
            Review.objects.filter(id=id).delete()
            context = {
                "is_logged": request.user.is_authenticated,
                'current_page': 'reviews',
            }
            return HttpResponseRedirect('/reviews', context)
        
        elif modify=="edit":
            concert = request.POST['event']
            content = request.POST['content']
            stars = request.POST['puntuacion']
            review.content=content
            review.concert=concert
            review.stars=stars
            review.save()
        
        elif modify=="comment":
            if request.user.is_authenticated: 
                comment_content = request.POST['comment-content']
                if comment_content!="":    
                    current_datetime = datetime.datetime.now()
                    user_id = request.user
                    review_id = review
                    comment = Comment(
                        user_id=user_id,
                        review_id=review_id,
                        content=comment_content,
                        date=current_datetime
                        )
                    comment.save()
                    
        elif modify=="delete_comment":
            comment_id=request.POST['comment-id']
            comment=Comment.objects.get(id=comment_id)
            if comment.user_id==request.user:    
                comment.delete()
        
        elif modify=="edit_comment":
            comment_id=request.POST['comment-id']
            comment_content_edit= request.POST['comment-content-edit']
            comment=Comment.objects.get(id=comment_id)
            if comment.user_id==request.user:
                comment.content=comment_content_edit
                comment.save()
        
        elif modify=="upvote":
            review_id=request.POST['review-id']
            if request.user.is_authenticated:
                review_id=request.POST['review-id']
                review=Review.objects.get(id=review_id)
                
                if Vote_Review.objects.filter(user_id=request.user, review_id=review_id).exists():
                    hasVoted=Vote_Review.objects.get(user_id=request.user, review_id=review_id)
                else:
                    hasVoted=Vote_Review(
                        user=request.user,
                        review=review,
                        is_positive=0
                        )
                
                if hasVoted.is_positive != 1:                
                    review.votes+=1
                    review.total_votes+=1
                    hasVoted.is_positive=1
                    hasVoted.save()
                    review.save()

        elif modify=="downvote":
            review_id=request.POST['review-id']
            if request.user.is_authenticated:
                review_id=request.POST['review-id']
                review=Review.objects.get(id=review_id)
                
                if Vote_Review.objects.filter(user_id=request.user, review_id=review_id).exists():
                    hasVoted=Vote_Review.objects.get(user_id=request.user, review_id=review_id)
                else:
                    hasVoted=Vote_Review(
                        user=request.user,
                        review=review,
                        is_positive=0
                        )
                
                if hasVoted.is_positive != -1:                
                    review.votes-=1
                    review.total_votes+=1
                    hasVoted.is_positive= (-1)
                    hasVoted.save()
                    review.save()
        
        context = {
            'is_logged': request.user.is_authenticated,
            'single_review':review, 
            'comments':comments,
            'current_page': 'reviews',
        }
        return HttpResponseRedirect('/single_review/'+id, context)
