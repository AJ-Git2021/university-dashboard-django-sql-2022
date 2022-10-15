from django.urls import path,include
from uploads.views import home

urlpatterns = [
    path('', home, name='home-page'),
    # path('',include())
]
