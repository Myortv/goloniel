from rest_framework import serializers
from .models import User

from discorduser.serializers import DiscordUserExtSerializer
from masters.serializers import MasterSerializer, PlayerSerializer



class UserSerializer(serializers.ModelSerializer):
    discorduserext = DiscordUserExtSerializer(read_only=True)
    master = MasterSerializer(read_only=True)
    learner = PlayerSerializer(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    date_joined = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'is_active',
            'is_superuser',
            'date_joined',

            'content',
            'quote',
            'pictogram',

            'learner',
            'master',
            'discorduserext'
        )



class ShortUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'is_active',
            'is_superuser',
            'last_login',

            'content',
            'quote',
            'pictogram',
        )
