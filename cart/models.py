from django.db import models
from django.urls import reverse

from account.models import Account
from course.models import Course

# Create your models here.


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(Account, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def get_remove_cart_item_url(self):
        return reverse('remove_cart_item', args=[self.pk])
