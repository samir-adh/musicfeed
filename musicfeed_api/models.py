from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)

class Artist(models.Model):
    name = models.CharField(max_length=255)
    deezer_id = models.IntegerField()
    
class Record(models.Model):
    deezer_id = models.IntegerField()
    title = models.CharField(max_length=255)
    record_type = models.CharField(max_length=255)
    release_date = models.DateField()
    
