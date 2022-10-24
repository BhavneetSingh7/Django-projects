from django.urls import path
from .views import *

urlpatterns = [
    path('<str:API_TOKEN>/',get_notes_list,name='notes_api'),
]