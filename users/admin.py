from django.contrib import admin
from django.contrib.auth.models import Group, User
# Register your models here.

from .models import Profile

admin.site.unregister(Group)

# Move profile into user info
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username", "email"]
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)