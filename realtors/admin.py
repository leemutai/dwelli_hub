from django.contrib import admin

# Register your models here.

from .models import Realtor, User


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')


admin.site.register(User, UserAdmin)
admin.site.register(Realtor, RealtorAdmin)
