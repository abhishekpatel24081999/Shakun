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
from . import views

urlpatterns = [
    path("hii", views.hii, name=""),
    path("", LatLong.as_view(), name=""),
    path("home/", HomeView.as_view(), name=""),
    path("shop/", ProductListView.as_view(), name=""),
    path("add_cart/<int:id>", AddCartView.as_view(), name=""),
    path("cart/", CartListView.as_view(), name=""),
    path("set_appointment/<int:id>",AppointmentView.as_view(), name=""),
    path("appointment/",AppointmentListView.as_view(), name=""),
    path("product/<int:id>",ProductView.as_view(), name=""),
    path("profile/",ProfileView.as_view(), name=""),
    path("editprofile/",EditProfileView.as_view(), name=""),
    # path("contactconfo/",EditProfileView.contactconfo(), name=""),
    path("search/",SearchView.as_view(), name=""),
    path("category/<str:data>",CategoryView.as_view(), name=""),
    path("advance_pay/<int:id>",AdvancePayView.as_view(), name=""),
    path("last_pay/<int:id>",LastPayView.as_view(), name=""),
]
