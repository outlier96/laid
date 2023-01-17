from django.shortcuts import render
from django.http import HttpResponseRedirect

 
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')
def inner(request):
    return render(request, 'main/inner.html')
def portfolio(request):
    return render(request, 'main/portfolio.html')


