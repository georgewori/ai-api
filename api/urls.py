from django.urls import path


from . import views
from . views import generate_text

urlpatterns = [
    path('', views.index, name='index'), # this will serve the html page
    path('generate/', views.generate_text, name='generate_text'), #API endpoint
]