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




# class Role(models.Model):  # to assign roles
#     role = models.CharField(max_length=50)
#     active = models.CharField(max_length=50, default='Y')
#     userrefs = models.ManyToManyField(UserInfo)
#     activeRoles = ActiveRoles()
#     roles = models.Manager()
#
#     @staticmethod
#     def dummyrole():
#         return Role(role='staff')
#
#
# class LoginInfo(models.Model):  # to maintain credentails
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     tokenval = models.CharField(max_length=50)
#     userref = models.OneToOneField(UserInfo, models.CASCADE)





