from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    best_seller_course = models.ForeignKey(
        'Course', on_delete=models.SET_NULL, null=True, related_name='best_seller', blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    def get_url(self):
        return reverse('course_by_category', ars=[self.slug])

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator(1)])
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, blank=True, null=True)
    COURSE_STATUS_AVAILABLE = 'A'
    COURSE_STATUS_UNAVAILABLE = 'UA'
    COURSE_STATUS_CHOICES = [
        (COURSE_STATUS_AVAILABLE, 'Available'),
        (COURSE_STATUS_UNAVAILABLE, 'Unavailable')
    ]
    course_status = models.CharField(
        max_length=2, choices=COURSE_STATUS_CHOICES, default=COURSE_STATUS_AVAILABLE)
    rated = models.PositiveSmallIntegerField(null=True,
                                             validators=[MinValueValidator(0), MaxValueValidator(5)])
    duration = models.DurationField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True,
                              upload_to="product/course/image/")
    slug = models.SlugField(max_length=200, unique=True, null=True)

    def get_url(self):
        return reverse('course_detail', ars=[self.category.slug, self.slug])

    def __str__(self):
        return self.title
