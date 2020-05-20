from django.shortcuts import render,redirect
from django.views.generic import View
from Owner.models import Employee
from .models import ManageAppointment
from Customer.models import Appointment,Address,Profile
from .forms import ConformForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from .decorator import *
from django.contrib.auth.models import User
# Create your views here.

class LoginView(View):
    def post(self,request):
        usn = request.POST.get("usn")
        pwd = request.POST.get("pwd")
        user = authenticate(request,username=usn,password=pwd)
        if user:
            try:
                obj = Employee.objects.get(user=user)
                login(request,user)
                return redirect("/emp/appointment")
            except:
                return redirect("/emp/login")
        else:
            return redirect("/emp/login")
    def get(self,request):
        return render(request,"auth/login.html")

@method_decorator([login_required(login_url="/emp/login"),employee_only], name='dispatch')
class AppointmentView(View):

    def get(self,request):
        employee = Employee.objects.get(user=request.user)
        manageAppointment = ManageAppointment.objects.filter(employee = employee,status=False,reject=False)
        return render(request,"temp/list-appointment.html",{"manageAppointment":manageAppointment})


class Conform(View):
    def post(self,request, *args, **kwargs):
        id = kwargs['id']
        manageAppointment = ManageAppointment.objects.get(id = id)
        manageAppointment.status = True
        form = ConformForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save(commit=False)
            form.save()
            # messages.success(request,'Added successfully..')
        # for data in manageAppointment:
        appointment = Appointment.objects.get(id = manageAppointment.appointment.id)
        amount = int(request.POST.get("amount"))
        advance_amount = int(request.POST.get("a_amount"))
        last_amount = int(request.POST.get("l_amount"))

        if amount == advance_amount+last_amount:
            appointment.amount = amount
            appointment.advance_amount = advance_amount
            appointment.last_amount = last_amount

            appointment.c_status = True
            appointment.advance_pay_s = True
            appointment.save()
            manageAppointment.save()
            employee = Employee.objects.get(user=request.user)
            return redirect("/emp")

    def get(self,request, *args, **kwargs):
        id = kwargs['id']
        manageAppointment = ManageAppointment.objects.get(id = id)
        
        appointment = Appointment.objects.get(id = manageAppointment.appointment.id)
        c_user = Profile.objects.get(user = appointment.user)
        form = ConformForm()
        return render(request,"temp/conform.html",{"form":form,"appointment":appointment,"c_user":c_user,"manageAppointment":manageAppointment})


class Reject(View):
    def get(self,request, *args, **kwargs):
        id = kwargs['id']
        manageAppointment = ManageAppointment.objects.get(id = id)
        appointment = Appointment.objects.get(id = manageAppointment.appointment.id)
        manageAppointment.reject = True
        appointment.reject = True
        # Resion
        manageAppointment.save()
        appointment.save()
        return redirect("/emp")

class RejectListView(View):
    def get(self,request):
        employee = Employee.objects.get(user=request.user)
        manageAppointment = ManageAppointment.objects.filter(employee = employee,status=False,reject=True)
        return render(request,"temp/list-appointment.html",{"manageAppointment":manageAppointment})


def hii(request):
    return render(request,"temp/conform.html")