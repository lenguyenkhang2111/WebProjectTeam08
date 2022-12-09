from django.shortcuts import render
from django.urls import reverse
from course.models import Course


def home(request):
    courses = Course.objects.all().filter(course_status='A').order_by('pk')[:3]
    context = {
        'courses': courses
    }
    return render(request, 'home.html', context=context)
