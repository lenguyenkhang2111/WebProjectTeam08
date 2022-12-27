import datetime
from dateutil.relativedelta import relativedelta
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
        # Response to
        return JsonResponse({'data': 'Thanks'}, status=200)
    except Exception as e:
        order.payment_status = 'F'
        order.save()
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
        order__user=request.user, order__payment_status='C', subscription_type__isnull=True)
    if purchased_orders:
        for item in purchased_orders:
            courses = []
            courses.append(item.course)
    else:
        courses = None
    if courses != None:
        page = request.GET.get('page')
        page = page or 1
        paginator = Paginator(courses, 8)
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


@login_required
def subscription_checkout(request):
    try:
        # Loading json from fetch API
        data = json.load(request)
        total = data['total']
        type = data['type']
        # Create new order record
        order = Order(
            user=request.user,
            total=total,
        )
        order.save()
        # Create new order detail
        order_detail = OrderDetail()
        order_detail.order = order
        current_datetime = datetime.datetime.now()
        if type == 'M':
            order_detail.subscription_type = 'M'
            request.user.subscription_expired = current_datetime + \
                relativedelta(months=1)
            request.user.save()
            # Plus 1 month
        if type == 'A':
            # Plus 1 year
            order_detail.subscription_type = 'A'
            request.user.subscription_expired = current_datetime + \
                relativedelta(years=1)
            request.user.save()
        order_detail.price = total
        order_detail.save()
        order.payment_status = 'C'
        order.save()
        return JsonResponse({"data": 'Thanks'}, status=200)
    except Exception as e:
        order.payment_status = 'F'
        order.save()
        return JsonResponse({"error": e}, status=400)
