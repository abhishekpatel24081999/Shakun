"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import auth
from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = [
    path('ajax_select/', include(ajax_select_urls)),
    path('admin/', admin.site.urls),
    path("email_validation/",auth.validate_username, name=""),
    path("control/",include("Owner.urls")),
    path("",include("Customer.urls")),
    path('jet_api/', include('jet_django.urls')),
    path("accounts/", include('allauth.urls')),
    path("emp/", include('Employee.urls')),
    path('tellme/', include("tellme.urls")),
    path('ckeditor/', include("ckeditor_uploader.urls")),
    path('pages/', include('django.contrib.flatpages.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

