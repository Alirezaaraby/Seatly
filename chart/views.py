from django.shortcuts import render

from urlhandler.views import  Data

def my_view(request):
    data = Data.objects.all()
    return render(request, 'preview.html', {'data': data})
def index(request):
    return render(request, 'index.html', {})