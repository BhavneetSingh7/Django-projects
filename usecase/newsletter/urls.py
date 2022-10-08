from django.urls import path
from . import views

app_name = 'newsletter'
urlpatterns = [
    path('',views.index,name='newsletter'),
    path('check/',views.check,name='newsletter_check'),
    path('<str:subscriber>/<str:verify_key>/',views.verification,name='newsletter_verify'),
    path('<str:subscriber>/<str:verify_key>/unsubscribe/',views.unsubscribe,name='newsletter_unsubscribe'),
]
