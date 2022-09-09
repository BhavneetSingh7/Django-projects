from django.urls import path
from . import views

app_name = 'linreg'
urlpatterns = [
    path('',views.index,name='index'),
]