import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import AbstractUser

# Create your models here.
from rest_framework.authtoken.admin import User as User_inf

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
        on_delete=models.CASCADE, verbose_name=_("User")
    )
    password = models.CharField(max_length=654 ,default='12345' )
    uuid = models.CharField(unique=False, default=uuid.uuid1,max_length=350)
    ip =  models.CharField(max_length=120, null=True)
    phone =  models.CharField(max_length=120, null=True)
    location =  models.CharField(max_length=120, null=True)
    # is_visitor = models.BooleanField(default=True)
    is_client = models.BooleanField(default=True)
    is_eng = models.BooleanField(default=False)
    is_designer = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)



    def __str__(self):
        return self.user.email
    def inf(self):
        data =User_inf.objects.filter(id=1)
        return data.values()
