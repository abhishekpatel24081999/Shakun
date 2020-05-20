from django.shortcuts import render,redirect,reverse
from django.contrib.auth import login,authenticate
from django.views.generic import View,CreateView,ListView,TemplateView,FormView
from .models import *
from .forms import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .decorator import *
from Customer.models import Appointment
from Employee.models import ManageAppointment,Conform
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

# class Hii(FormView):
#     form_class = ProductForm
#     template_name = "metronic/add-product.html"
#     success_url ="/thanks/"

# class Hii(View):
#     def post(self,request):
#         form = ProductForm(request.POST or None, request.FILES or None)
#         if form.is_valid:
#             form.save()
#         else:
#             print("ERROR")
#         owner = Owner.objects.get(user=request.user)
#         id = owner.id
#         city = owner.city.id
#         return render(request, 'metronic/add-product.html',{"form":ProductForm(),"id":id,"city":city})

#     def get(self,request):
#         print(request.user)
#         owner = Owner.objects.get(user=request.user)
#         id = owner.id
#         city = owner.city.id
#         return render(request, 'metronic/add-product.html',{"form":ProductForm(),"id":id,"city":city})

class Hii(TemplateView):
    template_name = "metronic/list-product.html"


class Manage_AppoList(View):
    def post(self,request):
        m_a = request.POST.get("emp_id")
        manageAppointment = ManageAppointment.objects.get(id = m_a)
        conform = Conform.objects.get(manageAppointment = manageAppointment)
        return render(request,'metronic/add-product.html',{"conform":conform})

    def get(self,request):
        owner = Owner.objects.get(user=request.user)
        employee = Employee.objects.get(owner=owner)
        manageAppointment = ManageAppointment.objects.get(employee = employee)
        return render(request,'metronic/add-product.html',{"manageAppointment":manageAppointment})

class ProductAppointment(View):
    def get(self,request):
        owner = Owner.objects.get(user=request.user)
        product = Product.objects.filter(owner=owner)

        page = request.GET.get('page', 1)
        paginator = Paginator(product, 20)

        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            product = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)

        return render(template_name="metronic/product_app.html",context={"product":product,"owner":owner},request=request)

class Manage_Appo(View):

    def post(self,request, *args, **kwargs):
        p_id = kwargs['id']
        try:
            appo = request.POST.get("appo_id")
            emp = request.POST.get("emp_id")
            appointment = Appointment.objects.get(id = appo)
            employee = Employee.objects.get(id = emp)
            manageAppointment = ManageAppointment.objects.create(appointment = appointment,employee= employee)
            manageAppointment.save()
            appointment.status = True
            appointment.save()
            id = appointment.product.id
            product = Product.objects.get(id = id)
            product.appointment_count -=1 
            # messae
        except:
            pass
        
        owner = Owner.objects.get(user=request.user)
        product = Product.objects.get(id=p_id)
        appointment = Appointment.objects.filter(product=product)

        page = request.GET.get('page', 1)
        paginator = Paginator(appointment, 20)

        try:
            appointment = paginator.page(page)
        except PageNotAnInteger:
            appointment = paginator.page(1)
        except EmptyPage:
            appointment = paginator.page(paginator.num_pages)

        return render(request,'metronic/list-appointment.html',{"appointment":appointment})
    
    def get(self,request, *args, **kwargs):
        p_id = int(kwargs['id'])
        id = request.GET.get("pro_id")
        owner = Owner.objects.get(user=request.user)
        product = Product.objects.get(id=p_id)
        appointment = Appointment.objects.filter(product=product)
        employee = Employee.objects.filter(owner=owner)

        page = request.GET.get('page', 1)
        paginator = Paginator(appointment, 20)

        try:
            appointment = paginator.page(page)
        except PageNotAnInteger:
            appointment = paginator.page(1)
        except EmptyPage:
            appointment = paginator.page(paginator.num_pages)

        return render(request,'metronic/list-appointment.html',{"appointment":appointment,"employee":employee})

class OwnerSignInView(View):
    def post(self,request):
        usn = request.POST.get("usn")
        pwd = request.POST.get("pwd")
        user = authenticate(request,username=usn,password=pwd)
        if user:
            try:
                obj = Owner.objects.get(user=user)
                login(request,user)
                return redirect("/control")
            except:
                return redirect("/control/signin")
        else:
            return redirect("/control/signin")

    def get(self,request):
        return render(request, 'metronic/login.html')


@method_decorator([login_required(login_url="/control/signin"),owner_only], name='dispatch')
class HomeView(View):
    def get(self,request):
        return render(request, 'index.html')

class EmployeeCreateView(View):
    def post(self,request):
        # def get_context_data(self, **kwargs):
        #     kwargs['user_type'] = 'employee'
        #     return super().get_context_data(**kwargs)

        # def form_valid(self, form):
        #     user = form.save()

        form = EmployeeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/control')


    
        
    def get(self,request):
        owner = Owner.objects.get(user=request.user)
        form = EmployeeForm()
        return render(request,'metronic/add-employee.html',{"owner":owner,"form":form})


@method_decorator([login_required(login_url="/control/signin"),owner_only], name='dispatch')
class EmployeeListView(View):
    def get(self,request):
        owner = Owner.objects.get(user=request.user)
        employee = Employee.objects.filter(owner=owner)

        page = request.GET.get('page', 1)
        paginator = Paginator(employee, 20)

        try:
            employee = paginator.page(page)
        except PageNotAnInteger:
            employee = paginator.page(1)
        except EmptyPage:
            employee = paginator.page(paginator.num_pages)

        return render(request, 'metronic/list-employee.html',{"employee":employee,"owner":owner})

@method_decorator([login_required(login_url="/control/signin"),owner_only], name='dispatch')
class ProductCreateView(View):
    def post(self,request):
        try:
            instance = Product.objects.get(id = id)
            form = ProductForm(request.POST or None, request.FILES or None,instance=instance )
            
        except:
            print("hiiiii")
            form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print("bye")
            form.save(commit=False)
            form.save()
        # mail
            # messages.success(request,'Added successfully..')
        return redirect("/control")

    def get(self,request):
        owner = Owner.objects.get(user=request.user)
        try:
            id = request.POST.get("p_id")
            instance = Product.objects.get(id = id)
            Productform = ProductForm(instance=instance)
        except:
            Productform = ProductForm()
        return render(request, 'metronic/add-product.html',{"form":Productform,"owner":owner})

class ProductListView(View):
    def get(self,request):
        owner = Owner.objects.get(user=request.user)
        product = Product.objects.filter(owner=owner)

        page = request.GET.get('page', 1)
        paginator = Paginator(product, 20)

        try:
            product = paginator.page(page)
        except PageNotAnInteger:
            product = paginator.page(1)
        except EmptyPage:
            product = paginator.page(paginator.num_pages)

        return render(request, 'metronic/list-product.html',{"product":product,"owner":owner})

