from django.db import models

class Userinfo(models.Model):
    """create a class for userinfo for resistration"""
    username=models.CharField(max_length=65)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=65)


class Roles(models.Model):
    """create class for roles"""
    roles=models.CharField(max_length=65)
    user=models.ForeignKey(Userinfo,on_delete=models.CASCADE,related_name='roles',null=True)






