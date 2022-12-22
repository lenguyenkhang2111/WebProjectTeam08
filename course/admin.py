from django.contrib import admin
from . import models
from course.models import Category, Course, Instructor
from django.db.models.aggregates import Count


class CourseInline(admin.StackedInline):
    model = models.Course
    extra = 0


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title',  'best_seller_course', 'courses_count')
    inlines = [CourseInline]
    extra = 0

    @admin.display(ordering='courses_count')
    def courses_count(self, category):
        return category.courses_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(courses_count=Count('course'))


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'category', 'course_status',
                    'instructor', 'lesson_number', 'course_status', 'rated', )

    prepopulated_fields = {'slug': ('title', )}
    list_editable = ('price', 'rated', 'course_status', 'lesson_number')
