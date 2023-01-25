import uuid

from django.conf import settings
from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.
from rest_framework.authtoken.admin import User as User_inf

from project.models import Project

'''
visitor ip location info meeting phone 
client project name  meeting phone 
eng [projects] location ip phone [meeting] 
designer  [projects] location ip phone [meeting] 
manager *[projects] location ip phone *[meeting]  

'''

class User(models.Model):
    # name = models.CharField(max_length=120, null=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name='auth_user',
        on_delete=models.CASCADE, verbose_name=("User")
    )
    password = models.CharField(max_length=654 ,default='12345' )
    uuid = models.CharField(unique=False, default=uuid.uuid1,max_length=350)
    ip =  models.CharField(max_length=120, null=True)
    phone =  models.CharField(max_length=120, null=True)
    location =  models.CharField(max_length=120, null=True)
    pic = models.ImageField(upload_to="useres/%y", null=True)
    # is_visitor = models.BooleanField(default=True)
    is_client = models.BooleanField(default=True)
    is_eng = models.BooleanField(default=False)
    is_designer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)



    def __str__(self):
        return self.user.email
    def inf(self):
        data =User_inf.objects.filter(id=self.id)
        return data.values()
    def projec(self):
        data =Project.objects.filter(owner=self.user)
        return data.values()
    def project_percent(self):
        data =Project.objects.filter(owner=self.user).reverse()[0]
        lenght=     data.steps_count
        print(lenght,type(lenght))
        finshed_count =data.steps_countFinshed
        print(finshed_count,type(finshed_count))
        percent = finshed_count//lenght
        return  percent