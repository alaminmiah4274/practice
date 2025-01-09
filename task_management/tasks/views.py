from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("Welcome to home...")


def contact(request):
	return HttpResponse("contact is running on django...")


def show_task(request):
	return HttpResponse("I want to show my tasks. But I do not have !!")