from multiprocessing import context
from django.shortcuts import render
from .models import Task
# Create your views here.
def home(request):
        data = Task.objects.all()
        context = {"data":data} 
        return render(request, 'uploads/index.html', context)
