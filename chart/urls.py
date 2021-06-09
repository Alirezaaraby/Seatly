from django.urls import path
from . import views

urlpatterns = [
    path('preview', views.my_view, name='chart'),
    path('', views.index, name='home')
]