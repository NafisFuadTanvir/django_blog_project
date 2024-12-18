from django.db import models
from django.contrib.auth.models import User


#make your models here

class Userprofile(models.Model):
    user=models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    profile_picture= models.ImageField(upload_to="profile_pics")
