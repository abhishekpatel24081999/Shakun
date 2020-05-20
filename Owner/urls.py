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
from django.urls import path
from .views import *

urlpatterns = [
    path('hii/',Hii.as_view(), name="Sign IN"),
    path('signin/',OwnerSignInView.as_view(), name="Sign IN"),
    # path("",HomeView.as_view(), name=""),
    path("add_emp/", EmployeeCreateView.as_view(), name=""),
    path("list_emp/", EmployeeListView.as_view(), name=""),
    path("add_product/", ProductCreateView.as_view(), name=""),
    # path("add_category/", CategoryCreateView.as_view(), name=""),
    path("list_product/", ProductListView.as_view(), name=""),
    path("list_product/", ProductListView.as_view(), name=""),
    path("appointment_manage/<int:id>", Manage_Appo.as_view(), name=""),
    path("list_manage_appointment/", Manage_AppoList.as_view(), name=""),
    #path("list_appp_product/", ProductAppointment.as_view(), name=""),
    path("", ProductAppointment.as_view(), name=""),
]
