from django.shortcuts import render
from .models import Portfolio
# Create your views here.


def homeView(request):
    portfolios = Portfolio.objects.all()

    return render(request, 'index.html', {"portfolios": portfolios})
