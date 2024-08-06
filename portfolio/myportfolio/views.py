from django.shortcuts import render,redirect,get_object_or_404
from myportfolio import *
from .forms import *


# Create your views here.

def portfolio(request):
	form = ContactForm()
	if request.method == "POST":
		form = ContactForm(request.POST or none)
		if form.is_valid():
			form.save()
			return redirect("portfolio")
	context = {
        'form':form,
    }
	return render(request, 'myportfolio/portfolio.html', context)

	
