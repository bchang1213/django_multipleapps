from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def blogsindex(request):
	return render(request, "blogs/index.html")

def new(request):
	response = "placeholder to later display new blogs"
	return HttpResponse(response)

def create(request):
	if request.method == "POST":
		print "*"*50
		print request.POST
		print request.POST['name']
		print request.POST['desc']
		request.session['name'] = request.POST['name']
		print "*"*50
		return redirect("/blogs")
	else:
		return redirect("/blogs")

def show(request, id):
	response = "placeholder to later display the id: " + id
	return HttpResponse(response)

def edit(request, id):
	response = "placeholder to later edit the id: " + id
	return HttpResponse(response)	

def destroy(request,id):
	response = "placeholder to later destroy the id: " + id
	return HttpResponse(response)	