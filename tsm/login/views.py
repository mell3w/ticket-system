from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


class TSLoginView(LoginView):
    template_name = 'ticketSystem/login.html'

class TSLogoutView(LogoutView):
    template_name = 'ticketSystem/index.html'


