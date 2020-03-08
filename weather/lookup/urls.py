from django.urls import path
from . import views

urlpatterns = [
	#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=07310&distance=5&API_KEY=5EC6FBC6-7EFD-40B2-A94D-57D35B4A71D6
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
]
