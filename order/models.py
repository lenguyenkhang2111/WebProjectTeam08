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
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return "Order " + str(self.id)

    def get_payment_status(self):
        return self.get_payment_status_display()

    def get_order_details(self):
        return self.orderdetail_set.all()


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,
                                validators=[MinValueValidator(1)], null=True)
    SUBSCRIPTION_TYPE_MONTHLY = 'M'
    SUBSCRIPTION_TYPE_ANNUALLY = "A"
    SUBSCRIPTION_TYPE_CHOICES = [
        (SUBSCRIPTION_TYPE_MONTHLY, 'Monthly'),
        (SUBSCRIPTION_TYPE_ANNUALLY, 'Annually'),
    ]
    subscription_type = models.CharField(
        max_length=1, choices=SUBSCRIPTION_TYPE_CHOICES, null=True)

    def __str__(self):
        return "Order " + str(self.id)
