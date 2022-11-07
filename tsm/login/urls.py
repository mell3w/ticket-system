from django.urls import path

from .views import TSLoginView, TSLogoutView

app_name = 'login'
urlpatterns = [
    path('login/', TSLoginView.as_view(), name='login'),
    path('logout/', TSLogoutView.as_view(), name='logout'),
]