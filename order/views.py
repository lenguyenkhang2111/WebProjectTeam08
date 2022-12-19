import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from .models import Order, OrderDetail
# Create your views here.


@login_required
def checkout(request):
    try:
        data = json.load(request)
        total = data['total']
        # Lấy bản ghi Cart
        cart = Cart.objects.get(
            user=request.user)
        # Tạo 1 bản ghi Order
        order = Order(
            user=request.user,
            total=total,
        )
        order.save()

        # Chuyển hết CartItem thành OrderDetail
        cart_items = CartItem.objects.filter(
            cart__user=request.user, cart=cart)
        for cart_item in cart_items:
            order_detail = OrderDetail()
            order_detail.price = cart_item.course.price
            order_detail.course = cart_item.course
            order_detail.order = order
            order_detail.save()

        # Xóa hết CartItem
        CartItem.objects.filter(
            cart__user=request.user, cart=cart).delete()
        order.payment_status = 'C'
        order.save()
        # Gửi thư cảm ơn
        # Phản hồi lại Ajax
        data = {
            'order_id': order.pk
        }
        return JsonResponse({'data': data}, status=200)
    except Exception as e:
        order.payment_status = 'F'
        return JsonResponse({"error": e}, status=400)
