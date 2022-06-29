from rest_framework import serializers

from .models import DiscordUserExt


class DiscordUserExtSerializer(serializers.ModelSerializer):
    is_oauth = serializers.BooleanField(read_only=True)
    discord_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = DiscordUserExt
        fields = (
            'id',
            'discord_id',
            'discord_name',
            'discord_server_name',

            'is_oauth',
        )
