from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    best_seller_course = models.ForeignKey(
        'Course', on_delete=models.SET_NULL, null=True, related_name='best_seller')


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator(1)])
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    COURSE_STATUS_AVAILABLE = 'A'
    COURSE_STATUS_UNAVAILABLE = 'UA'
    COURSE_STATUS_CHOICES = [
        (COURSE_STATUS_AVAILABLE, 'Available'),
        (COURSE_STATUS_UNAVAILABLE, 'Unavailable')
    ]
