from .models import *
from django.forms import ModelForm

class UploadBookForm(ModelForm):
    class Meta:
        model = EBooksModel
        fields = ('title', 'csv',)
