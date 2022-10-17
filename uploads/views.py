from multiprocessing import context
from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
        data = Student.objects.all()
        context = {"data":data} 
        return render(request, 'uploads/base.html', context)
