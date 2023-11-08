from django.contrib import admin
from django.contrib.auth import get_user_model
from . models import *
from django.contrib.auth.admin import UserAdmin

User = get_user_model()
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Customer)


class PostAdmin(admin.ModelAdmin):
    list_display = ('type',)

admin.site.register(Post, PostAdmin)