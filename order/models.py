from django.db import models
from account.models import Account
from django.core.validators import MinValueValidator
from course.models import Course

# Create your models here.


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2,
                                validators=[MinValueValidator(0)], blank=True, null=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    user = models.ForeignKey(Account, on_delete=models.PROTECT)

    def get_payment_status(self):
        return self.get_payment_status_display()


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator(1)])
