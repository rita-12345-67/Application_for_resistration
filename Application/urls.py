
from Newapp.views import Userview
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('Newapp.appurl'))
]
