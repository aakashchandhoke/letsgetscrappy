from django.shortcuts import render
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import *
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from datetime import datetime,timedelta
import random,string

def home(request):
	if request.POST:
		name = request.POST['name']
		message = request.POST['message']
		email = request.POST['email']
		send_mail(email, name+ "\n" + message,"scrappy0089@gmail.com","scrappy0089@gmail.com".split(' '), fail_silently=False)
	return render_to_response('index.html',context_instance=RequestContext(request))

def greetings(request):
	return render_to_response('greeting.html')

def collage(request):
	return render_to_response('collages.html')

def scrapbook(request):
	return render_to_response('scrapbook.html')

def calendar(request):
	return render_to_response('calendar.html')

def faq(request):
	return render_to_response('faq.html')

def about(request):
	return render_to_response('aboutus.html')

def form(request):
	return render_to_response('form.html')