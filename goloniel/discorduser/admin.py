from django.contrib import admin

from . import models


class DiscordUserExtAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'discord_name')
    search_fields = ('pk', 'user', 'discord_name')


admin.site.register(models.DiscordUserExt, DiscordUserExtAdmin)
