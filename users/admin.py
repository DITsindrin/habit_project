from django.contrib import admin
from users.models import User


# Register your models here.
@admin.register
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ('email', 'telegram_id', 'phone', 'city',)
