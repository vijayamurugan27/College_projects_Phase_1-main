from django.shortcuts import render, redirect
from demo.models import Project, Blog, Team, Contact
from demo.models import Course
from demo.forms import ContactForm



# Create your views here.
def home(request):
    course = Course.objects.all()
    training = Project.objects.all()
    # context = {'training': training, }
    context = { 'training': training,'course': course, }
    return render(request, 'demo/themes/home.html', context)

def about(request):
    team = Team.objects.all()
    context = {'team': team}
    return render(request, 'demo//themes/about.html', context)

def blog(request):
    blog = Blog.objects.all()
    context = {'blog': blog}
    return render(request, 'demo//themes/blog.html', context)

def portfolio(request):
    return render(request, 'demo//themes/portfolio.html')

def contact(request):    
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # name = form.cleaned_data.get('name')
            # email = form.cleaned_data.get('email')
            # mobile_number = form.cleaned_data.get('mobile_number')
            # college_name = form.cleaned_data.get('college_name')
            # msg = form.cleaned_data.get('msg')
            # return redirect('demo:portfolio')
            return redirect('/demo/home')
    context = {'form': form}
    return render(request, 'demo//themes/contact.html', context)
    # return render(request, 'demo//themes/contact.html')

def blogsingle(request, id):
    blog = Blog.objects.get(id = id)
    blog1= Blog.objects.all()
    context = {'blog': blog, 'blog1': blog1}
    return render(request, 'demo//themes/blogsingle.html', context)

def training(request):
    training = Project.objects.all()
    # context = {'training': training}
    course = Course.objects.all()
    context = {'training': training, 'course': course}
    return render(request, 'demo//themes/training.html', context)



def trainingdetails(request, id):
    training = Project.objects.get(id=id)
    context = {'training': training}
    course = Course.objects.all()
    context = {'training': training, 'course': course}
    return render(request, 'demo//themes/trainingdetails.html', context)

from django.views.generic import CreateView,  UpdateView

class TrainerCreateView(CreateView):
    model = Team
    fields = '__all__'
    template_name = 'demo/themes/cbv/create.html'
    success_url = '/demo/home'

class TrainerUpdateView(UpdateView):
    model = Team
    fields = '__all__'
    template_name = 'demo/themes/cbv/update.html'
    success_url = '/demo/home'
    
class TrainingUpdateView(UpdateView):
    model = Project
    fields = '__all__'
    template_name = 'demo/themes/cbv/update.html'
    success_url = '/demo/home'

