from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework import filters
import django_filters.rest_framework


from .models import User
from .serializers import UserSerializer, ShortUserSerializer


class MeUserApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user


class StrangerUserApiView(RetrieveAPIView):
    serializer_class = ShortUserSerializer
    queryset = User.objects.all()


class SuperUserApiView(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
    ]

    filter_fields = [
        ]

    search_fields = [
        'pk',
        'username',
    ]
