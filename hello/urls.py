from . import views
#from .views import first
from django.urls import path

urlpatterns = [
    path('', views.first, name='first')
    


    

]