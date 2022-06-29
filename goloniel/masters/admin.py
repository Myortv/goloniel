from django.contrib import admin

from . import models


class MasterAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'is_active')
    search_fields = ('pk', 'user', 'is_active')


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'is_active', 'master')
    search_fields = ('pk', 'user', 'is_active', 'master')

class MasterRatingAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Master, MasterAdmin)
admin.site.register(models.Player, PlayerAdmin)
admin.site.register(models.MasterRatingModel, MasterRatingAdmin)
