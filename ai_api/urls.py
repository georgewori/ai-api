"""
URL configuration for ai_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.conf import settings

# import the views from the app to be used for the root path
from api import views as api_views

def home_redirect(request):
    return redirect('/static/index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', lambda request: redirect("/api/generate/")), # redirect root url to /api/generate
   # path('api/generate/',api_views.generate_text,name='generate_text'), # The API view
    path('api/', include('api.urls')), # include the api app urls
    path('',home_redirect),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
