from django.shortcuts import render
from django.urls import reverse
from course.models import Course
from order.models import OrderDetail


def home(request):
    courses = Course.objects.all().filter(course_status='A').order_by('pk')[:3]
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
        'courses': courses,
        'purchased_courses': purchased_courses,
    }
    return render(request, 'home.html', context=context)
