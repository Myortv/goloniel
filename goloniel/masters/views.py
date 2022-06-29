from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import filters
import django_filters.rest_framework

from .serializers import PlayerSerializer, MasterSerializer
from .models import Player, Master


class MePlayerApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()

    def get_object(self):
        return self.queryset.get(user=self.request.user)


class SuperPlayerApi(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()


class MeMasterApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MasterSerializer
    queryset = Master.objects.all()

    def get_object(self):
        return self.queryset.get(user=self.request.user)


class SuperMasterApi(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = MasterSerializer
    queryset = Player.objects.all()
