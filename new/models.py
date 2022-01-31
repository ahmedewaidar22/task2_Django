from django.db import models

# Create your models here.
class Intake(models.Model):#ORM
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=70)