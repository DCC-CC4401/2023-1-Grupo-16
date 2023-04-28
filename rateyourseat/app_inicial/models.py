from django.db import models

# Create your models here.

#User (provisional due to how the password will be implemented)
class User(models.Model):
        name = models.CharField(max_length=20)
        email = models.EmailField()
        password = models.CharField(max_length=50) #placeholder

class Review(models.Model):
        user = models.ForeignKey('User', on_delete=models.CASCADE)
        concert = models.ForeignKey('Concert', on_delete=models.CASCADE) #opcional
        content = models.TextField()                #models.CharField(max_length=500)
        #foto
        sit_sector = models.CharField(max_length=15)
        stars = models.PositiveSmallIntegerField()          #models.IntegerField()
        up_votes = models.PositiveSmallIntegerField()
        down_votes = models.PositiveSmallIntegerField()
        date = models.DateTimeField()

class Comment(models.Model):
        user = models.ForeignKey('User', on_delete=models.CASCADE)
        content = models.TextField()                #models.CharField(max_length=500)
        review = models.ForeignKey('Review', on_delete=models.CASCADE)
        date = models.DateTimeField()
        

class Concert(models.Model):
        title = models.CharField(max_length=100)
        artist = models.CharField(max_length=100)
        date = models.DateField()
        location = models.ForeignKey('Location', on_delete=models.CASCADE)

class Location(models.Model):
        name = models.CharField(max_length=100)
        address = models.CharField(max_length=200)
        city = models.CharField(max_length=100)
        country = models.CharField(max_length=100)

class Vote_Comment(models.Model):
        user = models.ForeignKey('User', on_delete=models.CASCADE)
        comment = models.ForeignKey('Comment', on_delete=models.CASCADE)
        is_positive = models.BooleanField()

class Vote_Review(models.Model):
        user = models.ForeignKey('User', on_delete=models.CASCADE)
        review = models.ForeignKey('Review', on_delete=models.CASCADE)
        is_positive = models.BooleanField()