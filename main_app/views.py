from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def dashboard(request):
    return render(request, 'user/index.html')

def addDebt(request):
    return render(request, 'user/addDebt.html')