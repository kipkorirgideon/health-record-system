from django.contrib import admin

from accounts import models


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'first_name', 'last_name', 'email', 'user_type',)
    search_fields = ('username', 'email')
    ordering = ('username', 'email')


admin.site.register(models.User, UserAdmin)