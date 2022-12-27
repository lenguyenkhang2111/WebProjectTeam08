from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django_resized import ResizedImageField
from django.contrib.auth.decorators import login_required
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    best_seller_course = models.ForeignKey(
        'Course', on_delete=models.SET_NULL, null=True, related_name='best_seller', blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def get_url(self):
        return reverse('course_by_category', args=[self.slug])

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField(null=True,
                                        validators=[MinValueValidator(0)], blank=True)
    instructor = models.CharField(max_length=50)
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
    image = ResizedImageField(size=[500, 300], crop=['middle', 'center'],  upload_to="course/course_image/", null=True, quality=100
                              )
    video = models.FileField(
        upload_to="course/course_video", null=True)
    slug = models.SlugField(max_length=200, unique=True,
                            null=True, blank=True)

    def get_url(self):
        return reverse('course_detail', args=[self.slug])

    def get_video_url(self):
        return reverse('course_watching', args=[self.slug])

    def add_to_cart_url(self):
        return reverse('add_cart', args=[self.slug])

    def __str__(self):
        return self.title
