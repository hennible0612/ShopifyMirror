import json
from . models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])  # 스트링으로 된거 풀고 cart에저장
    except:
        cart = {}
    print('Cart:', cart)
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    cartItems = order['get_cart_items']
    for i in cart:  # 카트에 들어있는 quantity확인인
        try:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id=i)  # 아이디 기준으로 product에 저장
            total = (product.price * cart[i]["quantity"])  # total 비용계산

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]["quantity"]

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },
                'quantity': cart[i]["quantity"],
                'get_total': total
            }
            items.append(item)

            if product.digital == False:
                order['shipping'] = True
        except:
            pass
    return {'cartItems':cartItems,'order':order,'items':items}

def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)  # 현재 가져온 customer의 order가 없으면 만들고 있으면 가져오기,
        items = order.orderitem_set.all()  # OrderItem은 Order의 자식이기 현재Order의 OrderItem을 소문자로 orderitem_set.all()로 가져올수 있음
        cartItems = order.get_cart_items

    else:
        cookieData = cookieCart(request) #쿠키가져옴
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    return {'items': items, 'order': order, 'cartItems': cartItems}