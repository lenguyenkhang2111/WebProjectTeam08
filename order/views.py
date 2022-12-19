from django.http import JsonResponse
from django.shortcuts import render

from cart.models import Cart, CartItem
from .models import Order, OrderDetail
# Create your views here.


def checkout(request):
    try:
        # check ajax có tồn tại hay không và lấy dữ liệu ra
        if request.is_ajax() and request.method == 'POST':
            data = request.POST
            cart_id = data['cartID']
            total = data['total']
            # Lấy bản ghi Cart
            cart = Cart.objects.get(
                user=request.user, pk=cart_id)
            # Tạo 1 bản ghi Order
            order = Order(
                user=request.user,
                price=total,
            )
            order.save()

            # Chuyển hết CartItem thành OrderDetail
            cart_items = CartItem.objects.filter(
                cart__user=request.user, cart=cart)
            for cart_item in cart_items:
                order_item = OrderDetail()
                order_item.price = cart_item.price
                order_item.course = cart_items.course
                order_item.order = order
                order_item.save()

            # Xóa hết CartItem
            CartItem.objects.filter(user=request.user, cart=cart).delete()

            # Gửi thư cảm ơn

            # Phản hồi lại ajax (điền vô)
            data = {

            }
        return JsonResponse({"data": data}, status=200)
    except Exception as e:
        return JsonResponse({"error": e}, status=400)
