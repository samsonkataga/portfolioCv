from django.shortcuts import render,redirect,get_object_or_404
from myportfolio import *

# Create your views here.

def portfolio(request):
	return render(request, 'myportfolio/portfolio.html')
