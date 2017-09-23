from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def blogsindex(request):
	response = "placeholder to later display all the list of blogs"
	return HttpResponse(response)

def new(request):
	response = "placeholder to later display new blogs"
	return HttpResponse(response)

def create(request):
	return redirect('/blogs')

def show(request, id):
	response = "placeholder to later display the id: " + id
	return HttpResponse(response)

def edit(request, id):
	response = "placeholder to later edit the id: " + id
	return HttpResponse(response)	

def destroy(request,id):
	response = "placeholder to later destroy the id: " + id
	return HttpResponse(response)	