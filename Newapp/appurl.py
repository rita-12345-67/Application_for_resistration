from rest_framework.routers import SimpleRouter
from Newapp.views import Userview
simple=SimpleRouter()

simple.register('Signup',Userview)
urlpatterns=simple.urls
