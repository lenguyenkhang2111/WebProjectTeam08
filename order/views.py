from email.message import EmailMessage
import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from .models import Order, OrderDetail
from django.template.loader import render_to_string
# Create your views here.


def sendEmail(request, order):
    mail_subject = 'Thank you for your payment!'
    message = render_to_string('order/order_received_email.html', {
        'user': request.user,
        'order': order
    })
    to_email = request.user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()


@login_required
def checkout(request):
    try:
        data = json.load(request)
        total = data['total']
        # Get current Cart
        cart = Cart.objects.get(
            user=request.user)
        # Create new Order
        order = Order(
            user=request.user,
            total=total,
        )
        order.save()

        # Convert CartItem into OrderDetail
        cart_items = CartItem.objects.filter(
            cart__user=request.user, cart=cart)
        for cart_item in cart_items:
            order_detail = OrderDetail()
            order_detail.price = cart_item.course.price
            order_detail.course = cart_item.course
            order_detail.order = order
            order_detail.save()

        # Clean CartItems
        CartItem.objects.filter(
            cart__user=request.user, cart=cart).delete()
        order.payment_status = 'C'
        order.save()
        # Send email to thank
        sendEmail(request=request, order=order)

        # Response to
        data = {
            'order_id': order.pk
        }
        return JsonResponse({'data': data}, status=200)
    except Exception as e:
        order.payment_status = 'F'
        return JsonResponse({"error": e}, status=400)


def payment_history(request):
    pass
