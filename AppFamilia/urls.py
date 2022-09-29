from django.urls import path
from AppFamilia.views import *


urlpatterns = [
    path('', inicio),
    path('familia/', familia),
    path('Amigos/', Amigos),
    path('Asistencia/', Asistencia)

]