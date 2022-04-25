from django.urls import path

from . import views

app_name = 'MainApp'


urlpatterns = [
    path('', views.index, name = 'index'),
    path('topics', views.topics, name='topics'),
]