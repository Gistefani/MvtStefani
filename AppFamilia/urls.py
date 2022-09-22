from django.urls import path
from AppFamilia.views import *


urlpatterns = [
    path('', inicio),
    path('familia/', familia),
]