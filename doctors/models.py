from django.db import models

# Create your models here.
class demophy(models.Model):
    name=models.TextField(max_length=100)

class doctors(models.Model):
    name=models.TextField(max_length=100)
    specality=models.TextField(max_length=100)
    phone=models.TextField(unique=True,max_length=200)
    password=models.TextField(max_length=1000)
    gender=models.TextField()
    clinic_address=models.TextField()
    reg_time=models.DateTimeField(auto_now=True)

