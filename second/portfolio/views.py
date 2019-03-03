from django.shortcuts import render, redirect
from .models import Portfolio

# Create your views here.
def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolios': portfolios})

def new(request):
    return render(request, 'portfolio/new.html')

def create(request):
    portfolio = Portfolio()
    portfolio.image = request.POST['image']
    portfolio.title = request.POST['title']
    portfolio.description = request.POST['description']
    # portfolio.pub_date = timezone.datetime.now()
    portfolio.save()
    return redirect('portfolio')
