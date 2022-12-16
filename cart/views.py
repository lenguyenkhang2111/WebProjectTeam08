from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from course.models import Course
from account.models import Account
from .models import Cart, CartItem
# Create your views here.


def create_cart(request):
    if request.user.is_authenticated:
        cart_exist = Cart.objects.filter(
            user__username=request.user.username).exists
        if not cart_exist:
            cart = Cart(user=request.user)
            cart.save()


def add_cart(request, course_slug=None):
    current_user = request.user
    course = Course.objects.get(slug=course_slug)
    is_exists_cart_item = CartItem.objects.filter(
        course=course, cart__user=current_user).first()

    if current_user.is_authenticated:
        cart = Cart.objects.get(user=current_user)
        if is_exists_cart_item is None:
            cart_item = CartItem.objects.create(course=course, cart=cart)
            cart_item.save()
    return redirect('cart')


def remove_cart(request):
    pass


def remove_cart_item(request):
    pass


@login_required
def cart(request):
    try:
        if request.user.is_authenticated:
            cart = Cart.objects.get(user=request.user)
            cart_items = CartItem.objects.filter(cart=cart)
            for cart_item in cart_items:
                total += cart_item.course.price
    except ObjectDoesNotExist:
        pass
    context = {
        'cart_items': cart_items,
        'total': total if "total" in locals() else "",
    }
    return render(request, 'cart/cart.html', context=context)
