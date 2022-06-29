from django.db import models
from account.models import User


class DiscordUserExt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    discord_id = models.BigIntegerField(null=True)
    discord_name = models.CharField(max_length=100, null=True)
    discord_server_name = models.CharField(max_length=100, null=True)

    is_oauth = models.BooleanField(default=False, null=True)
