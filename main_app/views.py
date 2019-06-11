from django.shortcuts import render
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