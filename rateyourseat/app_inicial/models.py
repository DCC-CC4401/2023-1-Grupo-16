from django.db import models

# Create your models here.
class Reviews(models.Model):
        content=models.CharField(max_length=500)
        sit_sector=models.CharField(max_length=15)
        stars=models.IntegerField()
        up_votes=models.IntegerField()
        down_votes=models.IntegerField()
        #author=models.Users()
        date=models.DateTimeField()
        #fotos 

class Coments(models.Model):
        content=models.CharField(max_length=250)
        author=models.Object()
        #father_review=models.Reviews()
        date=models.DateTimeField()
        
