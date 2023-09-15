from django.contrib.auth.models import Group

from django.shortcuts import render , redirect
from django.http import HttpResponse 
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth. decorators import login_required

import logging
# Create your views here.

from .models import*

from .forms import OrderForm, CreateUserForm , CustomerForm

from .filters import OrderFilter
from .decorators import unautheticated_user, allowed_users , admin_only

@unautheticated_user
def loginPage(request):

    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username/Password is incorrect")

    context ={}

    return render(request,"accounts/login.html", context)



def logoutPage(request):
    logout(request)
    return  redirect('login')

@unautheticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name="customer")
            user.groups.add(group)
            Customer.objects.create(user=user, name=user.username)
            messages.success(request,'Account was Created for' + username )
            return redirect("login")

    context = {"form":form}
    return render(request,"accounts/register.html", context)


@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()
    total_orders   = orders.count()

    context = {'orders': orders, 'customers':customers,
               'total_orders':total_orders,"delivered":delivered,
               "pending":pending , 
    } 

    return render(request, "accounts/dashboard.html",context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()
    context ={'orders':orders}
    
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()
    total_orders   = orders.count()
    context = {'orders':orders,'total_orders':total_orders,"delivered":delivered,
               "pending":pending }

    return render(request, "accounts/user.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method =="POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()


    context ={'form':form}
    return render(request,"accounts/account_settings.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    
    return render(request,"accounts/products.html",{"products":products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customers(request, pk):
    customer = Customer.objects.get(id=pk) 


    orders = customer.order_set.all()
    logging.info(orders)

    myFilter = OrderFilter(request.GET, queryset=orders)
    
    orders = myFilter.qs
    order_count = orders.count()
    context = {"customer":customer,"orders":orders, "order_count":order_count, 'myFilter': myFilter }


    return render(request,"accounts/customer.html", context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product','status'), extra =10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    # form = OrderForm(initial={'customer': customer})
    if request.method =="POST":
        print(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        # form = OrderForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect("/")


    context = {"formset":formset}
    return render(request, "accounts/order_form.html", context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method =="POST":
      # print(request.POST)
      form = OrderForm(request.POST, instance=order)

      if form.isvalid():
          form.save()
          return redirect("/")

    context = {"form":form}

    return render(request,"accounts/order_form.html",context) 



@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request,pk):
    
    order = Order.objects.get(id=pk)

    if request.method =="POST":
        order.delete()
        return redirect("/")
         
    context ={"item":order}

    return render(request,"accounts/delete.html", context)





@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateCustomer(request, pk):
    form = CustomerForm()  # Initialize form here

    try:
        customer = Customer.objects.get(id=pk)
    except Customer.DoesNotExist:
        print(f"Customer with id {pk} does not exist.")
        return HttpResponse("Customer not found", status=404)
    
    if customer.profile_pic:
        print(f"Profile Picture URL: {customer.profile_pic.url}")

    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            print("Form saved successfully")
        else:
            print("Form is invalid")

    context = {'form': form, 'customer': customer}
    return render(request, "accounts/account_settings.html", context)



