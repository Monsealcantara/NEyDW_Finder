# apps/notifications/urls.py
from django.urls import path
from . import views

app_name = 'notifications'

urlpatterns = [
    path('', views.notification_list, name='notification_list'),
    path('mark-as-read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
]
