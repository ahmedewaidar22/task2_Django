from django.db import models

# Create your models here.
class Intake(models.Model):#ORM
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=70)

class Track(models.Model):
    name = models.CharField(max_length=40)


class Trainee(models.Model):
    name = models.CharField(max_length=40)
    track_name = models.ForeignKey(Track, on_delete=models.CASCADE)