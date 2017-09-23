from django.conf.urls import url
from . import views           # This line is new!
  

urlpatterns = [
	url(r'^$', views.surveyindex),    # This line has changed!
	url(r'^new$', views.newsurvey),
]