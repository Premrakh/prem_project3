from django.db import models

# Create your models here.
class Admin(models.Model):
    genders=[('male','male'),('female','female'),('other','other')]
    
    full_name= models.CharField(max_length=50)
    email=models.EmailField(unique=True,max_length=254)
    password=models.CharField(max_length=50)
    gender=models.CharField(choices=genders,max_length=20)
    Address=models.CharField(max_length=50)
    pic=models.FileField( upload_to='admin_pic', default='empty.png')
    
    def __str__(self):
        return self.full_name
class Member(models.Model):
    genders=[('male','male'),('female','female'),('other','other')]
    
    full_name= models.CharField(max_length=50)
    email=models.EmailField(unique=True,max_length=254)
    password=models.CharField(max_length=50)
    gender=models.CharField(choices=genders,max_length=20)
    Address=models.CharField(max_length=50)
    pic=models.FileField( upload_to='member_pic', default='empty.png')
    
    def __str__(self):
        return self.full_name
    
class Watchman(models.Model):
    types=[('morning','morning'),('night','night')]
    
    full_name= models.CharField(max_length=50)
    email=models.EmailField(unique=True,max_length=254)
    password=models.CharField(max_length=50)
    shift=models.CharField(choices=types,max_length=20)
    Address=models.CharField(max_length=50)
    pic=models.FileField( upload_to='member_pic', default='empty.png')
    
    def __str__(self):
        return self.full_name
    
class Event(models.Model):
    subject=models.CharField(max_length=50)
    message=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    
    def __str__(self):
        return self.subject
class Notice(models.Model):
    subject=models.CharField(max_length=50)
    notice=models.TextField()
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject