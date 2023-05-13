from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#User (provisional due to how the password will be implemented)
class User(AbstractUser):
        nick = models.CharField(max_length=20)

#Review Table with user,concert,content,photo,sit_sector,stars,up_votes,down_votes,date
class Review(models.Model):
        user = models.ForeignKey('User', on_delete=models.CASCADE)
        concert = models.ForeignKey('Concert', on_delete=models.CASCADE) #opcional
        content = models.TextField(max_length=500)
        photo = models.ImageField()
        sit_sector = models.CharField(max_length=15)
        stars = models.PositiveSmallIntegerField()
        up_votes = models.PositiveSmallIntegerField()
        down_votes = models.PositiveSmallIntegerField()
        date = models.DateTimeField()

#Comment table with user,content,review,date
class Comment(models.Model):
        user = models.ForeignKey('User', on_delete=models.CASCADE)
        content = models.TextField()                #models.CharField(max_length=500)
        review = models.ForeignKey('Review', on_delete=models.CASCADE)
        date = models.DateTimeField()
        
#Concert table with title,artist,date,location
class Concert(models.Model):
        title = models.CharField(max_length=100)
        artist = models.CharField(max_length=100)
        date = models.DateField()
        location = models.ForeignKey('Location', on_delete=models.CASCADE)

#Location table with name,addres,city,country
class Location(models.Model):
        name = models.CharField(max_length=100)
        address = models.CharField(max_length=200)
        city = models.CharField(max_length=100)
        country = models.CharField(max_length=100)

#Vote_Comment table with user,comment,is_positive
class Vote_Comment(models.Model):
        user = models.ForeignKey('User', on_delete=models.CASCADE)
        comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
        is_positive = models.BooleanField()

#Cote_Review table with user,review,is_positive
class Vote_Review(models.Model):
        user = models.ForeignKey('User', on_delete=models.CASCADE)
        review = models.ForeignKey('Review', on_delete=models.CASCADE)
        is_positive = models.BooleanField()