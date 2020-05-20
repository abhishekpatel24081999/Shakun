from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView,FormView,View
from Owner.models import *
from .models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .decorator import *
from allauth.account.decorators import verified_email_required
from .forms import ProfileForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from datetime import datetime
# Create your views here.
from Project.settings import MERCHANT_KEY,MERCHANT_ID

from django.views.decorators.csrf import csrf_exempt
from Project import Checksum


@method_decorator([check_city], name='dispatch')
class HomeView(TemplateView):
    template_name = "karma/index.html"
    

@method_decorator([check_city], name='dispatch')
class ProductListView(View):
    def get(self,request, *args, **kwargs):
        product = Product.objects.filter(city = City.objects.get(name = request.COOKIES.get("city")))
        
        com = set(val.category.name for val in product)

        page = request.GET.get('page', 1)
        paginator = Paginator(product, 10)

        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            product = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)

        cart = Cart.objects.filter(user = request.user)
        c = []
        for data in cart:
            c.append(data.product.id)
        
        return render(request,"karma/category.html",{"product":product,"category":com,"cart":c})

@method_decorator([check_city], name='dispatch')
class ProductView(View):
    def get(self,request, *args, **kwargs):
        id = kwargs['id']
        product = Product.objects.filter(id = id)
        return render(request,"karma/single-product.html",{"product":product})

@method_decorator([login_required(login_url="/accounts/login"),verified_email_required,check_profile,check_city], name='dispatch')
class CartListView(View):
    def post(self,request):
        if request.POST.get("submit") == "delete":
            id = request.POST.get("id")
            obj = Cart.objects.filter(id = id)
            obj.delete()
        return render(request,'karma/cart.html',{"cart":obj})
    def get(self,request):
        obj = Cart.objects.filter(user = request.user)
        return render(request,'karma/cart.html',{"cart":obj})

@method_decorator([login_required(login_url="/accounts/login"),verified_email_required,check_profile,check_city], name='dispatch')
class AddCartView(View):
    def get(self,request, *args, **kwargs):
        print("hii")
        try:
            id = kwargs['id']
            user = request.user
            product = Product.objects.get(id = id)

            obj = Cart.objects.create(user=user,product=product)
            obj.save()
        except:
            pass
        return redirect("/cart")

@method_decorator([login_required(login_url="/accounts/login"),verified_email_required,check_profile,check_city], name='dispatch')
class AppointmentView(View):
    def post(self,request, *args, **kwargs):
        address = Address.objects.create(user=request.user)
        address.address = request.POST.get("adr")
        address.village = request.POST.get("vlg")
        address.pin = int(request.POST.get("pin"))
        address.save()

        product=Product.objects.get(id=request.POST.get("id"))
        appointment = Appointment.objects.create(user=request.user,product=product,address=address)
        appointment.day =  request.POST['day']
        appointment.save()
        product.appointment_count += 1
        product.save()
        cart = Cart.objects.get(user = request.user,product=Product.objects.get(id=request.POST.get("id")))
        cart.delete()
        return redirect("/appointment")
    def get(self,request, *args, **kwargs):
        try:
            id = kwargs['id']
            cart = Cart.objects.filter(id = id)
            return render(request,'karma/appointment.html',{"cart":cart})
        except:
            pass
        return redirect("/cart")

@method_decorator([login_required(login_url="/accounts/login"),verified_email_required,check_profile,check_city], name='dispatch')
class AppointmentListView(View):
    def post(self,request):
        if request.POST.get("submit") == "delete":
            id = request.POST.get("id")
            obj = Appointment.objects.filter(id = id)
            status = ""
            for data in obj:
                status = data.status
            if status == False:
                obj.delete()
            else:
                pass
        return render(request,'karma/cart.html',{"cart":obj})
    def get(self,request, *args, **kwargs):
        appointment = Appointment.objects.filter(user = request.user)
        return render(request,"karma/appointment_list.html",{"data":appointment})

def hii(request):
    response=redirect("/")
    response.set_cookie('city',"Ahmedabad")
    
    return response

class LatLong(View):
    def post(self,request):
        if "city" in request.COOKIES:
            return redirect("/home")
        else:
            obj = City.objects.filter(name = request.POST.get("city"))
            if  obj != 0:
                response=JsonResponse(data={})
                response.set_cookie('city',request.POST.get("city"))
                
                return response
            else:
                messages.error(request,'Error SUCCESSFULLY')
                return JsonResponse()

    def get(self,request, *args, **kwargs):
        if "city" in request.COOKIES:
            return redirect("/home")
        else:
            return render(request,'karma/location.html')

