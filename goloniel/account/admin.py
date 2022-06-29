from django.contrib import admin

from . import models



class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'is_superuser')
    search_fields = ('pk', 'username', 'email')



admin.site.register(models.User, UserAdmin)
