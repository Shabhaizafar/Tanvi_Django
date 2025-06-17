from django.contrib import admin
from .models import Member
# from .models import Student


class AdminUser(admin.ModelAdmin):
    list_display = ("firstname","lastname")
# Register your models here.
admin.site.register(Member,AdminUser)