from django.urls import path

from .views import index

app_name = 'ticketSystem'
urlpatterns = [
    path('', index, name='index')
]