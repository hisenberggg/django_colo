from django.contrib import admin
from .models import UserModel
# Register your models here.


class UserModelAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in UserModel._meta.fields if True]


admin.site.register(UserModel, UserModelAdmin)