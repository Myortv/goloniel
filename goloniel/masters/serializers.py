from rest_framework import serializers

from .models import Player, Master



class PlayerSerializer(serializers.ModelSerializer):
    master = serializers.StringRelatedField()
    class Meta:
        model = Player
        fields = (
            'id',
            'user',
            'is_active',
            'content',
            'master',
        )


class MasterSerializer(serializers.ModelSerializer):
    # player = serializers.StringRelatedField(many=True)
    class Meta:
        model = Master
        fields = (
            'id',
            'user',
            'is_active',
            'content',
            # 'player',
        )
