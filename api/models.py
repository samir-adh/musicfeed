from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, unique=True)

class Following(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    artist_id = models.IntegerField()



# class Artist(models.Model):
#     name = models.CharField(max_length=255)
#     deezer_id = models.IntegerField()
    
# class Record(models.Model):
#     deezer_id = models.IntegerField()
#     title = models.CharField(max_length=255)
#     record_type = models.CharField(max_length=255)
#     release_date = models.DateField()
    
