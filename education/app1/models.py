from django.db import models

# Create your models here.
class parent(models.Model):
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    email=models.CharField(max_length=40)
    stu_name=models.CharField(max_length=20)
    msg=models.CharField(max_length=20)

class contact(models.Model):
    name  =models.CharField(max_length=20)
    phone =models.IntegerField()
    email =models.CharField(max_length=40)
    msg   =models.CharField(max_length=20)