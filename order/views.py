from email.message import EmailMessage
import json
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from WebProjectTeam08 import settings
from cart.models import Cart, CartItem
from .models import Order, OrderDetail
from django.template.loader import render_to_string
# Create your views here.


def sendEmail(request):
    mail_subject = 'Thank you for your payment!'
    message = render_to_string('order/order_received_email.html', {
        'user': request.user
    })
    to_email = request.user.email
    send_email = EmailMessage(mail_subject, message,
                              settings.EMAIL_HOST_USER, to=[to_email], fail_silently=True)
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
        # sendEmail(request)

        # Response to
        return JsonResponse({'data': 'Thanks'}, status=200)
    except Exception as e:
        order.payment_status = 'F'
        return JsonResponse({"error": e}, status=400)


@login_required
def payment_history(request, total_paid=0):
    orders = Order.objects.filter(user=request.user)
    for order in orders:
        total_paid += order.total
    context = {
        'orders': orders,
        'total_paid': total_paid
    }
    return render(request, 'order/payment_history.html', context=context)


@login_required
def purchased_courses(request):
    purchased_orders = OrderDetail.objects.all().filter(
        order__user=request.user, order__payment_status='C')
    if purchased_orders:
        for item in purchased_orders:
            courses = []
            courses.append(item.course)
    else:
        courses = None
    if courses != None:
        page = request.GET.get('page')
        page = page or 1
        paginator = Paginator(courses, 6)
        paged_courses = paginator.get_page(page)
        course_count = len(courses)
    else:
        paged_courses = 0
        course_count = 0
    context = {
        'courses': paged_courses,
        'course_count': course_count,
    }
    return render(request, 'order/purchased_courses.html', context=context)
