from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from course.models import Category, Course
from cart.models import Cart, CartItem

# Create your views here.


def course(request, category_slug=None):
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.all().filter(category=categories, course_status='A')
    else:
        courses = Course.objects.all().filter(course_status='A').order_by('pk')

    page = request.GET.get('page')
    page = page or 1
    paginator = Paginator(courses, 6)
    paged_courses = paginator.get_page(page)
    course_count = courses.count()

    context = {
        'courses': paged_courses,
        'course_count': course_count,
    }
    return render(request, 'course/course.html', context=context)


def course_detail(request, course_slug=None):
    single_course = Course.objects.get(slug=course_slug)
    context = {
        'single_course': single_course,
    }
    return render(request, 'course/course_detail.html', context=context)
