from django.db import models

class Userinfo(models.Model):
    username=models.CharField(max_length=65)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=65)


# class Roles(models.Model):
#     roles=models.CharField(max_length=65)
#     user=models.ManyToManyField(Userinfo)






