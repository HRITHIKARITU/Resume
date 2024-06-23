from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=110)
    email = models.EmailField()
    phone = models.CharField(max_length=110)
    address = models.TextField()
    summary = models.TextField()
    
class Experience(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='experience')
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

class Education(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='education')
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    
class Skill(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='skills')
    name = models.CharField(max_length=200)

