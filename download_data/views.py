from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def BookUploadView(request):
    if request.method == 'POST':
        form = UploadBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = UploadBookForm()
        context = {
            'form':form,
        }
    return render(request, 'download_data/UploadBook.html', context)