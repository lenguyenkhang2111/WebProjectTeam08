from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django_resized import ResizedImageField
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    best_seller_course = models.ForeignKey(
        'Course', on_delete=models.SET_NULL, null=True, related_name='best_seller', blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def get_url(self):
        return reverse('course_by_category', args=[self.slug])

    def __str__(self):
        return self.title


class Instructor(models.Model):
    name = models.CharField(max_length=50)


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator(1)])
    instructor = models.ForeignKey(
        Instructor, on_delete=models.CASCADE, blank=True, null=True)
    language = models.CharField(max_length=50, default='English')
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, blank=True, null=True)
    COURSE_STATUS_AVAILABLE = 'A'
    COURSE_STATUS_UNAVAILABLE = 'UA'
    COURSE_STATUS_CHOICES = [
        (COURSE_STATUS_AVAILABLE, 'Available'),
        (COURSE_STATUS_UNAVAILABLE, 'Unavailable')
    ]
    lesson_number = models.PositiveBigIntegerField(null=True,
                                                   validators=[MinValueValidator(0)], blank=True)
    course_status = models.CharField(
        max_length=2, choices=COURSE_STATUS_CHOICES, default=COURSE_STATUS_AVAILABLE)
    rated = models.PositiveSmallIntegerField(null=True,
                                             validators=[MinValueValidator(0), MaxValueValidator(5)], blank=True)
    duration = models.DecimalField(max_digits=6, decimal_places=2,
                                   validators=[MinValueValidator(0)], blank=True, null=True)
    image = ResizedImageField(size=[500, 300], crop=['middle', 'center'],  upload_to="course/course_image/", null=True, blank=True, quality=100
                              )
    slug = models.SlugField(max_length=200, unique=True,
                            null=True, blank=True)

    def get_url(self):
        return reverse('course_detail', args=[self.slug])

    def __str__(self):
        return self.title
