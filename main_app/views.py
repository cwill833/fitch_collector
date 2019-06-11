from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fintch
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def fintch_index(request):
    birds = Fintch.objects.all()
    return render(request, 'fintch/index.html', {'birds': birds})

def fintch_detail(request, fintch_id):
    bird = Fintch.objects.get(id=fintch_id)
    return render(request, 'fintch/detail.html', {'bird': bird})

class FintchCreate(CreateView):
    model = Fintch
    fields = '__all__'
    success_url = '/fintch/'

class FintchUpdate(UpdateView):
    model = Fintch
    fields = ['breed', 'description', 'age']

class FintchDelete(DeleteView):
    model = Fintch
    success_url = '/fintch/'