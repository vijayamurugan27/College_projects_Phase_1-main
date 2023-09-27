from django.shortcuts import render, redirect

from .models import StudentDetails
from .forms import StudentDetailsForm

from django.urls import reverse_lazy

# Create your views here.
def home(request):
    student = StudentDetails.objects.all()
    context = {'student':student}
    return render(request, 'library/home.html', context)
    # return redirect(reverse_lazy("library:home")) 



from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class Forms(CreateView):
    model = StudentDetails
    fields = "__all__"
    template_name = 'library/cbv/forms.html'
    success_url = '/'

class StudentList(ListView):
    model = StudentDetails
    template_name = 'library/cbv/stulist.html'

class StudentDetail(DetailView):
    model = StudentDetails
    template_name = 'library/cbv/studetail.html'

class StudentUpdate(UpdateView):
    model = StudentDetails
    fields = '__all__'
    template_name = 'library/cbv/stuupdate.html'
    success_url = '/'

class StudentDelete(DeleteView):
    model = StudentDetails
    template_name = 'library/cbv/studelete.html'
    success_url = '/'