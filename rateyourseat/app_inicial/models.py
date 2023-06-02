from django.db import models
from django.contrib.auth.models import AbstractUser

"""
User table with nick
Args: AbstractUser: username,first_name,last_name,email,password,groups,user_permissions,is_staff,is_active,is_superuser,last_login,date_joined
"""
class User(AbstractUser):
        nick = models.CharField(max_length=20)

"""
Review Table with user,concert,content,photo,sit_sector,stars,up_votes,down_votes,date
Args: models.Model
"""
class Review(models.Model):
        user = models.ForeignKey('User', on_delete=models.CASCADE)
        # concert = models.ForeignKey('Concert', on_delete=models.CASCADE, to_field='title') 
        concert = models.CharField(max_length=100)
        venue = models.ForeignKey('Location', on_delete=models.CASCADE, to_field='name')
        sit_sector = models.CharField(max_length=30)
        content = models.TextField(max_length=500)
        photo = models.ImageField(null=True, blank=True, upload_to='images/')
        stars = models.PositiveSmallIntegerField()
        up_votes = models.PositiveSmallIntegerField(default=0)
        down_votes = models.PositiveSmallIntegerField(default=0)
        date = models.DateTimeField()
        def __str__(self):
                return self.concert        

"""
Comment table with user,content,review,date 
Args: models.Model
"""
class Comment(models.Model):
        user_id = models.ForeignKey('User', on_delete=models.CASCADE)
        content = models.TextField()                #models.CharField(max_length=500)
        review_id = models.ForeignKey('Review', on_delete=models.CASCADE)
        date = models.DateTimeField()


"""
Concert table with title,artist,date,location
Args: models.Model
"""
class Concert(models.Model):
        title = models.CharField(max_length=100, unique=True)
        artist = models.CharField(max_length=100, null=True)
        date = models.DateField(null=True)
        location = models.ForeignKey('Location', on_delete=models.CASCADE, to_field='name')

"""
Location table with name,addres,city,country
Args: models.Model
"""
class Location(models.Model):
        name = models.CharField(max_length=100, unique=True)
        address = models.CharField(max_length=200, null=True)
        city = models.CharField(max_length=100, null=True)
        country = models.CharField(max_length=100, null=True)
        def __str__(self):
                return self.name

"""
#Vote_Comment table with user,comment,is_positive
Args: models.Model
"""
class Vote_Comment(models.Model):
        user_id = models.ForeignKey('User', on_delete=models.CASCADE)
        comment_id = models.ForeignKey('Comment', on_delete=models.CASCADE)
        is_positive = models.BooleanField()

"""
#Cote_Review table with user,review,is_positive
Args: models.Model
"""
class Vote_Review(models.Model):
        user = models.ForeignKey('User', on_delete=models.CASCADE)
        review = models.ForeignKey('Review', on_delete=models.CASCADE)
        is_positive = models.BooleanField()