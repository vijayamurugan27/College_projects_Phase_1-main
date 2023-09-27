from django.shortcuts import render
from photography.models import PhotoGraphy


# Create your views here.
def home(request):
    services = PhotoGraphy.objects.all()
    context = {'services': services }
    return render(request, 'photography/home.html', context)