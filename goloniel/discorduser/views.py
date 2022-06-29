from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import RetrieveUpdateDestroyAPIView
import django_filters.rest_framework


from .models import DiscordUserExt
from .serializers import DiscordUserExtSerializer


class MyDiscordApiView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DiscordUserExtSerializer
    queryset = DiscordUserExt.objects.all()

    def get_object(self):
        return self.queryset.get(pk=self.request.user.discorduserext.id)


class SuperDiscordApiView(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = DiscordUserExtSerializer
    queryset = DiscordUserExt.objects.all()
