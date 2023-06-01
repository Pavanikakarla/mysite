from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>This is main page</h1>")
def login(request):
    context={'msg':'This is login page'}
    return render(request,'login.html',context)