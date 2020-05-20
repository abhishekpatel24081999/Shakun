from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path("login/", LoginView.as_view(), name=""),
    path("", AppointmentView.as_view(), name=""),
    path("conform/<int:id>", Conform.as_view(), name=""),
    path("reject/<int:id>", Reject.as_view(), name=""),
    path("reject_list", RejectListView.as_view(), name=""),
    path("hii/", views.hii, name=""),
]
