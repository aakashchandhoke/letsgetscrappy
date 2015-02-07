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
	""" View for the home page"""
	if request.POST:
		name = request.POST['name']
		message = request.POST['message']
		email = request.POST['email']
		send_mail(email, name+ "\n" + message,"scrappy0089@gmail.com","scrappy0089@gmail.com".split(' '), fail_silently=False)
	return render_to_response('index.html',context_instance=RequestContext(request))

def greetings(request):
	""" View for the greetings list page """
	return render_to_response('greeting.html')

def collage(request):
	""" View for the collages page """
	return render_to_response('collages.html')

def scrapbook(request):
	""" View for the scrapbook page """
	return render_to_response('scrapbook.html')

def calendar(request):
	""" View for the Calender page """
	return render_to_response('calendar.html')

def faq(request):
	""" View for the faq page """
	return render_to_response('faq.html')

def about(request):
	""" View for the about page """
	return render_to_response('aboutus.html')

def thankyou(request):
	""" View for the registration form page """
	if request.POST:
		name = request.POST['name']
		email = request.POST['email']
		phno = request.POST['phno']
		quantity = request.POST['quantity']
		comment = request.POST['comment']
		options = request.POST["selectone"]
		send_mail("PRODUCT ORDER"," name: "+ name+"\n" + "email: "+ email+"\n"+ "phno:"+phno+"\n"+ "options:"+options+"\n"+ "quantity:"+quantity+"\n"+ "comment:"+comment+"\n","scrappy0089@gmail.com","scrappy0089@gmail.com".split(' '), fail_silently=False)
	return render_to_response('thankyou.html',context_instance=RequestContext(request))

def form(request):
	return render_to_response('form.html',context_instance=RequestContext(request))