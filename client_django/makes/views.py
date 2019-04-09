from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("You have reached the index")

def read(request):
    #return HttpResponse("You have reached read)

    context = {'temp': "John"}

    return render(request, 'read.html', context)