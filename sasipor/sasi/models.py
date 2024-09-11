from django.db import models

# Create your models here.
class Student(models.Model):
    RollNumber=models.CharField(max_length=30)
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    PhoneNumber=models.BigIntegerField()
    Course=models.CharField(max_length=10)
    Year=models.IntegerField()
    Gender=models.CharField(max_length=8)
    City=models.CharField(max_length=30)
    State=models.CharField(max_length=30)
class Results(models.Model):
    RollNumber=models.CharField(max_length=30)
    Telugu=models.IntegerField()
    Hindi=models.IntegerField()
    English=models.IntegerField()
    Maths=models.IntegerField()
    Physics=models.IntegerField()
    Chemistry=models.IntegerField()
    Science=models.IntegerField()
    Social=models.IntegerField()


