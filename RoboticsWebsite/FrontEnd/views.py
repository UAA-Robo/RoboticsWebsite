from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'FrontEnd/index.html')

def projects(request):
    return render(request, 'FrontEnd/projects.html')

def outreach(request):
    return render(request, 'FrontEnd/outreach.html')

def fund(request):
    return render(request, 'FrontEnd/fund.html')