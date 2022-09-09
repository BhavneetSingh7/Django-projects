from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.index,name='list'),
    path('todo/task/<str:pk>/',views.updateTask,name='Update'),
    path('todo/delete/<str:pk>/',views.deleteTask,name='Delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)