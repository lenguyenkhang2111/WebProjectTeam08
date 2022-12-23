import datetime
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from django.urls import reverse
from course.models import Category, Course
from cart.models import Cart, CartItem
from django.db.models import Q

from order.models import OrderDetail


def course(request, category_slug=None):
    course_url = reverse('course')
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.all().filter(category=category, course_status='A')
    else:
        courses = Course.objects.all().filter(course_status='A').order_by('pk')
        category = None

    page = request.GET.get('page')
    page = page or 1
    paginator = Paginator(courses, 6)
    paged_courses = paginator.get_page(page)
    course_count = courses.count()
    # Get list of purchased courses
    if request.user.is_authenticated:
        purchased_orders = OrderDetail.objects.filter(
            order__user=request.user, order__payment_status='C')
        if purchased_orders:
            for item in purchased_orders:
                purchased_courses = []
                purchased_courses.append(item.course)
        else:
            purchased_courses = None
    else:
        purchased_courses = None

    context = {
        'courses': paged_courses,
        'course_count': course_count,
        'category': category,
        'course_url': course_url,
        'purchased_courses': purchased_courses,

    }
    return render(request, 'course/course.html', context=context)


def course_detail(request, course_slug=None):
    single_course = Course.objects.get(slug=course_slug)
    context = {
        'single_course': single_course,
    }
    return render(request, 'course/course_detail.html', context=context)


def search(request):
    if 's' in request.GET:
        s = request.GET.get('s')
        courses = Course.objects.order_by(
            'pk').filter(title__icontains=s)
        course_count = courses.count()
    context = {
        'courses': courses,
        's': s,
        'course_count': course_count
    }
    return render(request, 'course/course.html', context=context)


def course_watching(request, course_slug=None):
    course = Course.objects.get(slug=course_slug)
    context = {
        'course': course
    }
    return render(request, 'course/video.html', context=context)
