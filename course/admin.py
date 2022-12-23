from django.contrib import admin
from .models import Category, Course
from course.models import Category, Course
from django.db.models.aggregates import Count
from import_export.admin import ImportExportModelAdmin


class CourseInline(admin.StackedInline):
    model = Course
    extra = 0


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title',  'best_seller_course', 'courses_count')
    inlines = [CourseInline]
    extra = 0

    @admin.display(ordering='courses_count')
    def courses_count(self, category):
        return category.courses_count

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(courses_count=Count('course'))


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    list_display = ('title', 'description', 'price', 'category', 'course_status',
                    'instructor', 'lesson_number', 'course_status', 'rated', )

    prepopulated_fields = {'slug': ('title', )}
    list_editable = ('price', 'rated', 'course_status', 'lesson_number')
