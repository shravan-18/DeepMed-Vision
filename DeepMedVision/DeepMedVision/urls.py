"""
URL configuration for DeepMedVision project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from DeepMedApp import views as DeepMedAppViews

urlpatterns = [
    # Test URLs
    path('navbar/', DeepMedAppViews.navbar, name='navbar'),
    path('footer/', DeepMedAppViews.footer, name='footer'),
    # Main URLs
    path("admin/", admin.site.urls),
    path('', DeepMedAppViews.home, name='home'),
    path('login/', DeepMedAppViews.loginuser, name='loginuser'),
    path('logout/', DeepMedAppViews.logoutuser, name='logoutuser'),
    path('signup/', DeepMedAppViews.signupuser, name='signupuser'),
    path('dashboard/', DeepMedAppViews.dashboard, name='dashboard'),
    path('about/', DeepMedAppViews.about, name='about'),
    path('create_record/', DeepMedAppViews.create_record, name='create_record'),
    path('existing_records/', DeepMedAppViews.existing_records, name='existing_records'),
    path('contact/', DeepMedAppViews.contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
