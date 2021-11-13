from .views import first
from django.urls import path

urlpatterns = [
    path('', first, name='first'),

]