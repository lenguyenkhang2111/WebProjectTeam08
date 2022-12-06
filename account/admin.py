from django.contrib import admin
from account.models import Profile

from account.models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name',
                    'last_name', 'last_login', 'is_active')
    # Các trường có gắn link dẫn đến trang detail
    list_display_links = ('email', 'username', 'first_name', 'last_name')

    # Bắt buộc phải khai báo
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)

admin.site.register(Profile)
