from django.urls import path,include
from uploads.views import analysis, home,questionAnswerView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',home, name='home-page'),
    path('question_ans/',questionAnswerView, name='question-ans-page'),
    path('analysis/',analysis, name='marks-analysis'),

    # path('',include())
]
