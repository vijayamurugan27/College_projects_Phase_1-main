from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'landingpage/resume.html')

def resume(request):
    return render(request, 'landingpage/resume.html')