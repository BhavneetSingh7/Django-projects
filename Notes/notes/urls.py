from django.urls import path
from .views import *

app_name = 'notes'
urlpatterns = [
    # User Authentication urls
    path('login/',user_login,name='login'),
    path('logout/',user_logout,name='logout'),
    path('signup/',register,name='register'),
    # CRUD operations urls
    path('',notes_list,name='notes_list'),
    path('update/<str:pk>',note_update,name='update'),
    path('detail/<str:pk>',note_detail,name='detail'),
    path('delete/<str:pk>',note_delete,name='delete'),
]