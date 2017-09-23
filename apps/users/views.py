from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
	response = "placeholder to later display the root route"
	return HttpResponse(response)

def register(request):
	response = "placeholder for registration"
	return HttpResponse(response)

def users(request):
	response = "placeholder for users"
	return HttpResponse(response)

def login(request):
	response = "placeholder for login"
	return HttpResponse(response)