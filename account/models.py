from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_resized import ResizedImageField


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):

        # Create new user objects
        user = self.model(
            # Normalize email
            email=self.normalize_email(email=email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email=email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_superadmin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    subscription_expired = models.DateField(null=True, blank=True)
    image = ResizedImageField(
        upload_to="account/profile_pics/", null=True, blank=True, quality=100, default='account/profile_pics/doras.png')
    # REQUIRED_FIELDS
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
    objects = MyAccountManager()
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.username}'

    def has_perm(self, perm, obj=None):
        return self.is_admin    # Admin có tất cả quyền trong hệ thống

    def has_module_perms(self, add_label):
        return True

    def full_name(self):
        return self.first_name + " " + self.last_name
