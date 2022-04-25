from django.shortcuts import render
from .models import Topic
# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')


def topics(request):
    topics = Topic.objects.all()


    context = {'topics': topics}
    ##WHATEVER YOU USE AS A KEY IN THIS DICTIONARY IS USED IN HTML FILE, THE VALUE IS USED IN THE VIEW FILE
    
    return render(request, 'MainApp/topics.html', context)