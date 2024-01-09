from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to ='profile_pics')
    

    def __str__(self) -> str:
        return self.user.username


class moviesave(models.Model):
    user = models.CharField(max_length=100)
    ids = models.CharField(max_length=100)
    type = models.CharField(max_length=100,null=True)
    title = models.CharField(max_length=200,null=True)
    overview = models.TextField(null=True)

    def __str__(self) -> str:
        return self.type