@method_decorator([login_required(login_url="/accounts/login"),verified_email_required,check_city], name='dispatch')       
class EditProfileView(View):
    # OTP = 0
    # def post(self,request):
    #     instance = Profile.objects.get(user=request.user)
    #     form = ProfileForm(request.POST or None, request.FILES or None,instance=instance )
    #     if self.OTP == int(request.POST['otp']):
    #         if form.is_valid():
    #             form.save(commit=False)
    #             form.save()
    #             messages.success(request,'Added successfully..')
    #             return redirect("/home")
    #         else:
    #             messages.error(request, 'Please correct the error below..')
    #         return redirect(f"/home")
    #     else:
    #         return redirect(f"/editprofile")

    def post(self,request):
        instance = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST or None, request.FILES or None,instance=instance )
        if form.is_valid():
            form.save(commit=False)
            form.save()
            messages.success(request,'Added successfully..')
            return redirect("/home")
        else:
            messages.error(request, 'Please correct the error below..')
        return redirect(f"/editprofile")

    # def contactconfo(self,request):
    #     self.OTP = 1234
    #     # send otp
    #     messages.success(request,'Added successfully..')
    #     return JsonResponse()

    def get(self,request):
        instance = Profile.objects.get(user=request.user)
        form = ProfileForm(instance=instance)
        return render(request,"karma/edit-profile.html",{"form":form,"profile":instance})

@method_decorator([login_required(login_url="/accounts/login"),verified_email_required(login_url="/accounts/login"),check_profile,check_city], name='dispatch')
class ProfileView(View):
    def get(self,request):
        profile = Profile.objects.get(user=request.user)
        return render(request,"karma/profile.html",{"profile":profile})   


class SearchView(View):
    def get(self,request):
        data = request.GET.get("data")
        product = Product.objects.filter(name__icontains = data)


        obj = Product.objects.filter(city = City.objects.get(name = request.COOKIES.get("city")))
        com = set(val.category.name for val in obj)
        
        page = request.GET.get('page', 1)
        paginator = Paginator(product, 15)

        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            product = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)


        return render(request,"karma/category.html",{"product":product,"category":com})

class CategoryView(View):
    def get(self,request, *args, **kwargs):
        data = kwargs['data']
        c = Category.objects.get(name = data)
        product = Product.objects.filter(category = c)
        obj = Product.objects.filter(city = City.objects.get(name = request.COOKIES.get("city")))
        com = set(val.category.name for val in obj)
        # cart = Cart.objects.filter(user = request.user,product=product)
        # print(cart)

        page = request.GET.get('page', 1)
        paginator = Paginator(product, 15)

        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            product = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)

        cart = Cart.objects.filter(user = request.user)
        c = []
        for data in cart:
            c.append(data.product.id)
        
        return render(request,"karma/category.html",{"product":product,"category":com,"cart":c})



class AdvancePayView(View):
    def get(self,request, *args, **kwargs):
        id = kwargs['id']
        appointment = Appointment.objects.get(id=id)
        if appointment.advance_pay_s == False:
            redirect("/home")
        amount = appointment.advance_amount
        c_id = Profile.objects.get(user=request.user)
        param_dict = {
                'MID': 'EcfAhw21043045854340',
                'ORDER_ID': str(appointment.id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': c_id,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/emp/handleadvancerequest/',
                    }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, 's&rzK!1j9xBQ%SEa')
        return render(request, 'paytm.html', {'param_dict': param_dict})

@csrf_exempt
def handleadvancerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})

class LastPayView(View):
    def get(self,request, *args, **kwargs):
        id = kwargs['id']
        appointment = Appointment.objects.get(id=id)
        if appointment.last_pay_s == False:
            redirect("/home")
        amount = appointment.last_amount
        c_id = Profile.objects.get(user=request.user)
        param_dict = {
                'MID': 'EcfAhw21043045854340',
                'ORDER_ID': str(appointment.id),
                'TXN_AMOUNT': str(amount),
                'CUST_ID': c_id,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8000/emp/handlelastrequest/',
                    }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, 's&rzK!1j9xBQ%SEa')
        return render(request, 'paytm.html', {'param_dict': param_dict})

@csrf_exempt
def handlelastrequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})


