
from Newapp.views import RegisterAPI,ChangePasswordView
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
#from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    url(r'^auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token)
    ]
