from django.shortcuts import render , redirect
from .models import ProductCategory , Products , CartModel
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    trend = False
    Off = False

    if 'q' in request.GET:
        q=request.GET['q']
        data = Products.objects.filter(Q(pname__icontains=q) |Q(pdesc__icontains=q))


    elif 'category_form' in request.GET:
        category_form=request.GET['category_form']
        pc=ProductCategory.objects.filter(pcategory=category_form)
        data = Products.objects.filter(ProductCategory=pc[0].id)

    elif 'Trending' in request.GET:
        data = Products.objects.filter(Trending=1)
        trend=True

    elif 'Offer' in request.GET:
        data = Products.objects.filter(Offer=1)
        Off=True
    else:
        data = Products.objects.all()

    category_data = ProductCategory.objects.all()

    return render(request,'home.html',{'data':data ,'category_data':category_data,'trend':trend,'Off':Off})

@login_required(login_url='user_login')
def cart(request):

    cartproducts_count = CartModel.objects.filter(host = request.user).count()

    cartproducts = CartModel.objects.filter(host = request.user)

    ta = 0
    for i in cartproducts:
        ta += i.totalprice

    return render(request,'cart.html',{'cartproducts':cartproducts,'ta':ta,'profile_nav':True,'cartproducts_count':cartproducts_count})


@login_required(login_url='user_login')
def addtocart(request,pk):
    product=Products.objects.get(id=pk)

    try:
        cp=CartModel.objects.get(pname=product.pname,host=request.user)
        cp.quantity+=1
        cp.totalprice+=product.price
        cp.save()
        return redirect('cart')
    except:
        CartModel.objects.create(
            pname=product.pname,
            price=product.price,
            quantity=1,
            totalprice=product.price,
            host=request.user
        )
        return redirect('cart')

@login_required(login_url='user_login')
def remove(request,pk):
    Cartproduct=CartModel.objects.get(id=pk)
    Cartproduct.delete()
    return redirect('cart')

def details(request,pk):

    data = Products.objects.get(id=pk)

    return render(request,'details.html',{'data':data})


def aboutus(request):

    return render(request,'aboutus.html')

def support(request):

    return render(request,'support.html')

@login_required(login_url='user_login')
def shipping(request):

    return render(request,'shipping.html')

def increase_quantity(request, id):
    item = CartModel.objects.get(id=id, host=request.user)
    item.quantity += 1
    item.totalprice = item.quantity * item.price
    item.save()
    return redirect('cart')  

def decrease_quantity(request, id):
    item = CartModel.objects.get(id=id, host=request.user)
    if item.quantity > 1:
        item.quantity -= 1
        item.totalprice = item.quantity * item.price
        item.save()
    else:
        item.delete()  
    return redirect('cart')