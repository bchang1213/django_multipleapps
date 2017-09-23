from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def surveyindex(request):
	response = "placeholder to later display all the list of surveys"
	return HttpResponse(response)

def newsurvey(request):
	response = "placeholder to later display new surveys"
	return HttpResponse(response)