from django.contrib import admin

from product.models import Category, Course


class CategoryAdmin(admin.ModelAdmin):
    # Gợi ý trường slug theo category_name
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'slug', 'best_seller_course')
    readonly_fields = ['slug']


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'category', 'course_status',
                    'instructor', 'lesson_number', 'course_status', 'rated', 'image', 'duration', 'slug')
    readonly_fields = ['slug']
    prepopulated_fields = {'slug': ('title', )}


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
