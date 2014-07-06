from django.http import HttpResponse
from django.shortcuts import render,render_to_response
def home(request):
	a=5
	b=6
	c=a+b
	return render(request,'index.html',locals())


# Create your views here.
