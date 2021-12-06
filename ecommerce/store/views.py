from django.shortcuts import render
from .models import *
# Create your views here.
from django.http import JsonResponse
import json

"""
메인 페이지
모든 제품 표시
"""
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)  # 현재 가져온 customer의 order가 없으면 만들고 있으면 가져오기,
        items = order.orderitem_set.all()  # order에 있는 모든 items 가져오기
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    context ={'products':products,'cartItems':cartItems}
    return render(request,'store/store.html',context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created=Order.objects.get_or_create(customer=customer, complete=False) #현재 가져온 customer의 order가 없으면 만들고 있으면 가져오기,
        items = order.orderitem_set.all() #OrderItem은 Order의 자식이기 현재Order의 OrderItem을 소문자로 orderitem_set.all()로 가져올수 있음
        cartItems = order.get_cart_items

    else:
        items=[]
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    context ={'items':items, 'order':order,'cartItems':cartItems}
    return render(request,'store/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,
                                                     complete=False)  # 현재 가져온 customer의 order가 없으면 만들고 있으면 가져오기,
        items = order.orderitem_set.all()  # order에 있는 모든 items 가져오기
        cartItems = order.get_cart_items

    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
        cartItems = order['get_cart_items']

    context = {'items': items, 'order': order,'cartItems':cartItems}
    return render(request,'store/checkout.html',context)


def updateItem(request):#아이템 추가할때마다 제이슨 리스폰스 보냄
    data = json.loads(request.body) #json객체를 body를 data에저장 받고 data에 저장
    productId= data['productId'] #제이슨은 dict 형태이니 요렇게 접속 가능
    action = data['action']
    print('ProductId:', productId)
    print('Action:', action)

    customer = request.user.customer #현재 Customer 가져옴
    product = Product.objects.get(id=productId) #ID사용해서 현재 클릭한 product 저장
    order, created = Order.objects.get_or_create(customer=customer, #현재 customer의 order를 get or create
                                                 complete=False)  # 현재 가져온 customer의 order가 없으면 만들고 있으면 가져오기,
    orderItem, created = OrderItem.objects.get_or_create(order=order, #주문 아이템템
                                                         product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added!', safe=False)

def processOrder(request):
    print('Data:', request.body)
    return JsonResponse('Payment complete!', safe=False)