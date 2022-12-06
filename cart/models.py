from django.db import models

from account.models import Account
from course.models import Course

# Create your models here.


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    customer = models.OneToOneField(Account, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
