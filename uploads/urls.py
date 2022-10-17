from django.urls import path,include
from uploads.views import home
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',home, name='home-page'),
    # path('',include())
]
