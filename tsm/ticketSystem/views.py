from django.shortcuts import render, get_object_or_404, redirect
from .models import Applications
from login.models import AdvUser
from .forms import ChangeAppForm


# Create your views here.

def index(request):
    context = {}
    if request.user.is_anonymous == False:
        open_apps = Applications.objects.filter(master=request.user)
        context = {'open_apps':open_apps}
    return render(request, 'ticketSystem/index.html', context)



