from django.shortcuts import render
from .models import *
# Create your views here.
def store(request):
    products = Product.objects.all()
    context ={'products':products}
    return render(request,'store/store.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created=Order.objects.get_or_create(customer=customer, complete=False) #현재 가져온 customer의 order가 없으면 만들고 있으면 가져오기,
        items = order.orderitem_set.all() #order에 있는 모든 items 가져오기
    else:
        item=[]
        order = {'get_cart_total':0, 'get_cart_items':0}
    context ={'items':items, 'order':order}
    return render(request,'store/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)  # 현재 가져온 customer의 order가 없으면 만들고 있으면 가져오기,
        items = order.orderitem_set.all()  # order에 있는 모든 items 가져오기
    else:
        item = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request,'store/checkout.html',context)
    