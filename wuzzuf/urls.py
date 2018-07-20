"""wuzzuf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import settings
from django.conf.urls.static import static
from user_profile.views import *
from profile_formset.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #ProfileCreateView
    path('add-profile/', ProfileCreateView.as_view(), name='profile-add'),
    path('', SignUp.as_view(), name='signup'),
    path('login', SignIn.as_view(), name='login'),
    path('home', Home.as_view(), name='home'),
    path('profile-formset/update/<int:pk>', CreateProfile.as_view(), name='profile-formset-add'),


]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)